# CE272 - ปฏิบัติการกลศาสตร์ของไหล (Fluid Mechanics Laboratory)
> คลังความรู้ สรุปเนื้อหาเตรียมสอบปฏิบัติการ ครบทุกบท (บทที่ 1 ถึง บทที่ 11)  
> จัดทำโดย **ธนภรณ์ นพรัตน์ (Thanaporn Nopparat)** • ภาควิชาวิศวกรรมโยธา คณะวิศวกรรมศาสตร์ มหาวิทยาลัยธรรมศาสตร์

---

## 🌐 เข้าชมเว็บแอปพลิเคชันออนไลน์ (Live Website)
👉 **GitHub Pages:** [https://thanakornnopp-dev.github.io/CE272/](https://thanakornnopp-dev.github.io/CE272/)

---

## 📖 สรุปเนื้อหาการทดลองครบทุกบท (All Laboratory Chapters)

1. **บทที่ 1: โต๊ะชลศาสตร์ (Hydraulic Bench) & การวัดอัตราการไหล**
   - ส่วนประกอบ: Sump Tank, Volumetric Tank, Dump Valve, Sight Glass
   - สูตรคำนวณอัตราการไหลจริง: $Q = \frac{\Delta V}{\Delta t}$
2. **บทที่ 2: จุดศูนย์กลางของแรงดัน (Center of Pressure)**
   - ทุ่นเสี้ยววงกลม (Quadrant): ทำไมผิวโค้งไม่เกิดโมเมนต์รอบจุดหมุน (แนวแรงพุ่งผ่านจุด Pivot)
   - กรณีจมบางส่วน ($d < D$): $F = \frac{1}{2}\rho g B d^2, y_{cp} = \frac{2}{3}d$
   - กรณีจมทั้งหมด ($d \ge D$): $F = \rho g B D(d - D/2), y_{cp} = y_c + \frac{I_{xx}}{y_c A}$
3. **บทที่ 3: แรงกระแทกของลำน้ำ (Impact of Jet)**
   - ฉากแบน ($90^\circ$ Flat plate): $F = \rho Q V = \rho A V^2$
   - ฉากครึ่งทรงกลม ($0^\circ / 180^\circ$ Hemispherical cup): $F = 2\rho Q V = 2\rho A V^2$ (**แรงเป็น 2 เท่า!**)
   - ฉากเอียง $\theta$: $F = \rho Q V (\cos\theta + 1)$
4. **บทที่ 4: สมการเบอร์นูลลี่และการประยุกต์ใช้ (Bernoulli & Venturi Tube)**
   - Hydraulic Grade Line (HGL: $P/\gamma + Z$) vs Energy Grade Line (EGL: $P/\gamma + V^2/2g + Z$)
   - ปรากฏการณ์ที่คอคอด (Throat): หน้าตัดแคบ $\to$ ความเร็วสูงสุด $\to$ ความดันตกต่ำสุด
   - $Q_{\text{theory}} = A_1 \sqrt{\frac{2g(h_1 - h_2)}{(A_1/A_2)^2 - 1}}, C_d = \frac{Q_{\text{actual}}}{Q_{\text{theory}}}$
5. **บทที่ 5: สมการแมนนิ่ง (Manning's Equation - ทางน้ำเปิด)**
   - $V = \frac{1}{n} R^{2/3} S^{1/2}$, $Q = \frac{1}{n} A R^{2/3} S^{1/2}$ ($R = A/P, S = \tan\theta$)
   - พื้นเรียบ ($n$ น้อย น้ำไหลเร็ว น้ำตื้น) vs พื้นหญ้า/ขรุขระ ($n$ มาก น้ำไหลช้า น้ำเอ่อสูง)
6. **บทที่ 6: การวัดอัตราการไหลด้วยฝาย (Flow over Weir)**
   - ฝายสี่เหลี่ยม (Rectangular Weir): $Q = C_d \frac{2}{3} B \sqrt{2g} H^{3/2}$ ($Q \propto H^{1.5}$)
   - ฝายสามเหลี่ยม (V-Notch Weir): $Q = C_d \frac{8}{15} \sqrt{2g} \tan(\theta/2) H^{5/2}$ ($Q \propto H^{2.5}$)
   - ฝาย $90^\circ$: $Q \approx 2.36 C_d H^{2.5}$ (วัดอัตราไหลต่ำได้แม่นยำกว่าฝายสี่เหลี่ยม)
7. **บทที่ 7: การสูญเสียพลังงานของการไหลในท่อ (Loss in Pipe Network)**
   - Major Loss (Darcy-Weisbach): $h_f = f \frac{L}{D} \frac{V^2}{2g} \propto \frac{Q^2}{D^5}$ (ท่อเล็กลงครึ่งหนึ่ง สูญเสียเพิ่ม 32 เท่า)
   - ท่อขนาน: Head loss เท่ากัน ($h_{L1} = h_{L2}$), อัตราไหลรวมกัน ($Q = Q_1 + Q_2$)
   - ท่ออนุกรม: อัตราไหลเท่ากัน ($Q_1 = Q_2$), Head loss รวมกัน ($h_{L,\text{total}} = h_1 + h_2$)
8. **บทที่ 8: การไหลผ่านรูลอด (Orifice, Jet Velocity and Trajectory)**
   - ปรากฏการณ์ Vena Contracta: หน้าตัดลำน้ำที่คอดตัวเล็กที่สุด
   - สัมประสิทธิ์ 3 ตัว: $C_v = \frac{x}{2\sqrt{yH}}, C_c = (d_c/d_0)^2, C_d = C_v \cdot C_c = \frac{Q_{\text{actual}}}{Q_{\text{theory}}}$
9. **บทที่ 9: การทดสอบเครื่องสูบน้ำ (Pump Test)**
   - ทางน้ำเข้า-ออก: ปั๊มเดี่ยว, ปั๊มอนุกรม ($h_1 = 0$, ได้ $2H$), ปั๊มขนาน (ได้ $2Q$)
   - ปรับหน้า Z: $H_d = h_d(\text{out}) - h_d(\text{in})$ (เดี่ยว $+0.15\text{ m}$, อนุกรม $-0.07\text{ m}$, ขนาน $+0.94\text{ m}$)
   - กำลังงานชลศาสตร์: $W_i = \gamma Q H$ ($\gamma = 9,810\text{ N/m}^3$)
   - กับดัก มล. $\to$ ลบ.ม. ($1\text{ L} = 10^{-3}\text{ m}^3, 1\text{ mL} = 10^{-6}\text{ m}^3$)
10. **บทที่ 10: การไหลลอดประตูน้ำ (Flow under Sluice Gate)**
    - พลังงานจำเพาะ: $E = y + \frac{V^2}{2g}$
    - ต้นน้ำ $y_0$ (Subcritical $Fr < 1$) vs ท้ายน้ำ $y_1$ (Supercritical $Fr > 1$)
    - $Q = C_d y_g B \sqrt{2gy_0}$
11. **บทที่ 11: รางน้ำแบบเวนจูรี่ (Venturi Flume)**
    - สภาพการไหลวิกฤตที่คอคอด ($Fr = 1$): $y_c = \frac{2}{3}H$
    - อัตราไหลทฤษฎี: $Q_{\text{theory}} = (2/3)^{1.5} \sqrt{g} b y_1^{1.5}$
    - ข้อดี: การสูญเสียต่ำและไม่เกิดตะกอนตกค้างหน้าคันเหมือนฝาย

---

## 🛠️ ฟังก์ชันพิเศษในเว็บ
- **Master Cheatsheet Table:** ตารางรวมสูตร 10 แล็ปในหน้าเดียว
- **Universal Lab Calculator:** เครื่องคิดเลขจำลองการแทนค่าสูตร 5 แล็ปหลัก พร้อมแปลงหน่วยอัตโนมัติ
- **All-Chapters Mock Exam (12 ข้อ):** ระบบข้อสอบปรนัยเสมือนจริง ตรวจคะแนนพร้อมเฉลยละเอียดและชี้จุดหลอกทุกข้อ
- **One-Click Printout:** กดปุ่มพิมพ์เป็นชีทสรุปสรุปย่อขนาด A4 ได้ทันที
