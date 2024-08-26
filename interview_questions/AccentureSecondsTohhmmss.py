def convert_seconds(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

# Example usage:
seconds_input = 3661
formatted_time = convert_seconds(seconds_input)
print(formatted_time)  # Output: 01:01:01
