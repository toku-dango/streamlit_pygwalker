import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer

# Streamlitページの幅を調整する
st.set_page_config(
    page_title="StreamlitでPygwalkerを使う",
    layout="wide"
)

# タイトルを追加
st.title("StreamlitでPygwalkerを使う")

# サイドバーでファイルアップローダーを設定
uploaded_files = st.sidebar.file_uploader("CSVファイルをアップロードしてください", type=["csv"], accept_multiple_files=True)

if 'uploaded_files' not in st.session_state:
    st.session_state['uploaded_files'] = {}

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.session_state['uploaded_files'][uploaded_file.name] = uploaded_file

file_names = list(st.session_state['uploaded_files'].keys())
selected_file = st.sidebar.selectbox("表示するファイルを選択してください", file_names)

if selected_file:
    uploaded_file = st.session_state['uploaded_files'][selected_file]
    try:
        df = pd.read_csv(uploaded_file)
        st.write(f"選択されたデータファイル: {selected_file}")
        #st.write(df)  # データフレームの内容を表示

        # Pygwalkerを使用してデータを可視化
        pyg_app = StreamlitRenderer(df)
        vis_spec = pyg_app.explorer()
    except Exception as e:
        st.error(f"ファイルの読み込み中にエラーが発生しました: {e}")
