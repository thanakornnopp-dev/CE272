/* CE 272: Interactive Mock Exam Quiz Engine */
(function () {
  "use strict";

  var quizData = [
    {
      id: 1,
      lab: "บทที่ 9",
      topic: "ทิศทางการไหลและความดันด้านดูด",
      q: "ในการต่อเครื่องสูบน้ำแบบอนุกรม (Two Pumps in Series) ความดันด้านดูดของปั๊มตัวแรก (\\(h_1\\)) กำหนดให้มีค่าเท่าใดตามคู่มือปฏิบัติการหน้า 51?",
      choices: [
        "\\(h_1 = 1.0\\text{ m}\\) เพราะต้องมีแรงดันบวกคอยดันน้ำเข้าปั๊มเสมอ",
        "\\(h_1 = 0\\text{ m}\\) เพราะดูดน้ำตรงจากถัง Sump Tank ซึ่งเปิดสัมผัสกับความดันบรรยากาศ",
        "\\(h_1 = -0.24\\text{ m}\\) เท่ากับระดับความสูงติดลบของ Bench Pump Inlet",
        "\\(h_1 = 0.17\\text{ m}\\) เท่ากับระดับความสูงของ Outlet Gauge"
      ],
      correct: 1,
      expl: "ตามคู่มือปฏิบัติการหน้า 51 ข้อ 6 ระบุว่า ความดันที่จุดเข้าของปั๊มตัวแรกให้ถือว่าเป็นความดันบรรยากาศ หรือมีค่าเป็นศูนย์ (\\(h_1 = 0\\)) เนื่องจากดูดน้ำจากถังพักน้ำ (Sump Tank) ของ Hydraulic Bench โดยตรง"
    },
    {
      id: 2,
      lab: "บทที่ 9",
      topic: "ค่าปรับแก้ระดับเกจ (Datum Correction)",
      q: "ในการทดสอบปั๊มต่ออนุกรม (Series Pumps) กำหนดระยะความสูงเกจ \\(h_d(\\text{outlet}) = 0.17\\text{ m}\\) และ \\(h_d(\\text{bench}) = 0.24\\text{ m}\\) ค่าปรับแก้ระดับ Datum Head Correction (\\(H_d\\)) มีค่าเท่าใด?",
      choices: [
        "\\(+0.41\\text{ m}\\)",
        "\\(+0.07\\text{ m}\\)",
        "\\(-0.07\\text{ m}\\)",
        "\\(+0.15\\text{ m}\\)"
      ],
      correct: 2,
      expl: "สูตรคือ \\(H_d = h_d(\\text{outlet}) - h_d(\\text{inlet}) = 0.17 - 0.24 = -0.07\\text{ m}\\) มีค่าติดลบ! นี่คือจุดดักคะแนนอันดับ 1 ของอาจารย์ ถ้านักศึกษาเผลอใส่เป็นบวก \\(+0.07\\) จะทำให้ Total Head ผิดทันที"
    },
    {
      id: 3,
      lab: "บทที่ 9",
      topic: "สมรรถนะปั๊มอนุกรมเทียบกับปั๊มขนาน",
      q: "เครื่องสูบน้ำ 2 ตัวที่มีสมรรถนะเท่ากัน เมื่อนำมาต่อแบบอนุกรม (Series) และต่อแบบขนาน (Parallel) จะส่งผลต่อ Total Head (\\(H\\)) และ Discharge (\\(Q\\)) อย่างไรเทียบกับปั๊มเดี่ยว?",
      choices: [
        "อนุกรมได้อัตราไหล 2 เท่า (\\(2Q\\)), ขนานได้เฮด 2 เท่า (\\(2H\\))",
        "อนุกรมได้เฮด 2 เท่า (\\(2H\\)), ขนานได้อัตราไหล 2 เท่า (\\(2Q\\))",
        "ทั้งสองแบบได้เฮด 2 เท่า และอัตราไหล 2 เท่าเท่ากัน",
        "การต่ออนุกรมหรือขนานไม่มีผลต่อเฮดและอัตราไหล"
      ],
      correct: 1,
      expl: "การต่อแบบอนุกรม (Series) เพิ่มพลังงานความดันเป็น 2 เท่า (\\(2H\\)) ที่อัตราไหลเท่าเดิม เหมาะกับการส่งน้ำขึ้นที่สูง ส่วนการต่อแบบขนาน (Parallel) ช่วยเพิ่มปริมาณน้ำเป็น 2 เท่า (\\(2Q\\)) ที่ระดับเฮดเดิม เหมาะกับการระบายน้ำท่วม"
    },
    {
      id: 4,
      lab: "บทที่ 9",
      topic: "กับดักการแปลงหน่วย (มล. เป็น ลบ.ม.)",
      q: "ในการวัดอัตราการไหล ตวงน้ำได้ปริมาตร \\(V = 5,000\\text{ mL}\\) ในเวลา \\(t = 4.0\\text{ วินาที}\\) อัตราการไหลจริง (\\(Q\\)) ในหน่วย \\(\\text{m}^3/\\text{s}\\) มีค่าเท่าใด?",
      choices: [
        "\\(1,250\\text{ m}^3/\\text{s}\\)",
        "\\(1.25\\text{ m}^3/\\text{s}\\)",
        "\\(0.00125\\text{ m}^3/\\text{s}\\) (หรือ \\(1.25 \\times 10^{-3}\\text{ m}^3/\\text{s}\\))",
        "\\(0.00000125\\text{ m}^3/\\text{s}\\)"
      ],
      correct: 2,
      expl: "แปลงมิลลิลิตรเป็นลูกบาศก์เมตร: \\(1\\text{ mL} = 10^{-6}\\text{ m}^3\\) ดังนั้น \\(5,000\\text{ mL} = 5,000 \\times 10^{-6} = 0.005\\text{ m}^3\\) จะได้ \\(Q = \\frac{0.005}{4.0} = 0.00125\\text{ m}^3/\\text{s} = 1.25 \\times 10^{-3}\\text{ m}^3/\\text{s}\\)"
    },
    {
      id: 5,
      lab: "บทที่ 9",
      topic: "การคำนวณกำลังไฮดรอลิก (Power)",
      q: "เครื่องสูบน้ำตัวหนึ่งมี Total Head \\(H = 20.0\\text{ m}\\) และสูบน้ำได้อัตราการไหล \\(Q = 2.0\\text{ L/s}\\) กำหนด \\(\\gamma = 9,810\\text{ N/m}^3\\) กำลังงานชลศาสตร์ที่น้ำได้รับ (\\(W_i\\)) มีค่าเท่าใด?",
      choices: [
        "\\(392.4\\text{ Watts}\\)",
        "\\(392,400\\text{ Watts}\\)",
        "\\(40.0\\text{ Watts}\\)",
        "\\(19.62\\text{ Watts}\\)"
      ],
      correct: 0,
      expl: "ต้องแปลง \\(Q\\) เป็น \\(\\text{m}^3/\\text{s}\\) ก่อนเสมอ: \\(Q = 2.0 \\times 10^{-3}\\text{ m}^3/\\text{s}\\) จากสูตร \\(W_i = \\gamma Q H = 9,810 \\times (2.0 \\times 10^{-3}) \\times 20.0 = 392.4\\text{ Watts}\\) (ถ้าลืมแปลงหน่วยจะได้ 392,400 W ซึ่งเป็นช้อยส์หลอกข้อ ข)"
    },
    {
      id: 6,
      lab: "บทที่ 9",
      topic: "การเลือกใช้ปั๊มในงานวิศวกรรมโยธา",
      q: "วิศวกรโยธาต้องการระบายน้ำออกจากพื้นที่ลุ่มต่ำริมแม่น้ำเจ้าพระยาเพื่อป้องกันน้ำท่วม โดยระดับคันกั้นน้ำสูงจากระดับน้ำเพียง 1.5 เมตร แต่ต้องการระบายน้ำปริมาณมากอย่างรวดเร็ว ควรเลือกติดตั้งเครื่องสูบน้ำแบบใด?",
      choices: [
        "ต่อแบบอนุกรม (Series) เพื่ออัดแรงดันน้ำให้พุ่งได้ไกลที่สุด",
        "ต่อแบบขนาน (Parallel) เพื่อเพิ่มปริมาณการสูบน้ำรวมเป็นทวีคูณ (2Q) ที่ระดับเฮดต่ำ",
        "ใช้ปั๊มเดี่ยวตัวเล็กหลายๆ ตัวโดยไม่ต้องเชื่อมท่อกัน",
        "ต่อแบบอนุกรมร่วมกับขนานโดยปิดวาล์วท่อร่วมทั้งหมด"
      ],
      correct: 1,
      expl: "งานสูบระบายน้ำท่วมมีลักษณะเป็น Low Head - High Discharge (ยกน้ำไม่สูงแต่ต้องการปริมาณน้ำมหาศาล) จึงต้องเลือกต่อแบบขนาน (Parallel) เพื่อให้ได้อัตราการไหลรวมสูงสุด"
    },
    {
      id: 7,
      lab: "บทที่ 2",
      topic: "ความลับผิวโค้งทุ่นเสี้ยววงกลม (First Principles)",
      q: "ในการทดลองหาจุดศูนย์กลางของแรงดัน (Center of Pressure) ทำไมแรงดันน้ำที่กระทำต่อผิวด้านโค้งของทุ่น Quadrant จึงไม่ทำให้เกิดโมเมนต์รอบแกนหมุน (Pivot Axis)?",
      choices: [
        "แรงดันที่ผิวโค้งบนและผิวโค้งล่างมีขนาดเท่ากันและหักล้างกันเองหมด",
        "แรงดันทุกจุดตั้งฉากกับผิวโค้งและมีแนวแรงพุ่งผ่านจุดศูนย์กลางความโค้งซึ่งตรงกับแกนหมุนพอดี ทำให้ระยะแขนโมเมนต์ r = 0",
        "ผิวด้านโค้งเคลือบสารลดแรงตึงผิวทำให้น้ำไม่เกาะ",
        "ทุ่นถูกหน่วงด้วยตุ้มถ่วงสมดุลทำให้แรงดันผิวโค้งหายไป"
      ],
      correct: 1,
      expl: "แรงดันของเหลวตั้งฉากกับผิวสัมผัสเสมอ สำหรับผิวโค้งทรงกระบอก แนวแรงตั้งฉากทุกจุดจะพุ่งผ่านจุดศูนย์กลางความโค้ง ซึ่งผู้ออกแบบวางตรงกับแกนหมุน (Pivot Axis) พอดี ทำให้ Moment Arm \\(r = 0\\) ดังนั้น \\(M = F \\times 0 = 0\\) โมเมนต์หมุนจึงเกิดจากแรงดันบนแผ่นระนาบแนวดิ่งเพียงด้านเดียว!"
    },
    {
      id: 8,
      lab: "บทที่ 2",
      topic: "ตำแหน่งจุดศูนย์กลางแรงดัน",
      q: "ตำแหน่งจุดศูนย์กลางของแรงดัน (\\(y_{cp}\\)) บนแผ่นระนาบที่จมน้ำ จะมีตำแหน่งสัมพันธ์กับจุดเซนทรอยด์ (\\(y_c\\)) อย่างไร และเมื่อระดับน้ำท่วมสูงขึ้นมากค่า \\(y_{cp}\\) จะมีแนวโน้มอย่างไร?",
      choices: [
        "\\(y_{cp}\\) อยู่สูงกว่า \\(y_c\\) เสมอ และจะเลื่อนสูงขึ้นเรื่อยๆ",
        "\\(y_{cp}\\) อยู่ต่ำกว่า \\(y_c\\) เสมอ และเมื่อน้ำลึกขึ้นมาก \\(y_{cp}\\) จะเลื่อนเข้าใกล้ \\(y_c\\) มากขึ้น",
        "\\(y_{cp}\\) ทับกับตำแหน่ง \\(y_c\\) พอดีตลอดเวลาทุกระดับน้ำ",
        "\\(y_{cp}\\) จะอยู่ที่ก้นภาชนะเสมอไม่ว่าน้ำจะลึกเท่าใด"
      ],
      correct: 1,
      expl: "จากทฤษฎีแกนขนาน \\(y_{cp} = y_c + \\frac{I_{xx}}{y_c A}\\) เนื่องจาก \\(I_{xx} / (y_c A) > 0\\) เสมอ ดังนั้น \\(y_{cp}\\) จึงต้องอยู่ต่ำกว่า \\(y_c\\) เสมอ และเมื่อน้ำลึกขึ้นเรื่อยๆ (\\(y_c \\to \\infty\\)) พจน์ \\(I_{xx} / (y_c A) \\to 0\\) ส่งผลให้ \\(y_{cp}\\) เลื่อนเข้าใกล้ \\(y_c\\)"
    },
    {
      id: 9,
      lab: "บทที่ 3",
      topic: "แรงกระแทกลำน้ำ (Impact of Jet)",
      q: "เมื่อปล่อยลำน้ำอัตราการไหล \\(Q\\) ความเร็ว \\(v\\) พุ่งชน 'ฉากรูปครึ่งทรงกลม' (Hemispherical Cup 180°) แรงที่ฉากได้รับมีค่าเท่าใดเมื่อเทียบกับ 'ฉากแบนราบ' (Flat Plate 90°)?",
      choices: [
        "เท่ากัน คือ \\(F = \\rho Q v\\)",
        "ฉากครึ่งทรงกลมได้รับแรงเป็น 2 เท่า คือ \\(F = 2\\rho Q v\\) เพราะลำน้ำสะท้อนกลับทิศทาง 180°",
        "ฉากครึ่งทรงกลมได้รับแรงเป็นครึ่งหนึ่งของฉากแบนราบ",
        "ฉากครึ่งทรงกลมไม่ได้รับแรงเลยเพราะน้ำไหลวนออกไป"
      ],
      correct: 1,
      expl: "จากกฎการดล-โมเมนตัม \\(F = \\rho Q (v_{\\text{in}} - v_{\\text{out}})\\) สำหรับแผ่นแบน \\(v_{\\text{out}} = 0\\) ในแนวดิ่ง จะได้ \\(F = \\rho Q v\\) ส่วนถ้วยครึ่งทรงกลมเบนน้ำกลับ 180° ทำให้ \\(v_{\\text{out}} = -v\\) จะได้ \\(F = \\rho Q (v - (-v)) = 2\\rho Q v\\) แรงจึงเป็น 2 เท่าพอดี!"
    },
    {
      id: 10,
      lab: "บทที่ 4",
      topic: "สมการเบอร์นูลี่และท่อเวนจูรี่ (Venturi Paradox)",
      q: "ตามสมการเบอร์นูลี่ เมื่อน้ำไหลผ่านจุดคอคอด (Throat) ของท่อเวนจูรี่ ซึ่งมีพื้นที่หน้าตัดแคบที่สุด ความเร็วและความดันของน้ำจะเปลี่ยนแปลงอย่างไร?",
      choices: [
        "ความเร็วลดลง และความดันเพิ่มขึ้นสูงที่สุด",
        "ความเร็วเพิ่มขึ้นสูงสุด และความดันเพิ่มขึ้นสูงสุดด้วย",
        "ความเร็วเพิ่มขึ้นสูงสุด แต่ความดันจะลดลงต่ำที่สุด",
        "ความเร็วและความดันมีค่าคงที่เท่ากับทางเข้า"
      ],
      correct: 2,
      expl: "ตามสมการความต่อเนื่อง น้ำต้องเร่งความเร็วสูงสุดที่คอคอด ส่งผลให้เฮดความเร็ว (\\(v^2/2g\\)) พุ่งสูงขึ้นมาก และตามกฎอนุรักษ์พลังงานเบอร์นูลี่ เฮดความดัน (\\(P/\\gamma\\)) จึงต้องลดฮวบลงต่ำที่สุดเพื่อรักษาระดับพลังงานรวมให้คงที่"
    },
    {
      id: 11,
      lab: "บทที่ 5",
      topic: "สมการแมนนิ่งและผลของหญ้าเทียม",
      q: "ในการทดลองทางน้ำเปิด หากนำแผ่นหญ้าเทียมมาปูที่ท้องรางน้ำ จะส่งผลต่อสัมประสิทธิ์ความขรุขระ (\\(n\\)) และความลึกน้ำ (\\(y\\)) อย่างไร เมื่ออัตราการไหลคงที่?",
      choices: [
        "ค่า \\(n\\) ลดลง, ความเร็ว \\(V\\) สูงขึ้น, ความลึกน้ำ \\(y\\) ลดลง",
        "ค่า \\(n\\) เพิ่มขึ้น, ความเร็ว \\(V\\) ลดลง, ความลึกน้ำ \\(y\\) เพิ่มสูงขึ้น",
        "ค่า \\(n\\) เพิ่มขึ้น แต่ความลึกน้ำและระดับน้ำไม่เปลี่ยนแปลง",
        "ค่า \\(n\\) เท่าเดิมเพราะหญ้าเทียมทำจากพลาสติกผิวเรียบ"
      ],
      correct: 1,
      expl: "หญ้าเทียมมีความขรุขระสูงกว่าก้นรางสแตนเลสหรืออะคริลิก ทำให้ค่า \\(n\\) เพิ่มขึ้น แรงต้านทานการไหลมากขึ้น ความเร็วเฉลี่ย \\(V\\) จึงลดลง และเพื่อคงอัตราการไหล \\(Q = AV\\) น้ำจึงต้องเอ่อตัวสูงขึ้น (\\(y\\) เพิ่มขึ้น)"
    },
    {
      id: 12,
      lab: "บทที่ 6",
      topic: "ความสัมพันธ์อัตราไหลกับเฮดเหนือน้ำของฝาย",
      q: "อัตราการไหล \\(Q\\) ข้ามฝายสันคมรูปสี่เหลี่ยม และฝายสามเหลี่ยม V-Notch แปรผันตามเฮดเหนือน้ำ \\(H\\) ยกกำลังเท่าใดตามลำดับ?",
      choices: [
        "ฝายสี่เหลี่ยม \\(H^{2.5}\\), ฝายสามเหลี่ยม \\(H^{1.5}\\)",
        "ฝายสี่เหลี่ยม \\(H^{1.5}\\) (หรือ \\(H^{3/2}\\)), ฝายสามเหลี่ยม \\(H^{2.5}\\) (หรือ \\(H^{5/2}\\))",
        "ทั้งสองแบบแปรผันตาม \\(H^{1.0}\\) เส้นตรง",
        "ฝายสี่เหลี่ยม \\(H^{0.5}\\), ฝายสามเหลี่ยม \\(H^{2.0}\\)"
      ],
      correct: 1,
      expl: "จำเลขยกกำลังให้แม่น: ฝายสี่เหลี่ยมพื้นที่น้ำเป็นสี่เหลี่ยม \\(Q \\propto H^{3/2} = H^{1.5}\\) ส่วนฝายสามเหลี่ยมรูปตัว V หน้าตัดขยายตัวตามระดับน้ำ \\(Q \\propto H^{5/2} = H^{2.5}\\) ฝายสามเหลี่ยมจึงวัดน้ำอัตราไหลต่ำได้ละเอียดและแม่นยำกว่ามาก"
    },
    {
      id: 13,
      lab: "บทที่ 7",
      topic: "Darcy-Weisbach และอิทธิพลของขนาดท่อ",
      q: "ตามสมการ Darcy-Weisbach หากอัตราการไหลคงที่ แต่เปลี่ยนขนาดเส้นผ่านศูนย์กลางท่อให้เล็กลงเหลือครึ่งหนึ่ง (\\(D_2 = D_1 / 2\\)) การสูญเสียพลังงานจากแรงเสียดทาน (\\(h_f\\)) จะเพิ่มขึ้นเป็นกี่เท่า?",
      choices: [
        "เพิ่มขึ้น 2 เท่า",
        "เพิ่มขึ้น 4 เท่า",
        "เพิ่มขึ้น 16 เท่า",
        "เพิ่มขึ้น 32 เท่า"
      ],
      correct: 3,
      expl: "จากสูตร \\(h_f = \\frac{8 f L Q^2}{\\pi^2 g D^5}\\) จะเห็นว่า \\(h_f \\propto \\frac{1}{D^5}\\) ดังนั้นเมื่อ \\(D\\) ลดลงเหลือ \\(1/2\\) การสูญเสียจะเพิ่มขึ้นเป็น \\(2^5 = 32\\) เท่า!"
    },
    {
      id: 14,
      lab: "บทที่ 8",
      topic: "ความสัมพันธ์ของสัมประสิทธิ์ไฮดรอลิก 3 ตัว",
      q: "ความสัมพันธ์ระหว่างสัมประสิทธิ์การไหล (\\(C_d\\)), สัมประสิทธิ์ความเร็ว (\\(C_v\\)) และสัมประสิทธิ์การหดตัว (\\(C_c\\)) ของรูเจาะ Orifice คือข้อใด?",
      choices: [
        "\\(C_d = C_v + C_c\\)",
        "\\(C_d = C_v \\times C_c\\)",
        "\\(C_d = C_v / C_c\\)",
        "\\(C_d = \\sqrt{C_v^2 + C_c^2}\\)"
      ],
      correct: 1,
      expl: "เพราะอัตราการไหลจริง \\(Q_{\\text{act}} = A_{\\text{act}} v_{\\text{act}} = (C_c A_0)(C_v v_{\\text{th}}) = (C_c C_v)(A_0 v_{\\text{th}}) = C_d Q_{\\text{th}}\\) ดังนั้น \\(C_d = C_v \\times C_c\\) เสมอ!"
    },
    {
      id: 15,
      lab: "บทที่ 10 และ 11",
      topic: "สภาวะการไหลวิกฤตและเวนจูรี่ฟลูม",
      q: "การไหลของน้ำที่พุ่งลอดผ่านใต้บานประตูระบายน้ำ (Sluice Gate) ด้านท้ายน้ำ (Downstream) จะมีสภาวะการไหลแบบใด และเวนจูรี่ฟลูมมีข้อดีเหนือฝายอย่างไร?",
      choices: [
        "ท้ายประตูน้ำเป็น Subcritical Flow (\\(Fr < 1\\)) และเวนจูรี่ฟลูมสร้างง่ายกว่าฝาย",
        "ท้ายประตูน้ำเป็น Supercritical Flow (\\(Fr > 1\\)) และเวนจูรี่ฟลูมไม่กักตะกอนดินทรายพร้อมสูญเสียเฮดน้อยกว่าฝาย",
        "ท้ายประตูน้ำเป็น Critical Flow (\\(Fr = 1\\)) ตลอดเวลา และเวนจูรี่ฟลูมวัดน้ำได้เฉพาะคลองท่อปิด",
        "ท้ายประตูน้ำไม่มีสภาวะการไหลแน่นอน และเวนจูรี่ฟลูมไม่สามารถใช้วัดอัตราไหลได้"
      ],
      correct: 1,
      expl: "น้ำที่พุ่งลอดใต้ประตูน้ำจะตื้นมากและมีความเร็วสูงจัด ทำให้ \\(Fr = \\frac{V}{\\sqrt{gy}} > 1\\) (Supercritical Flow) ส่วนเวนจูรี่ฟลูมไม่มีแผ่นสันฝายขวางกั้นท้องน้ำ ตะกอนดินทรายจึงไหลผ่านไปได้โดยไม่ทับถมตกค้าง และมีการสูญเสียพลังงาน (Head Loss) ต่ำกว่าฝายมาก"
    }
  ];

  var answered = {};
  var score = 0;

  function renderQuiz() {
    var container = document.getElementById("quiz-list");
    if (!container) return;

    var html = quizData.map(function (item, idx) {
      return (
        '<div class="quiz-card" id="qcard-' + item.id + '">' +
          '<div class="quiz-header">' +
            '<span class="quiz-badge">ข้อที่ ' + (idx + 1) + ' · ' + item.lab + ' · ' + item.topic + '</span>' +
            '<span class="quiz-pts">1 คะแนน</span>' +
          '</div>' +
          '<p class="quiz-q">' + item.q + '</p>' +
          '<div class="quiz-opts" id="qopts-' + item.id + '">' +
            item.choices.map(function (choice, cIdx) {
              var letter = ["ก", "ข", "ค", "ง"][cIdx];
              return (
                '<button type="button" class="quiz-opt" onclick="window.answerQuiz(' + item.id + ', ' + cIdx + ')">' +
                  '<span class="opt-let">' + letter + '.</span>' +
                  '<span class="opt-txt">' + choice + '</span>' +
                '</button>'
              );
            }).join("") +
          '</div>' +
          '<div class="quiz-expl" id="qexpl-' + item.id + '"></div>' +
        '</div>'
      );
    }).join("");

    container.innerHTML = html;

    // Render KaTeX for quiz container
    if (typeof renderMathInElement === "function") {
      renderMathInElement(container, {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "\\(", right: "\\)", display: false },
          { left: "\\[", right: "\\]", display: true }
        ],
        throwOnError: false,
        trust: true
      });
    }
  }

  window.answerQuiz = function (qId, choiceIdx) {
    if (answered[qId] !== undefined) return;
    answered[qId] = choiceIdx;

    var item = quizData.filter(function (x) { return x.id === qId; })[0];
    if (!item) return;

    var card = document.getElementById("qcard-" + qId);
    var opts = card ? card.querySelectorAll(".quiz-opt") : [];
    var expl = document.getElementById("qexpl-" + qId);

    // Disable all options
    for (var i = 0; i < opts.length; i++) {
      opts[i].disabled = true;
      if (i === item.correct) {
        opts[i].classList.add("correct");
      }
      if (i === choiceIdx && choiceIdx !== item.correct) {
        opts[i].classList.add("wrong");
      }
    }

    var isCorrect = (choiceIdx === item.correct);
    if (isCorrect) {
      score++;
      expl.className = "quiz-expl pass";
      expl.innerHTML = "<strong>✓ ถูกต้อง! (+1 คะแนน)</strong><br>" + item.expl;
    } else {
      var correctLetter = ["ก", "ข", "ค", "ง"][item.correct];
      expl.className = "quiz-expl fail";
      expl.innerHTML = "<strong>✗ ยังไม่ถูกต้อง!</strong> คำตอบที่ถูกต้องคือข้อ <strong>" + correctLetter + ".</strong><br>" + item.expl;
    }

    var scoreEl = document.getElementById("quiz-score-val");
    if (scoreEl) scoreEl.textContent = score;

    // Render math in explanation
    if (typeof renderMathInElement === "function") {
      renderMathInElement(expl, {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "\\(", right: "\\)", display: false },
          { left: "\\[", right: "\\]", display: true }
        ],
        throwOnError: false,
        trust: true
      });
    }
  };

  window.resetQuiz = function () {
    answered = {};
    score = 0;
    var scoreEl = document.getElementById("quiz-score-val");
    if (scoreEl) scoreEl.textContent = "0";
    renderQuiz();
  };

  // Switch between Interactive Quiz and Step-by-Step Practice
  window.switchExamTab = function (tab) {
    var quizSec = document.getElementById("exam-tab-quiz");
    var stepSec = document.getElementById("exam-tab-step");
    var btnQuiz = document.getElementById("btn-tab-quiz");
    var btnStep = document.getElementById("btn-tab-step");

    if (tab === "quiz") {
      if (quizSec) quizSec.style.display = "block";
      if (stepSec) stepSec.style.display = "none";
      if (btnQuiz) { btnQuiz.classList.add("active"); }
      if (btnStep) { btnStep.classList.remove("active"); }
    } else {
      if (quizSec) quizSec.style.display = "none";
      if (stepSec) stepSec.style.display = "block";
      if (btnQuiz) { btnQuiz.classList.remove("active"); }
      if (btnStep) { btnStep.classList.add("active"); }
    }
  };

  // Auto-init when #exam section is shown
  function checkInit() {
    var sec = document.getElementById("exam");
    if (sec && !sec.getAttribute("data-quiz-init")) {
      renderQuiz();
      sec.setAttribute("data-quiz-init", "1");
    }
  }

  window.addEventListener("hashchange", function () {
    if (location.hash === "#exam") {
      setTimeout(checkInit, 50);
    }
  });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      setTimeout(checkInit, 100);
    });
  } else {
    setTimeout(checkInit, 100);
  }
})();
