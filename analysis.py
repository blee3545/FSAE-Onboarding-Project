import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("data/08102025Endurance1_FirstHalf.csv")


print("Rows:", len(data))
print("Columns:", len(data.columns))
print("Columns sample:", data.columns[:10].tolist())

motor_temp = data["SME_TEMP_MotorTemperature"]
controller_temp = data["SME_TEMP_ControllerTemperature"]
brake_front = data["TMAIN_DATA_BRAKES_F"]
brake_rear = data["TMAIN_DATA_BRAKES_R"]
accel_x = data["VDM_X_AXIS_ACCELERATION"]
accel_y = data["VDM_Y_AXIS_ACCELERATION"]
accel_z = data["VDM_Z_AXIS_ACCELERATION"]

print("\n=== Basic Stats ===")
print(f"Motor Temp Avg: {motor_temp.mean():.2f} °C")
print(f"Controller Temp Avg: {controller_temp.mean():.2f} °C")
print(f"Front Brake Avg: {brake_front.mean():.3f}")
print(f"Rear Brake Avg: {brake_rear.mean():.3f}")
print(f"Avg Accel (Z-axis / gravity): {accel_z.mean():.2f}g")

plt.figure(figsize=(10, 5))
plt.plot(motor_temp, label="Motor Temp (°C)")
plt.plot(controller_temp, label="Controller Temp (°C)")
plt.title("Motor & Controller Temperature Over Time")
plt.xlabel("Sample")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("motor_temp_trend.png")
plt.close()

plt.figure(figsize=(6, 6))
plt.scatter(brake_front, brake_rear, alpha=0.5)
plt.title("Front vs Rear Brake Pressure")
plt.xlabel("Front Brake")
plt.ylabel("Rear Brake")
plt.grid(True)
plt.tight_layout()
plt.savefig("braking_correlation.png")
plt.close()

plt.figure(figsize=(8, 4))
plt.hist(accel_z, bins=50, color="skyblue", edgecolor="black")
plt.title("Z-axis Acceleration Distribution (Vertical G-Force)")
plt.xlabel("Acceleration (g)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("acceleration_hist.png")
plt.close()

print("\n Plots saved:")
print(" - motor_temp_trend.png")
print(" - braking_correlation.png")
print(" - acceleration_hist.png")
