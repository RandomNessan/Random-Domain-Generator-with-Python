import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

# 协议 -> 前缀 映射
PROTOCOL_PREFIX_MAP = {
    "hysteria1": "h1",
    "hysteria2": "h2",
    "shadowsocks": "ss",
    "vmess": "vm",
    "vless": "vl",
    "tuic": "tc",
    "anytls": "at",
    "trojan": "tj",
    "v2node": "vn",
}

# 国家列表（ISO 3166-1 alpha-2）
COUNTRIES = [
    ("Afghanistan", "AF"),
    ("Åland Islands", "AX"),
    ("Albania", "AL"),
    ("Algeria", "DZ"),
    ("American Samoa", "AS"),
    ("Andorra", "AD"),
    ("Angola", "AO"),
    ("Anguilla", "AI"),
    ("Antarctica", "AQ"),
    ("Antigua and Barbuda", "AG"),
    ("Argentina", "AR"),
    ("Armenia", "AM"),
    ("Aruba", "AW"),
    ("Australia", "AU"),
    ("Austria", "AT"),
    ("Azerbaijan", "AZ"),
    ("Bahamas", "BS"),
    ("Bahrain", "BH"),
    ("Bangladesh", "BD"),
    ("Barbados", "BB"),
    ("Belarus", "BY"),
    ("Belgium", "BE"),
    ("Belize", "BZ"),
    ("Benin", "BJ"),
    ("Bermuda", "BM"),
    ("Bhutan", "BT"),
    ("Bolivia", "BO"),
    ("Bonaire, Sint Eustatius and Saba", "BQ"),
    ("Bosnia and Herzegovina", "BA"),
    ("Botswana", "BW"),
    ("Bouvet Island", "BV"),
    ("Brazil", "BR"),
    ("British Indian Ocean Territory", "IO"),
    ("Brunei Darussalam", "BN"),
    ("Bulgaria", "BG"),
    ("Burkina Faso", "BF"),
    ("Burundi", "BI"),
    ("Cabo Verde", "CV"),
    ("Cambodia", "KH"),
    ("Cameroon", "CM"),
    ("Canada", "CA"),
    ("Cayman Islands", "KY"),
    ("Central African Republic", "CF"),
    ("Chad", "TD"),
    ("Chile", "CL"),
    ("China", "CN"),
    ("Christmas Island", "CX"),
    ("Cocos (Keeling) Islands", "CC"),
    ("Colombia", "CO"),
    ("Comoros", "KM"),
    ("Congo", "CG"),
    ("Congo (Democratic Republic)", "CD"),
    ("Cook Islands", "CK"),
    ("Costa Rica", "CR"),
    ("Croatia", "HR"),
    ("Cuba", "CU"),
    ("Curaçao", "CW"),
    ("Cyprus", "CY"),
    ("Czechia", "CZ"),
    ("Côte d'Ivoire", "CI"),
    ("Denmark", "DK"),
    ("Djibouti", "DJ"),
    ("Dominica", "DM"),
    ("Dominican Republic", "DO"),
    ("Ecuador", "EC"),
    ("Egypt", "EG"),
    ("El Salvador", "SV"),
    ("Equatorial Guinea", "GQ"),
    ("Eritrea", "ER"),
    ("Estonia", "EE"),
    ("Eswatini", "SZ"),
    ("Ethiopia", "ET"),
    ("Falkland Islands", "FK"),
    ("Faroe Islands", "FO"),
    ("Fiji", "FJ"),
    ("Finland", "FI"),
    ("France", "FR"),
    ("French Guiana", "GF"),
    ("French Polynesia", "PF"),
    ("French Southern Territories", "TF"),
    ("Gabon", "GA"),
    ("Gambia", "GM"),
    ("Georgia", "GE"),
    ("Germany", "DE"),
    ("Ghana", "GH"),
    ("Gibraltar", "GI"),
    ("Greece", "GR"),
    ("Greenland", "GL"),
    ("Grenada", "GD"),
    ("Guadeloupe", "GP"),
    ("Guam", "GU"),
    ("Guatemala", "GT"),
    ("Guernsey", "GG"),
    ("Guinea", "GN"),
    ("Guinea-Bissau", "GW"),
    ("Guyana", "GY"),
    ("Haiti", "HT"),
    ("Heard Island and McDonald Islands", "HM"),
    ("Holy See", "VA"),
    ("Honduras", "HN"),
    ("Hong Kong", "HK"),
    ("Hungary", "HU"),
    ("Iceland", "IS"),
    ("India", "IN"),
    ("Indonesia", "ID"),
    ("Iran", "IR"),
    ("Iraq", "IQ"),
    ("Ireland", "IE"),
    ("Isle of Man", "IM"),
    ("Israel", "IL"),
    ("Italy", "IT"),
    ("Jamaica", "JM"),
    ("Japan", "JP"),
    ("Jersey", "JE"),
    ("Jordan", "JO"),
    ("Kazakhstan", "KZ"),
    ("Kenya", "KE"),
    ("Kiribati", "KI"),
    ("Korea (North)", "KP"),
    ("Korea (South)", "KR"),
    ("Kuwait", "KW"),
    ("Kyrgyzstan", "KG"),
    ("Lao People's Democratic Republic", "LA"),
    ("Latvia", "LV"),
    ("Lebanon", "LB"),
    ("Lesotho", "LS"),
    ("Liberia", "LR"),
    ("Libya", "LY"),
    ("Liechtenstein", "LI"),
    ("Lithuania", "LT"),
    ("Luxembourg", "LU"),
    ("Macao", "MO"),
    ("Madagascar", "MG"),
    ("Malawi", "MW"),
    ("Malaysia", "MY"),
    ("Maldives", "MV"),
    ("Mali", "ML"),
    ("Malta", "MT"),
    ("Marshall Islands", "MH"),
    ("Martinique", "MQ"),
    ("Mauritania", "MR"),
    ("Mauritius", "MU"),
    ("Mayotte", "YT"),
    ("Mexico", "MX"),
    ("Micronesia", "FM"),
    ("Moldova", "MD"),
    ("Monaco", "MC"),
    ("Mongolia", "MN"),
    ("Montenegro", "ME"),
    ("Montserrat", "MS"),
    ("Morocco", "MA"),
    ("Mozambique", "MZ"),
    ("Myanmar", "MM"),
    ("Namibia", "NA"),
    ("Nauru", "NR"),
    ("Nepal", "NP"),
    ("Netherlands", "NL"),
    ("New Caledonia", "NC"),
    ("New Zealand", "NZ"),
    ("Nicaragua", "NI"),
    ("Niger", "NE"),
    ("Nigeria", "NG"),
    ("Niue", "NU"),
    ("Norfolk Island", "NF"),
    ("North Macedonia", "MK"),
    ("Northern Mariana Islands", "MP"),
    ("Norway", "NO"),
    ("Oman", "OM"),
    ("Pakistan", "PK"),
    ("Palau", "PW"),
    ("Palestine", "PS"),
    ("Panama", "PA"),
    ("Papua New Guinea", "PG"),
    ("Paraguay", "PY"),
    ("Peru", "PE"),
    ("Philippines", "PH"),
    ("Pitcairn", "PN"),
    ("Poland", "PL"),
    ("Portugal", "PT"),
    ("Puerto Rico", "PR"),
    ("Qatar", "QA"),
    ("Réunion", "RE"),
    ("Romania", "RO"),
    ("Russian Federation", "RU"),
    ("Rwanda", "RW"),
    ("Saint Barthélemy", "BL"),
    ("Saint Helena", "SH"),
    ("Saint Kitts and Nevis", "KN"),
    ("Saint Lucia", "LC"),
    ("Saint Martin (French)", "MF"),
    ("Saint Pierre and Miquelon", "PM"),
    ("Saint Vincent and the Grenadines", "VC"),
    ("Samoa", "WS"),
    ("San Marino", "SM"),
    ("Sao Tome and Principe", "ST"),
    ("Saudi Arabia", "SA"),
    ("Senegal", "SN"),
    ("Serbia", "RS"),
    ("Seychelles", "SC"),
    ("Sierra Leone", "SL"),
    ("Singapore", "SG"),
    ("Sint Maarten (Dutch)", "SX"),
    ("Slovakia", "SK"),
    ("Slovenia", "SI"),
    ("Solomon Islands", "SB"),
    ("Somalia", "SO"),
    ("South Africa", "ZA"),
    ("South Georgia and the South Sandwich Islands", "GS"),
    ("South Sudan", "SS"),
    ("Spain", "ES"),
    ("Sri Lanka", "LK"),
    ("Sudan", "SD"),
    ("Suriname", "SR"),
    ("Svalbard and Jan Mayen", "SJ"),
    ("Sweden", "SE"),
    ("Switzerland", "CH"),
    ("Syrian Arab Republic", "SY"),
    ("Taiwan (Province of China)", "TW"),
    ("Tajikistan", "TJ"),
    ("Tanzania", "TZ"),
    ("Thailand", "TH"),
    ("Timor-Leste", "TL"),
    ("Togo", "TG"),
    ("Tokelau", "TK"),
    ("Tonga", "TO"),
    ("Trinidad and Tobago", "TT"),
    ("Tunisia", "TN"),
    ("Turkey", "TR"),
    ("Turkmenistan", "TM"),
    ("Turks and Caicos Islands", "TC"),
    ("Tuvalu", "TV"),
    ("Uganda", "UG"),
    ("Ukraine", "UA"),
    ("United Arab Emirates", "AE"),
    ("United Kingdom", "GB"),
    ("United States", "US"),
    ("United States Minor Outlying Islands", "UM"),
    ("Uruguay", "UY"),
    ("Uzbekistan", "UZ"),
    ("Vanuatu", "VU"),
    ("Venezuela", "VE"),
    ("Viet Nam", "VN"),
    ("Virgin Islands (British)", "VG"),
    ("Virgin Islands (U.S.)", "VI"),
    ("Wallis and Futuna", "WF"),
    ("Western Sahara", "EH"),
    ("Yemen", "YE"),
    ("Zambia", "ZM"),
    ("Zimbabwe", "ZW"),
]


def random_string(length: int) -> str:
    """生成指定长度的字母数字混合字符串"""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def generate_domains(protocol: str,
                     country_code: str,
                     main_domain: str,
                     obf_len: int,
                     count: int,
                     use_dash: bool) -> list:
    """组合生成随机域名列表"""
    result = []
    prefix = PROTOCOL_PREFIX_MAP.get(protocol)
    if not prefix:
        raise ValueError("未知协议: " + protocol)

    # 主域名简单清理一下前后空格和前导点
    main_domain = main_domain.strip()
    if main_domain.startswith("."):
        main_domain = main_domain[1:]

    if not main_domain:
        raise ValueError("主域名不能为空")

    for _ in range(count):
        obf = random_string(obf_len)
        if use_dash:
            # 形如: h2-X8fK29qaL1Dp-US.airando.icu
            full_host = f"{prefix}-{obf}-{country_code}.{main_domain}"
        else:
            # 形如: h2X8fK29qaL1DpUS.airando.icu
            full_host = f"{prefix}{obf}{country_code}.{main_domain}"
        result.append(full_host)

    return result

class DomainGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("随机域名生成器 · Random Domain Generator")
        self.geometry("700x520")
        self.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # ===== 上半部分：输入区域 =====
        frame = ttk.LabelFrame(self, text="参数设置")
        frame.pack(fill=tk.X, padx=10, pady=10)

        # 协议
        ttk.Label(frame, text="协议 (Protocol):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.protocol_var = tk.StringVar()
        self.protocol_combo = ttk.Combobox(
            frame,
            textvariable=self.protocol_var,
            state="readonly",
            values=list(PROTOCOL_PREFIX_MAP.keys())
        )
        self.protocol_combo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.protocol_combo.current(1)  # 默认选 hysteria2

        # 国家
        ttk.Label(frame, text="地区/国家 (Country):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.country_var = tk.StringVar()
        country_display_list = [f"{name} ({code})" for name, code in COUNTRIES]
        self.country_combo = ttk.Combobox(
            frame,
            textvariable=self.country_var,
            state="readonly",
            values=country_display_list
        )
        self.country_combo.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        if country_display_list:
            self.country_combo.current(0)

        # 主域名
        ttk.Label(frame, text="主域名 (Main domain):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.domain_var = tk.StringVar(value="xxx.com")
        self.domain_entry = ttk.Entry(frame, textvariable=self.domain_var, width=30)
        self.domain_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # 混淆位数
        ttk.Label(frame, text="混淆位数 (5-25):").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.length_var = tk.IntVar(value=12)
        self.length_spin = ttk.Spinbox(
            frame,
            from_=5,
            to=25,
            textvariable=self.length_var,
            width=5
        )
        self.length_spin.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # 生成个数
        ttk.Label(frame, text="生成数量 (Count):").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.count_var = tk.IntVar(value=10)
        self.count_spin = ttk.Spinbox(
            frame,
            from_=1,
            to=1000,
            textvariable=self.count_var,
            width=5
        )
        self.count_spin.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        # 是否使用 "-"
        self.use_dash_var = tk.BooleanVar(value=True)
        self.use_dash_check = ttk.Checkbutton(
            frame,
            text="参数之间使用 '-' 分隔 (例如: h2-xxxx-US.domain)",
            variable=self.use_dash_var
        )
        self.use_dash_check.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        # 按钮区域
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        self.generate_btn = ttk.Button(btn_frame, text="生成随机域名", command=self.on_generate)
        self.generate_btn.pack(side=tk.LEFT, padx=5)

        self.copy_btn = ttk.Button(btn_frame, text="复制全部到剪贴板", command=self.copy_to_clipboard)
        self.copy_btn.pack(side=tk.LEFT, padx=5)

        # 按钮：生成域名解析模板
        self.dns_template_btn = ttk.Button(
            btn_frame,
            text="生成域名解析模板",
            command=self.open_dns_template_window
        )
        self.dns_template_btn.pack(side=tk.LEFT, padx=5)

        # 输出区域
        output_frame = ttk.LabelFrame(self, text="生成结果（随机域名）")
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        self.output_text = tk.Text(output_frame, wrap="none")
        self.output_text.pack(fill=tk.BOTH, expand=True)

        # 垂直滚动条
        y_scroll = ttk.Scrollbar(self.output_text, orient="vertical", command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=y_scroll.set)
        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    def on_generate(self):
        try:
            protocol = self.protocol_var.get()
            if not protocol:
                messagebox.showwarning("警告", "请选择协议")
                return

            country_display = self.country_var.get()
            if not country_display or "(" not in country_display or ")" not in country_display:
                messagebox.showwarning("警告", "请选择地区/国家")
                return

            # 从 "United States (US)" 中提取 "US"
            country_code = country_display.split("(")[-1].split(")")[0].strip().upper()

            main_domain = self.domain_var.get()
            if not main_domain.strip():
                messagebox.showwarning("警告", "主域名不能为空")
                return

            obf_len = int(self.length_var.get())
            if obf_len < 5 or obf_len > 25:
                messagebox.showwarning("警告", "混淆位数必须在 5 到 25 之间")
                return

            count = int(self.count_var.get())
            if count <= 0:
                messagebox.showwarning("警告", "生成数量必须大于 0")
                return

            use_dash = self.use_dash_var.get()

            domains = generate_domains(
                protocol=protocol,
                country_code=country_code,
                main_domain=main_domain,
                obf_len=obf_len,
                count=count,
                use_dash=use_dash
            )

            self.output_text.delete("1.0", tk.END)
            for d in domains:
                self.output_text.insert(tk.END, d + "\n")

        except Exception as e:
            messagebox.showerror("错误", f"生成失败：\n{e}")

    def copy_to_clipboard(self):
        text = self.output_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showinfo("提示", "没有内容可以复制")
            return
        self.clipboard_clear()
        self.clipboard_append(text)
        messagebox.showinfo("提示", "已复制到剪贴板")

    # ========= 新增：域名解析模板窗口 =========
    def open_dns_template_window(self):
        win = tk.Toplevel(self)
        win.title("生成域名解析模板 · DNS Record Generator")
        win.geometry("700x480")
        win.resizable(False, False)

        # 输入区域
        input_frame = ttk.LabelFrame(win, text="解析参数")
        input_frame.pack(fill=tk.X, padx=10, pady=10)

        # 域名（只能填一个）
        ttk.Label(input_frame, text="域名（Host）:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        domain_var = tk.StringVar()
        domain_entry = ttk.Entry(input_frame, textvariable=domain_var, width=40)
        domain_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        # 如果主界面有已经生成的域名，可以手动复制粘贴到这里

        # 记录类型
        ttk.Label(input_frame, text="记录类型（Type）:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        record_type_var = tk.StringVar()
        record_type_combo = ttk.Combobox(
            input_frame,
            textvariable=record_type_var,
            state="readonly",
            values=["A", "AAAA", "CNAME", "TXT", "MX", "NS", "SRV"]
        )
        record_type_combo.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        record_type_combo.current(0)  # 默认 A 记录

        # IP 地址（或目标，多行）
        ttk.Label(input_frame, text="IP / 目标（多行或用逗号分隔）:").grid(
            row=2, column=0, padx=5, pady=5, sticky="ne"
        )
        ip_text = tk.Text(input_frame, height=5, width=40)
        ip_text.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # 备注
        ttk.Label(input_frame, text="备注（Comment，可选）:").grid(
            row=3, column=0, padx=5, pady=5, sticky="e"
        )
        comment_var = tk.StringVar(
            value="例如: cf_tags=cf-proxied:false"
        )
        comment_entry = ttk.Entry(input_frame, textvariable=comment_var, width=40)
        comment_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # 按钮区域
        btn_frame = ttk.Frame(win)
        btn_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        def generate_dns_records():
            host = domain_var.get().strip()
            if not host:
                messagebox.showwarning("警告", "请填写域名（Host）")
                return

            rtype = record_type_var.get().strip().upper()
            if not rtype:
                messagebox.showwarning("警告", "请选择记录类型")
                return

            # 处理 IP / 目标，多行或逗号分隔
            raw_ips = ip_text.get("1.0", tk.END)
            # 支持逗号和换行分隔
            raw_ips = raw_ips.replace(",", "\n")
            items = [x.strip() for x in raw_ips.splitlines() if x.strip()]
            if not items:
                messagebox.showwarning("警告", "请至少填写一个 IP / 目标")
                return

            comment = comment_var.get().strip()

            # 域名统一加一个尾部的点
            if not host.endswith("."):
                host_out = host + "."
            else:
                host_out = host

            lines = []
            for item in items:
                if comment:
                    line = f"{host_out}\t1\tIN\t{rtype}\t{item} ; {comment}"
                else:
                    line = f"{host_out}\t1\tIN\t{rtype}\t{item}"
                lines.append(line)

            dns_output_text.delete("1.0", tk.END)
            dns_output_text.insert(tk.END, "\n".join(lines))

        def copy_dns_to_clipboard():
            text = dns_output_text.get("1.0", tk.END).strip()
            if not text:
                messagebox.showinfo("提示", "没有内容可以复制")
                return
            win.clipboard_clear()
            win.clipboard_append(text)
            messagebox.showinfo("提示", "解析记录已复制到剪贴板")

        generate_btn = ttk.Button(btn_frame, text="生成解析记录", command=generate_dns_records)
        generate_btn.pack(side=tk.LEFT, padx=5)

        copy_btn = ttk.Button(btn_frame, text="复制解析到剪贴板", command=copy_dns_to_clipboard)
        copy_btn.pack(side=tk.LEFT, padx=5)

        # 输出区域
        output_frame = ttk.LabelFrame(win, text="生成的解析记录")
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        dns_output_text = tk.Text(output_frame, wrap="none")
        dns_output_text.pack(fill=tk.BOTH, expand=True)

        y_scroll = ttk.Scrollbar(dns_output_text, orient="vertical", command=dns_output_text.yview)
        dns_output_text.configure(yscrollcommand=y_scroll.set)
        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)


if __name__ == "__main__":
    app = DomainGeneratorApp()
    app.mainloop()
