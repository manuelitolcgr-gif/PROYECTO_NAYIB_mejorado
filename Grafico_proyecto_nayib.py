st.subheader("Estado de los Viajes")

status_count = filtered_df['booking_status'].value_counts()
status_percent = (status_count / status_count.sum()) * 100

st.bar_chart(status_count)

st.write("Porcentaje de cada estado:")
st.write(status_percent.round(2))

