import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def calculate_next_time():
    try:
        # รับค่าจาก Entry widgets
        user_name = entry_name.get()
        hours_str = entry_hours.get()
        minutes_str = entry_minutes.get()
        interval_str = entry_interval.get()

        # ตรวจสอบว่ากรอกข้อมูลครบไหม
        if not (user_name and hours_str and minutes_str and interval_str):
            messagebox.showwarning("แจ้งเตือน", "กรุณากรอกข้อมูลให้ครบทุกช่องครับ")
            return

        hours = int(hours_str)
        minutes = int(minutes_str)
        interval = int(interval_str)

        # ตรวจสอบความถูกต้องของเวลา
        if not (0 <= hours <= 23 and 0 <= minutes <= 59):
            messagebox.showerror("ข้อมูลผิดพลาด", "กรุณาป้อนชั่วโมง (0-23) และนาที (0-59) ให้ถูกต้อง")
            return
        
        if interval <= 0:
            messagebox.showerror("ข้อมูลผิดพลาด", "ช่วงเวลาแจ้งเตือนต้องมากกว่า 0")
            return

        # คำนวณเวลา
        current_datetime = datetime.now()
        last_dressing_time = current_datetime.replace(hour=hours, minute=minutes, second=0, microsecond=0)
        next_dressing_time = last_dressing_time + timedelta(hours=interval)

        # รูปแบบข้อความผลลัพธ์
        result_msg = f"ถึงเวลาทำแผลครั้งถัดไปตอน: {next_dressing_time.strftime('%H:%M น.')}"
        
        # 1. แสดงการแจ้งเตือนแบบ Popup เด้งขึ้นมา
        messagebox.showinfo("ตั้งค่าการแจ้งเตือนสำเร็จ", f"สวัสดีคุณ {user_name}\nระบบได้บันทึกเวลาไว้แล้ว\n\n{result_msg}")

        # 2. แสดงผลลัพธ์บนหน้าจอ GUI
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
root.title("ระบบบันทึกเวลาทำแผล - นาย ณฐภณ")
root.geometry("420x550")
root.configure(padx=25, pady=25)

# ส่วนหัวข้อ
tk.Label(root, text="🏥 ระบบแจ้งเตือนเวลาทำแผล", font=("Tahoma", 16, "bold"), fg="#1565C0").pack(pady=10)

# ช่องกรอกชื่อ
tk.Label(root, text="ชื่อผู้ป่วย:", font=("Tahoma", 10, "bold")).pack(anchor="w")
entry_name = tk.Entry(root, font=("Tahoma", 11))
entry_name.pack(fill="x", pady=5)

# ช่องกรอกชั่วโมงและนาที
frame_time = tk.Frame(root)
frame_time.pack(fill="x", pady=10)

tk.Label(frame_time, text="เวลาทำแผลล่าสุด (ชม.):", font=("Tahoma", 10)).grid(row=0, column=0, sticky="w")
entry_hours = tk.Entry(frame_time, width=10, font=("Tahoma", 11))
entry_hours.grid(row=1, column=0, padx=5, pady=5, sticky="w")

tk.Label(frame_time, text="นาที (0-59):", font=("Tahoma", 10)).grid(row=0, column=1, sticky="w")
entry_minutes = tk.Entry(frame_time, width=10, font=("Tahoma", 11))
entry_minutes.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# ช่องกรอกช่วงเวลา
tk.Label(root, text="ต้องทำแผลทุกๆ (กี่ชั่วโมง):", font=("Tahoma", 10, "bold")).pack(anchor="w", pady=(10, 0))
entry_interval = tk.Entry(root, font=("Tahoma", 11), fg="blue")
entry_interval.pack(fill="x", pady=5)

# ปุ่มคำนยณและเปิดการแจ้งเตือน
btn_calculate = tk.Button(root, text="🔔 คำนวณและตั้งการแจ้งเตือน", command=calculate_next_time, 
                          bg="#2E7D32", fg="white", font=("Tahoma", 11, "bold"), pady=10, cursor="hand2")
btn_calculate.pack(fill="x", pady=20)

# ส่วนแสดงผลลัพธ์บนหน้า GUI
label_result = tk.Label(root, text="", font=("Tahoma", 10), justify="left", bg="#F0F0F0", padx=10, pady=10)
label_result.pack(fill="x")

# --- ส่วนข้อมูลผู้จัดทำ ---
tk.Frame(root, height=1, bg="#CCCCCC").pack(fill="x", pady=15)
dev_info = "ผู้พัฒนา: นาย ณฐภณ แก่นไม้ เลขที่ 5\nโรงเรียนบางบ่อวิทยาคม"
tk.Label(root, text=dev_info, font=("Tahoma", 9, "italic"), fg="#666666").pack(side="bottom")

root.mainloop()
