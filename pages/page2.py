import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
import pandas as pd

st.title("PAGE 2")


df = pd.DataFrame(
    {"id": [1,2,3], "url": [
        "https://images.unsplash.com/photo-1608848461950-0fe51dfc41cb?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8fA%3D%3D",
        "https://hips.hearstapps.com/hmg-prod/images/cute-cat-photos-1593441022.jpg?crop=0.670xw:1.00xh;0.167xw,0&resize=640:*",
        "https://t4.ftcdn.net/jpg/00/97/58/97/360_F_97589769_t45CqXyzjz0KXwoBZT9PRaWGHRk5hQqQ.jpg"]})

thumbnail_renderer = JsCode("""
class ThumbnailRenderer {
init(params) {
this.eGui = document.createElement('img');
this.eGui.setAttribute('src', params.value);
this.eGui.setAttribute('width', 'auto');
this.eGui.setAttribute('height', 'auto');
}
getGui() {
return this.eGui;
}
}
""")

builder = GridOptionsBuilder.from_dataframe(df)
builder.configure_default_column(editable=True, wrapText=True, autoHeight=True)
builder.configure_column("id", editable=False)
builder.configure_column("url", cellRenderer=thumbnail_renderer, flex=True)

# Display data with editable table
edited_df = AgGrid(df, builder.build(), allow_unsafe_jscode=True, height=200)
