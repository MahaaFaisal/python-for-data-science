# get the date in python
import datetime

dt = datetime.datetime.now(datetime.timezone.utc )

# Print Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
epoch_time = dt.timestamp()
epoch_to_scientific = "{:.2e}".format(epoch_time)

print("Seconds since January 1, 1970:", "{:,}".format(epoch_time), "or", epoch_to_scientific, "in scientific notation")

# # Print Oct 21 2022$
print(dt.strftime("%b %d %Y"))