---
name: CE 272 ปฏิบัติการกลศาสตร์ของไหล (Fluid Mechanics Laboratory)
description: A formal Thai worked-solution and lab revision portal matching cn271-fluid-mechanics architecture with KaTeX, Practice Mode, and Multi-Lab Calculator.
---

# Design & Architecture (สถาปัตยกรรมและหลักการออกแบบ)

โครงสร้างและสุนทรียภาพทางวิศวกรรมถอดแบบ 100% จาก [`cn271-fluid-mechanics`](https://github.com/thanakornnopp-dev/cn271-fluid-mechanics):
- ออกแบบให้อ่านง่ายเหมือนเอกสารวิชาการ / ชีทสรุปของภาควิชา (Centered single-column layout, max-width 800px)
- ฟอนต์มาตรฐาน Sarabun สำหรับภาษาไทย พร้อม KaTeX สำหรับทุกสมการคณิตศาสตร์
- ระบบหัวเรื่องมาตรฐาน: Gold kicker (`.kick`), Navy title (`h1`), Subtitle (`.sub`), Byline (`.by`), และ Practice mode note (`.pracnote`)

## Colour Tokens (CSS variables in `assets/style.css`)

| token | light | dark | ความหมายและการใช้งาน |
|---|---|---|---|
| `--bg` | #ffffff | #10131a | พื้นหลังหน้าเว็บ |
| `--ink` | #16181d | #e7eaf0 | สีตัวอักษรหลัก และเส้นแบ่ง |
| `--navy` | #14295b | #a9c1ff | หัวข้อหลัก, แท็บที่เลือก, ลิงก์ |
| `--gold` | #a8651a | #e3a556 | Kicker, ป้ายข้อสังเกต |
| `--blue` | #1c2fa8 | #86a0ff | ข้อมูลที่โจทย์กำหนด (Given data) |
| `--red` | #b3201f | #ff8178 | คำตอบสุดท้าย, จุดดักข้อสอบ (Trap) |
| `--green` | #17702a | #63d487 | การตรวจสอบผ่านเกณฑ์ (OK check) |
| `--hover` | #f4f6fa | #1c2230 | พื้นหลังแถบการ์ด และตาราง |

## Structure & UX

1. **Sticky Top Navigation (`nav.toc`):**
   - แถบเมนูด้านบนแบบตรึงติดหน้าจอ เลื่อนได้นุ่มนวลทั้งบนมือถือและจอคอมพิวเตอร์
   - ปุ่ม **"ฝึก" (Practice Mode):** ซ่อนขั้นตอนเฉลยวิธีทำ (`.exam .row`) เพื่อให้นักศึกษาลองคิดเลขเองก่อน แล้วแตะเพื่อเปิดดูเฉลยทีละบรรทัด
   - ปุ่ม **สลับโหมดมืด/สว่าง (Theme Toggle):** จดจำค่าผ่าน `localStorage.theme` และรองรับ `prefers-color-scheme`
2. **Single-Page Hash Routing (`assets/app.js`):**
   - แสดงเฉพาะ `<section>` ที่ตรงกับ URL hash (`#sum`, `#lab1` - `#lab11`, `#exam`, `#calc`, `#ref`)
   - เรียก KaTeX `renderMathInElement` อัตโนมัติเมื่อเปิดหน้านั้นๆ
3. **Universal Lab Calculator (`assets/calc.js`):**
   - เครื่องคิดเลขสด 10 โหมด ครอบคลุมการคำนวณของทุกบท
4. **Strict Thai Proofreading:**
   - ตรวจสอบอักขระภาษาไทย 100% ปราศจากตัวอักษรเพี้ยนจาก OCR (ไม่มี `ปŗด`, `เปŨน`, `โตŢะ`, `นาŲิกา` ฯลฯ)
