import time
from picar.back_wheels import Back_Wheels

bw = Back_Wheels()
bw.ready()

print("Calibrating back wheels. They should move FORWARD. Ctrl+C to stop.")

try:
    bw.calibration()  # this sets speed and starts moving forward
    time.sleep(1)

    # If car is going backward, flip both
    print("Flipping both directions...")
    bw.cali_left()
    bw.cali_right()
    time.sleep(1)

    # Save the calibration to config
    bw.cali_ok()
    print("Calibration saved. Car should now move forward normally.")

except KeyboardInterrupt:
    print("Cancelled by user.")
    bw.stop()

finally:
    bw.stop()
