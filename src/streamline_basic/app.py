from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="지하철 혼잡도 대시보드", page_icon="🚇", layout="wide")

DATA_PATH = Path(__file__).parent / "data" / "서울교통공사_지하철혼잡도정보_20260930.csv"
METADATA_COLUMNS = ["구분", "호선", "역번호", "역명", "상하구분"]


@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    """CSV를 읽고 시간대 값을 숫자로 바꿉니다."""
    try:
        data = pd.read_csv(path, encoding="cp949")
    except UnicodeDecodeError:
        data = pd.read_csv(path, encoding="utf-8-sig")

    data.columns = data.columns.str.strip()
    data["역명"] = data["역명"].astype(str).str.strip()
    data["호선"] = data["호선"].astype(str).str.strip()
    data["구분"] = data["구분"].astype(str).str.strip()
    data["상하구분"] = data["상하구분"].astype(str).str.strip()
    time_cols = [column for column in data.columns if column not in METADATA_COLUMNS]
    data[time_cols] = data[time_cols].apply(pd.to_numeric, errors="coerce")
    return data


if not DATA_PATH.exists():
    st.error(f"CSV 파일을 찾을 수 없습니다: {DATA_PATH}")
    st.stop()

raw_csv = load_data(DATA_PATH)
time_columns = [column for column in raw_csv.columns if column not in METADATA_COLUMNS]
day_options = ["전체"] + sorted(raw_csv["구분"].dropna().unique().tolist())
direction_options = ["전체"] + sorted(raw_csv["상하구분"].dropna().unique().tolist())

st.title("서울 지하철 혼잡도")
st.caption("요일 유형, 노선, 역 방향별 30분 단위 혼잡도를 살펴봅니다.")

with st.sidebar:
    st.header("공통 필터")
    selected_day = st.selectbox("요일 유형", day_options)
    selected_direction = st.selectbox("역 방향", direction_options)

filtered = raw_csv.copy()
if selected_day != "전체":
    filtered = filtered[filtered["구분"] == selected_day]
if selected_direction != "전체":
    filtered = filtered[filtered["상하구분"] == selected_direction]

tab_overview, tab_lines, tab_station = st.tabs(["전체 현황", "노선 비교", "역별 상세"])

with tab_overview:
    st.subheader("전체 현황")
    all_values = filtered[time_columns].stack().dropna()
    if all_values.empty:
        st.info("선택한 조건에 표시할 데이터가 없습니다.")
    else:
        peak_row_index, peak_time = filtered[time_columns].stack().idxmax()
        peak_value = filtered.loc[peak_row_index, peak_time]
        peak_row = filtered.loc[peak_row_index]
        peak_label = f"{peak_row['역명']} · {peak_row['상하구분']} · {peak_time}"

        metric1, metric2, metric3 = st.columns(3)
        metric1.metric("평균 혼잡도", f"{all_values.mean():.1f}")
        metric2.metric("최고 혼잡도", f"{peak_value:.1f}")
        metric3.metric("최고 혼잡 구간", peak_label)

        hourly_average = filtered[time_columns].mean(axis=0).rename_axis("시간").reset_index(name="평균 혼잡도")
        st.subheader("시간대별 평균 혼잡도")
        st.plotly_chart(
            px.line(hourly_average, x="시간", y="평균 혼잡도", markers=True),
            use_container_width=True,
        )

        ranked = filtered[METADATA_COLUMNS + time_columns].copy()
        ranked["하루 최고 혼잡도"] = ranked[time_columns].max(axis=1)
        ranked["최고 시간"] = ranked[time_columns].idxmax(axis=1)
        ranked["역 방향"] = ranked["역명"] + " · " + ranked["상하구분"]
        top_rows = ranked.nlargest(10, "하루 최고 혼잡도").sort_values("하루 최고 혼잡도")
        st.subheader("하루 최고 혼잡도 상위 10개 역·방향")
        top_chart = px.bar(
            top_rows,
            x="하루 최고 혼잡도",
            y="역 방향",
            orientation="h",
            hover_data=["호선", "최고 시간"],
            labels={"하루 최고 혼잡도": "혼잡도", "역 방향": "역 · 방향"},
        )
        st.plotly_chart(top_chart, use_container_width=True)

with tab_lines:
    st.subheader("노선 비교")
    line_average = filtered.groupby("호선")[time_columns].mean()
    line_chart_data = line_average.rename_axis("호선").reset_index().melt(
        id_vars="호선", var_name="시간", value_name="평균 혼잡도"
    )
    st.markdown("#### 노선별 시간대 평균")
    st.plotly_chart(
        px.line(line_chart_data, x="시간", y="평균 혼잡도", color="호선", markers=True),
        use_container_width=True,
    )

    available_lines = sorted(filtered["호선"].dropna().unique().tolist())
    if available_lines:
        chosen_line = st.selectbox("히트맵에 표시할 노선", available_lines)
        line_data = filtered[filtered["호선"] == chosen_line]
        heatmap_data = line_data.groupby("역명")[time_columns].mean()
        st.markdown(f"#### {chosen_line} 역별 시간대 혼잡도")
        st.plotly_chart(
            px.imshow(
                heatmap_data,
                aspect="auto",
                color_continuous_scale="YlOrRd",
                labels={"x": "시간", "y": "역명", "color": "혼잡도"},
            ),
            use_container_width=True,
        )
    else:
        st.info("선택한 조건에 표시할 노선이 없습니다.")

with tab_station:
    st.subheader("역별 상세")
    available_lines = sorted(filtered["호선"].dropna().unique().tolist())
    if not available_lines:
        st.info("선택한 조건에 표시할 역이 없습니다.")
    else:
        chosen_line = st.selectbox("호선 선택", available_lines, key="station_line")
        station_data = filtered[filtered["호선"] == chosen_line]
        available_stations = sorted(station_data["역명"].dropna().unique().tolist())
        chosen_station = st.selectbox("역 선택", available_stations)
        selected_rows = station_data[station_data["역명"] == chosen_station]

        station_long = selected_rows.melt(
            id_vars=["구분", "상하구분"],
            value_vars=time_columns,
            var_name="시간",
            value_name="혼잡도",
        )
        station_long = station_long.dropna(subset=["혼잡도"])
        st.markdown(f"#### {chosen_line} {chosen_station} 시간대별 혼잡도")
        st.plotly_chart(
            px.line(
                station_long,
                x="시간",
                y="혼잡도",
                color="상하구분",
                line_dash="구분",
                markers=True,
                labels={"상하구분": "역 방향", "구분": "요일 유형"},
            ),
            use_container_width=True,
        )
        st.markdown("#### 시간대별 원자료")
        st.dataframe(
            station_long.pivot_table(
                index="시간", columns=["구분", "상하구분"], values="혼잡도"
            ),
            use_container_width=True,
        )

st.caption("혼잡도는 CSV 원자료 값이며, 단위와 산정 기준은 원자료 정의를 확인해 주세요.")
