def build_message(df_rain, date, query):
    message_string = (
    f"🌧️ Rain expected today in {query}\n"
    f"📅 {date}\n\n"
    )

    for _, row in df_rain.iterrows():
        message_string += (
            f"🕒 {row['Hour']:02d}:00 - "
            f"{row['Condition']} "
            f"({row['Chance_of_rain']}%)\n"
        )

    return message_string