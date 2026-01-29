import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def calculate_next_time():
    try:
        # รับค่าจาก Entry widgets
        user_name = entry_name.get()
        hours = int(entry_hours.get())
        minutes = int(entry_minutes.get())
        interval = int(entry_interval.get())

        # ตรวจสอบความถูกต้องของข้อมูล
        if not (0 <= hours <= 23 and 0 <= minutes <= 59):
            messagebox.showerror("ข้อมูลผิดพลาด", "กรุณาป้อนชั่วโมง (0-23) และนาที (0-59) ให้ถูกต้อง")
            return
        
        if interval <= 0:
            messagebox.showerror("ข้อมูลผิดพลาด", "ช่วงเวลาแจ้งเตือนต้องมากกว่า 0")
            return

        # คำนวณเวลา
        current_datetime = datetime.now()
        last_dressing_time = current_datetime.replace(hour=hours, minute=minutes, second=0, microsecond=0)
        
        # หากเวลาที่ป้อนมา "ผ่านไปแล้ว" ในวันนี้ (เช่น ป้อน 08:00 แต่ตอนนี้ 10:00) 
        # ระบบจะถือว่าเป็นของวันนี้ แต่ถ้าต้องการให้เป็นระบบเตือนล่วงหน้าก็ใช้ logic เดิมได้ครับ
        
        next_dressing_time = last_dressing_time + timedelta(hours=interval)

        # แสดงผลลัพธ์
        result_text = (
            f"สวัสดีคุณ {user_name}!\n"
            f"---------------------------\n"
            f"เวลาทำแผลล่าสุด: {last_dressing_time.strftime('%H:%M')}\n"
            f"ช่วงเวลาแจ้งเตือน: {interval} ชั่วโมง\n"
            f"เวลาทำแผลครั้งถัดไป: {next_dressing_time.strftime('%Y-%m-%d %H:%M')}"
        )
        label_result.config(text=result_text, fg="#2E7D32")

    except ValueError:
        messagebox.showerror("ข้อมูลผิดพลาด", "กรุณากรอกเฉพาะตัวเลขในช่องเวลาและช่วงเวลา")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("ระบบบันทึกเวลาทำแผล")
root.geometry("400x450")
root.configure(padx=20, pady=20)

# ส่วนหัวข้อ
tk.Label(root, text="🏥 บันทึกการทำแผล", font=("Tahoma", 16, "bold")).pack(pady=10)

# ช่องกรอกชื่อ
tk.Label(root, text="ชื่อผู้ป่วย:").pack(anchor="w")
entry_name = tk.Entry(root, font=("Tahoma", 10))
entry_name.pack(fill="x", pady=5)

# ช่องกรอกชั่วโมงและนาที (จัดวางแบบแนวนอน)
frame_time = tk.Frame(root)
frame_time.pack(fill="x", pady=5)

tk.Label(frame_time, text="เวลาที่ทำล่าสุด (ชม.):").grid(row=0, column=0, sticky="w")
entry_hours = tk.Entry(frame_time, width=5)
entry_hours.grid(row=1, column=0, padx=5, sticky="w")

tk.Label(frame_time, text="นาที:").grid(row=0, column=1, sticky="w")
entry_minutes = tk.Entry(frame_time, width=5)
entry_minutes.grid(row=1, column=1, padx=5, sticky="w")

# ช่องกรอกช่วงเวลา
tk.Label(root, text="แจ้งเตือนทุกๆ (ชั่วโมง):").pack(anchor="w", pady=(10, 0))
entry_interval = tk.Entry(root, font=("Tahoma", 10))
entry_interval.pack(fill="x", pady=5)

# ปุ่มคำนวณ
btn_calculate = tk.Button(root, text="คำนวณเวลาถัดไป", command=calculate_next_time, 
                          bg="#008CBA", fg="white", font=("Tahoma", 10, "bold"), pady=5)
btn_calculate.pack(fill="x", pady=20)

# ส่วนแสดงผลลัพธ์
label_result = tk.Label(root, text="", font=("Tahoma", 11), justify="left")
label_result.pack(pady=10)

root.mainloop()
