from typing import Any
from typing import Final

from collections.abc import Callable
from collections.abc import Sequence

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject

A: Final[int]
AE: Final[int]
Aacute: Final[int]
Abelowdot: Final[int]
Abreve: Final[int]
Abreveacute: Final[int]
Abrevebelowdot: Final[int]
Abrevegrave: Final[int]
Abrevehook: Final[int]
Abrevetilde: Final[int]
AccessX_Enable: Final[int]
AccessX_Feedback_Enable: Final[int]
Acircumflex: Final[int]
Acircumflexacute: Final[int]
Acircumflexbelowdot: Final[int]
Acircumflexgrave: Final[int]
Acircumflexhook: Final[int]
Acircumflextilde: Final[int]
Adiaeresis: Final[int]
Agrave: Final[int]
Ahook: Final[int]
Alt_L: Final[int]
Alt_R: Final[int]
Amacron: Final[int]
Aogonek: Final[int]
Arabic_0: Final[int]
Arabic_1: Final[int]
Arabic_2: Final[int]
Arabic_3: Final[int]
Arabic_4: Final[int]
Arabic_5: Final[int]
Arabic_6: Final[int]
Arabic_7: Final[int]
Arabic_8: Final[int]
Arabic_9: Final[int]
Arabic_ain: Final[int]
Arabic_alef: Final[int]
Arabic_alefmaksura: Final[int]
Arabic_beh: Final[int]
Arabic_comma: Final[int]
Arabic_dad: Final[int]
Arabic_dal: Final[int]
Arabic_damma: Final[int]
Arabic_dammatan: Final[int]
Arabic_ddal: Final[int]
Arabic_farsi_yeh: Final[int]
Arabic_fatha: Final[int]
Arabic_fathatan: Final[int]
Arabic_feh: Final[int]
Arabic_fullstop: Final[int]
Arabic_gaf: Final[int]
Arabic_ghain: Final[int]
Arabic_ha: Final[int]
Arabic_hah: Final[int]
Arabic_hamza: Final[int]
Arabic_hamza_above: Final[int]
Arabic_hamza_below: Final[int]
Arabic_hamzaonalef: Final[int]
Arabic_hamzaonwaw: Final[int]
Arabic_hamzaonyeh: Final[int]
Arabic_hamzaunderalef: Final[int]
Arabic_heh: Final[int]
Arabic_heh_doachashmee: Final[int]
Arabic_heh_goal: Final[int]
Arabic_jeem: Final[int]
Arabic_jeh: Final[int]
Arabic_kaf: Final[int]
Arabic_kasra: Final[int]
Arabic_kasratan: Final[int]
Arabic_keheh: Final[int]
Arabic_khah: Final[int]
Arabic_lam: Final[int]
Arabic_madda_above: Final[int]
Arabic_maddaonalef: Final[int]
Arabic_meem: Final[int]
Arabic_noon: Final[int]
Arabic_noon_ghunna: Final[int]
Arabic_peh: Final[int]
Arabic_percent: Final[int]
Arabic_qaf: Final[int]
Arabic_question_mark: Final[int]
Arabic_ra: Final[int]
Arabic_rreh: Final[int]
Arabic_sad: Final[int]
Arabic_seen: Final[int]
Arabic_semicolon: Final[int]
Arabic_shadda: Final[int]
Arabic_sheen: Final[int]
Arabic_sukun: Final[int]
Arabic_superscript_alef: Final[int]
Arabic_switch: Final[int]
Arabic_tah: Final[int]
Arabic_tatweel: Final[int]
Arabic_tcheh: Final[int]
Arabic_teh: Final[int]
Arabic_tehmarbuta: Final[int]
Arabic_thal: Final[int]
Arabic_theh: Final[int]
Arabic_tteh: Final[int]
Arabic_veh: Final[int]
Arabic_waw: Final[int]
Arabic_yeh: Final[int]
Arabic_yeh_baree: Final[int]
Arabic_zah: Final[int]
Arabic_zain: Final[int]
Aring: Final[int]
Armenian_AT: Final[int]
Armenian_AYB: Final[int]
Armenian_BEN: Final[int]
Armenian_CHA: Final[int]
Armenian_DA: Final[int]
Armenian_DZA: Final[int]
Armenian_E: Final[int]
Armenian_FE: Final[int]
Armenian_GHAT: Final[int]
Armenian_GIM: Final[int]
Armenian_HI: Final[int]
Armenian_HO: Final[int]
Armenian_INI: Final[int]
Armenian_JE: Final[int]
Armenian_KE: Final[int]
Armenian_KEN: Final[int]
Armenian_KHE: Final[int]
Armenian_LYUN: Final[int]
Armenian_MEN: Final[int]
Armenian_NU: Final[int]
Armenian_O: Final[int]
Armenian_PE: Final[int]
Armenian_PYUR: Final[int]
Armenian_RA: Final[int]
Armenian_RE: Final[int]
Armenian_SE: Final[int]
Armenian_SHA: Final[int]
Armenian_TCHE: Final[int]
Armenian_TO: Final[int]
Armenian_TSA: Final[int]
Armenian_TSO: Final[int]
Armenian_TYUN: Final[int]
Armenian_VEV: Final[int]
Armenian_VO: Final[int]
Armenian_VYUN: Final[int]
Armenian_YECH: Final[int]
Armenian_ZA: Final[int]
Armenian_ZHE: Final[int]
Armenian_accent: Final[int]
Armenian_amanak: Final[int]
Armenian_apostrophe: Final[int]
Armenian_at: Final[int]
Armenian_ayb: Final[int]
Armenian_ben: Final[int]
Armenian_but: Final[int]
Armenian_cha: Final[int]
Armenian_da: Final[int]
Armenian_dza: Final[int]
Armenian_e: Final[int]
Armenian_exclam: Final[int]
Armenian_fe: Final[int]
Armenian_full_stop: Final[int]
Armenian_ghat: Final[int]
Armenian_gim: Final[int]
Armenian_hi: Final[int]
Armenian_ho: Final[int]
Armenian_hyphen: Final[int]
Armenian_ini: Final[int]
Armenian_je: Final[int]
Armenian_ke: Final[int]
Armenian_ken: Final[int]
Armenian_khe: Final[int]
Armenian_ligature_ew: Final[int]
Armenian_lyun: Final[int]
Armenian_men: Final[int]
Armenian_nu: Final[int]
Armenian_o: Final[int]
Armenian_paruyk: Final[int]
Armenian_pe: Final[int]
Armenian_pyur: Final[int]
Armenian_question: Final[int]
Armenian_ra: Final[int]
Armenian_re: Final[int]
Armenian_se: Final[int]
Armenian_separation_mark: Final[int]
Armenian_sha: Final[int]
Armenian_shesht: Final[int]
Armenian_tche: Final[int]
Armenian_to: Final[int]
Armenian_tsa: Final[int]
Armenian_tso: Final[int]
Armenian_tyun: Final[int]
Armenian_verjaket: Final[int]
Armenian_vev: Final[int]
Armenian_vo: Final[int]
Armenian_vyun: Final[int]
Armenian_yech: Final[int]
Armenian_yentamna: Final[int]
Armenian_za: Final[int]
Armenian_zhe: Final[int]
Atilde: Final[int]
AudibleBell_Enable: Final[int]
B: Final[int]
Babovedot: Final[int]
BackSpace: Final[int]
Begin: Final[int]
BounceKeys_Enable: Final[int]
Break: Final[int]
Byelorussian_SHORTU: Final[int]
Byelorussian_shortu: Final[int]
C: Final[int]
Cabovedot: Final[int]
Cacute: Final[int]
Cancel: Final[int]
Caps_Lock: Final[int]
Ccaron: Final[int]
Ccedilla: Final[int]
Ccircumflex: Final[int]
Clear: Final[int]
Codeinput: Final[int]
ColonSign: Final[int]
Control_L: Final[int]
Control_R: Final[int]
CruzeiroSign: Final[int]
Cyrillic_A: Final[int]
Cyrillic_BE: Final[int]
Cyrillic_CHE: Final[int]
Cyrillic_CHE_descender: Final[int]
Cyrillic_CHE_vertstroke: Final[int]
Cyrillic_DE: Final[int]
Cyrillic_DZHE: Final[int]
Cyrillic_E: Final[int]
Cyrillic_EF: Final[int]
Cyrillic_EL: Final[int]
Cyrillic_EM: Final[int]
Cyrillic_EN: Final[int]
Cyrillic_EN_descender: Final[int]
Cyrillic_ER: Final[int]
Cyrillic_ES: Final[int]
Cyrillic_GHE: Final[int]
Cyrillic_GHE_bar: Final[int]
Cyrillic_HA: Final[int]
Cyrillic_HARDSIGN: Final[int]
Cyrillic_HA_descender: Final[int]
Cyrillic_I: Final[int]
Cyrillic_IE: Final[int]
Cyrillic_IO: Final[int]
Cyrillic_I_macron: Final[int]
Cyrillic_JE: Final[int]
Cyrillic_KA: Final[int]
Cyrillic_KA_descender: Final[int]
Cyrillic_KA_vertstroke: Final[int]
Cyrillic_LJE: Final[int]
Cyrillic_NJE: Final[int]
Cyrillic_O: Final[int]
Cyrillic_O_bar: Final[int]
Cyrillic_PE: Final[int]
Cyrillic_SCHWA: Final[int]
Cyrillic_SHA: Final[int]
Cyrillic_SHCHA: Final[int]
Cyrillic_SHHA: Final[int]
Cyrillic_SHORTI: Final[int]
Cyrillic_SOFTSIGN: Final[int]
Cyrillic_TE: Final[int]
Cyrillic_TSE: Final[int]
Cyrillic_U: Final[int]
Cyrillic_U_macron: Final[int]
Cyrillic_U_straight: Final[int]
Cyrillic_U_straight_bar: Final[int]
Cyrillic_VE: Final[int]
Cyrillic_YA: Final[int]
Cyrillic_YERU: Final[int]
Cyrillic_YU: Final[int]
Cyrillic_ZE: Final[int]
Cyrillic_ZHE: Final[int]
Cyrillic_ZHE_descender: Final[int]
Cyrillic_a: Final[int]
Cyrillic_be: Final[int]
Cyrillic_che: Final[int]
Cyrillic_che_descender: Final[int]
Cyrillic_che_vertstroke: Final[int]
Cyrillic_de: Final[int]
Cyrillic_dzhe: Final[int]
Cyrillic_e: Final[int]
Cyrillic_ef: Final[int]
Cyrillic_el: Final[int]
Cyrillic_em: Final[int]
Cyrillic_en: Final[int]
Cyrillic_en_descender: Final[int]
Cyrillic_er: Final[int]
Cyrillic_es: Final[int]
Cyrillic_ghe: Final[int]
Cyrillic_ghe_bar: Final[int]
Cyrillic_ha: Final[int]
Cyrillic_ha_descender: Final[int]
Cyrillic_hardsign: Final[int]
Cyrillic_i: Final[int]
Cyrillic_i_macron: Final[int]
Cyrillic_ie: Final[int]
Cyrillic_io: Final[int]
Cyrillic_je: Final[int]
Cyrillic_ka: Final[int]
Cyrillic_ka_descender: Final[int]
Cyrillic_ka_vertstroke: Final[int]
Cyrillic_lje: Final[int]
Cyrillic_nje: Final[int]
Cyrillic_o: Final[int]
Cyrillic_o_bar: Final[int]
Cyrillic_pe: Final[int]
Cyrillic_schwa: Final[int]
Cyrillic_sha: Final[int]
Cyrillic_shcha: Final[int]
Cyrillic_shha: Final[int]
Cyrillic_shorti: Final[int]
Cyrillic_softsign: Final[int]
Cyrillic_te: Final[int]
Cyrillic_tse: Final[int]
Cyrillic_u: Final[int]
Cyrillic_u_macron: Final[int]
Cyrillic_u_straight: Final[int]
Cyrillic_u_straight_bar: Final[int]
Cyrillic_ve: Final[int]
Cyrillic_ya: Final[int]
Cyrillic_yeru: Final[int]
Cyrillic_yu: Final[int]
Cyrillic_ze: Final[int]
Cyrillic_zhe: Final[int]
Cyrillic_zhe_descender: Final[int]
D: Final[int]
Dabovedot: Final[int]
Dcaron: Final[int]
Delete: Final[int]
DongSign: Final[int]
Down: Final[int]
Dstroke: Final[int]
E: Final[int]
ENG: Final[int]
ETH: Final[int]
Eabovedot: Final[int]
Eacute: Final[int]
Ebelowdot: Final[int]
Ecaron: Final[int]
Ecircumflex: Final[int]
Ecircumflexacute: Final[int]
Ecircumflexbelowdot: Final[int]
Ecircumflexgrave: Final[int]
Ecircumflexhook: Final[int]
Ecircumflextilde: Final[int]
EcuSign: Final[int]
Ediaeresis: Final[int]
Egrave: Final[int]
Ehook: Final[int]
Eisu_Shift: Final[int]
Eisu_toggle: Final[int]
Emacron: Final[int]
End: Final[int]
Eogonek: Final[int]
Escape: Final[int]
Eth: Final[int]
Etilde: Final[int]
EuroSign: Final[int]
Execute: Final[int]
F: Final[int]
F1: Final[int]
F10: Final[int]
F11: Final[int]
F12: Final[int]
F13: Final[int]
F14: Final[int]
F15: Final[int]
F16: Final[int]
F17: Final[int]
F18: Final[int]
F19: Final[int]
F2: Final[int]
F20: Final[int]
F21: Final[int]
F22: Final[int]
F23: Final[int]
F24: Final[int]
F25: Final[int]
F26: Final[int]
F27: Final[int]
F28: Final[int]
F29: Final[int]
F3: Final[int]
F30: Final[int]
F31: Final[int]
F32: Final[int]
F33: Final[int]
F34: Final[int]
F35: Final[int]
F4: Final[int]
F5: Final[int]
F6: Final[int]
F7: Final[int]
F8: Final[int]
F9: Final[int]
FFrancSign: Final[int]
Fabovedot: Final[int]
Farsi_0: Final[int]
Farsi_1: Final[int]
Farsi_2: Final[int]
Farsi_3: Final[int]
Farsi_4: Final[int]
Farsi_5: Final[int]
Farsi_6: Final[int]
Farsi_7: Final[int]
Farsi_8: Final[int]
Farsi_9: Final[int]
Farsi_yeh: Final[int]
Find: Final[int]
First_Virtual_Screen: Final[int]
G: Final[int]
Gabovedot: Final[int]
Gbreve: Final[int]
Gcaron: Final[int]
Gcedilla: Final[int]
Gcircumflex: Final[int]
Georgian_an: Final[int]
Georgian_ban: Final[int]
Georgian_can: Final[int]
Georgian_char: Final[int]
Georgian_chin: Final[int]
Georgian_cil: Final[int]
Georgian_don: Final[int]
Georgian_en: Final[int]
Georgian_fi: Final[int]
Georgian_gan: Final[int]
Georgian_ghan: Final[int]
Georgian_hae: Final[int]
Georgian_har: Final[int]
Georgian_he: Final[int]
Georgian_hie: Final[int]
Georgian_hoe: Final[int]
Georgian_in: Final[int]
Georgian_jhan: Final[int]
Georgian_jil: Final[int]
Georgian_kan: Final[int]
Georgian_khar: Final[int]
Georgian_las: Final[int]
Georgian_man: Final[int]
Georgian_nar: Final[int]
Georgian_on: Final[int]
Georgian_par: Final[int]
Georgian_phar: Final[int]
Georgian_qar: Final[int]
Georgian_rae: Final[int]
Georgian_san: Final[int]
Georgian_shin: Final[int]
Georgian_tan: Final[int]
Georgian_tar: Final[int]
Georgian_un: Final[int]
Georgian_vin: Final[int]
Georgian_we: Final[int]
Georgian_xan: Final[int]
Georgian_zen: Final[int]
Georgian_zhar: Final[int]
Greek_ALPHA: Final[int]
Greek_ALPHAaccent: Final[int]
Greek_BETA: Final[int]
Greek_CHI: Final[int]
Greek_DELTA: Final[int]
Greek_EPSILON: Final[int]
Greek_EPSILONaccent: Final[int]
Greek_ETA: Final[int]
Greek_ETAaccent: Final[int]
Greek_GAMMA: Final[int]
Greek_IOTA: Final[int]
Greek_IOTAaccent: Final[int]
Greek_IOTAdiaeresis: Final[int]
Greek_IOTAdieresis: Final[int]
Greek_KAPPA: Final[int]
Greek_LAMBDA: Final[int]
Greek_LAMDA: Final[int]
Greek_MU: Final[int]
Greek_NU: Final[int]
Greek_OMEGA: Final[int]
Greek_OMEGAaccent: Final[int]
Greek_OMICRON: Final[int]
Greek_OMICRONaccent: Final[int]
Greek_PHI: Final[int]
Greek_PI: Final[int]
Greek_PSI: Final[int]
Greek_RHO: Final[int]
Greek_SIGMA: Final[int]
Greek_TAU: Final[int]
Greek_THETA: Final[int]
Greek_UPSILON: Final[int]
Greek_UPSILONaccent: Final[int]
Greek_UPSILONdieresis: Final[int]
Greek_XI: Final[int]
Greek_ZETA: Final[int]
Greek_accentdieresis: Final[int]
Greek_alpha: Final[int]
Greek_alphaaccent: Final[int]
Greek_beta: Final[int]
Greek_chi: Final[int]
Greek_delta: Final[int]
Greek_epsilon: Final[int]
Greek_epsilonaccent: Final[int]
Greek_eta: Final[int]
Greek_etaaccent: Final[int]
Greek_finalsmallsigma: Final[int]
Greek_gamma: Final[int]
Greek_horizbar: Final[int]
Greek_iota: Final[int]
Greek_iotaaccent: Final[int]
Greek_iotaaccentdieresis: Final[int]
Greek_iotadieresis: Final[int]
Greek_kappa: Final[int]
Greek_lambda: Final[int]
Greek_lamda: Final[int]
Greek_mu: Final[int]
Greek_nu: Final[int]
Greek_omega: Final[int]
Greek_omegaaccent: Final[int]
Greek_omicron: Final[int]
Greek_omicronaccent: Final[int]
Greek_phi: Final[int]
Greek_pi: Final[int]
Greek_psi: Final[int]
Greek_rho: Final[int]
Greek_sigma: Final[int]
Greek_switch: Final[int]
Greek_tau: Final[int]
Greek_theta: Final[int]
Greek_upsilon: Final[int]
Greek_upsilonaccent: Final[int]
Greek_upsilonaccentdieresis: Final[int]
Greek_upsilondieresis: Final[int]
Greek_xi: Final[int]
Greek_zeta: Final[int]
H: Final[int]
Hangul: Final[int]
Hangul_A: Final[int]
Hangul_AE: Final[int]
Hangul_AraeA: Final[int]
Hangul_AraeAE: Final[int]
Hangul_Banja: Final[int]
Hangul_Cieuc: Final[int]
Hangul_Codeinput: Final[int]
Hangul_Dikeud: Final[int]
Hangul_E: Final[int]
Hangul_EO: Final[int]
Hangul_EU: Final[int]
Hangul_End: Final[int]
Hangul_Hanja: Final[int]
Hangul_Hieuh: Final[int]
Hangul_I: Final[int]
Hangul_Ieung: Final[int]
Hangul_J_Cieuc: Final[int]
Hangul_J_Dikeud: Final[int]
Hangul_J_Hieuh: Final[int]
Hangul_J_Ieung: Final[int]
Hangul_J_Jieuj: Final[int]
Hangul_J_Khieuq: Final[int]
Hangul_J_Kiyeog: Final[int]
Hangul_J_KiyeogSios: Final[int]
Hangul_J_KkogjiDalrinIeung: Final[int]
Hangul_J_Mieum: Final[int]
Hangul_J_Nieun: Final[int]
Hangul_J_NieunHieuh: Final[int]
Hangul_J_NieunJieuj: Final[int]
Hangul_J_PanSios: Final[int]
Hangul_J_Phieuf: Final[int]
Hangul_J_Pieub: Final[int]
Hangul_J_PieubSios: Final[int]
Hangul_J_Rieul: Final[int]
Hangul_J_RieulHieuh: Final[int]
Hangul_J_RieulKiyeog: Final[int]
Hangul_J_RieulMieum: Final[int]
Hangul_J_RieulPhieuf: Final[int]
Hangul_J_RieulPieub: Final[int]
Hangul_J_RieulSios: Final[int]
Hangul_J_RieulTieut: Final[int]
Hangul_J_Sios: Final[int]
Hangul_J_SsangKiyeog: Final[int]
Hangul_J_SsangSios: Final[int]
Hangul_J_Tieut: Final[int]
Hangul_J_YeorinHieuh: Final[int]
Hangul_Jamo: Final[int]
Hangul_Jeonja: Final[int]
Hangul_Jieuj: Final[int]
Hangul_Khieuq: Final[int]
Hangul_Kiyeog: Final[int]
Hangul_KiyeogSios: Final[int]
Hangul_KkogjiDalrinIeung: Final[int]
Hangul_Mieum: Final[int]
Hangul_MultipleCandidate: Final[int]
Hangul_Nieun: Final[int]
Hangul_NieunHieuh: Final[int]
Hangul_NieunJieuj: Final[int]
Hangul_O: Final[int]
Hangul_OE: Final[int]
Hangul_PanSios: Final[int]
Hangul_Phieuf: Final[int]
Hangul_Pieub: Final[int]
Hangul_PieubSios: Final[int]
Hangul_PostHanja: Final[int]
Hangul_PreHanja: Final[int]
Hangul_PreviousCandidate: Final[int]
Hangul_Rieul: Final[int]
Hangul_RieulHieuh: Final[int]
Hangul_RieulKiyeog: Final[int]
Hangul_RieulMieum: Final[int]
Hangul_RieulPhieuf: Final[int]
Hangul_RieulPieub: Final[int]
Hangul_RieulSios: Final[int]
Hangul_RieulTieut: Final[int]
Hangul_RieulYeorinHieuh: Final[int]
Hangul_Romaja: Final[int]
Hangul_SingleCandidate: Final[int]
Hangul_Sios: Final[int]
Hangul_Special: Final[int]
Hangul_SsangDikeud: Final[int]
Hangul_SsangJieuj: Final[int]
Hangul_SsangKiyeog: Final[int]
Hangul_SsangPieub: Final[int]
Hangul_SsangSios: Final[int]
Hangul_Start: Final[int]
Hangul_SunkyeongeumMieum: Final[int]
Hangul_SunkyeongeumPhieuf: Final[int]
Hangul_SunkyeongeumPieub: Final[int]
Hangul_Tieut: Final[int]
Hangul_U: Final[int]
Hangul_WA: Final[int]
Hangul_WAE: Final[int]
Hangul_WE: Final[int]
Hangul_WEO: Final[int]
Hangul_WI: Final[int]
Hangul_YA: Final[int]
Hangul_YAE: Final[int]
Hangul_YE: Final[int]
Hangul_YEO: Final[int]
Hangul_YI: Final[int]
Hangul_YO: Final[int]
Hangul_YU: Final[int]
Hangul_YeorinHieuh: Final[int]
Hangul_switch: Final[int]
Hankaku: Final[int]
Hcircumflex: Final[int]
Hebrew_switch: Final[int]
Help: Final[int]
Henkan: Final[int]
Henkan_Mode: Final[int]
Hiragana: Final[int]
Hiragana_Katakana: Final[int]
Home: Final[int]
Hstroke: Final[int]
Hyper_L: Final[int]
Hyper_R: Final[int]
I: Final[int]
INTERFACE_CONFIG: Final = "org.freedesktop.IBus.Config"
INTERFACE_ENGINE: Final = "org.freedesktop.IBus.Engine"
INTERFACE_FACTORY: Final = "org.freedesktop.IBus.Factory"
INTERFACE_IBUS: Final = "org.freedesktop.IBus"
INTERFACE_INPUT_CONTEXT: Final = "org.freedesktop.IBus.InputContext"
INTERFACE_NOTIFICATIONS: Final = "org.freedesktop.IBus.Notifications"
INTERFACE_PANEL: Final = "org.freedesktop.IBus.Panel"
INTERFACE_PORTAL: Final = "org.freedesktop.IBus.Portal"
ISO_Center_Object: Final[int]
ISO_Continuous_Underline: Final[int]
ISO_Discontinuous_Underline: Final[int]
ISO_Emphasize: Final[int]
ISO_Enter: Final[int]
ISO_Fast_Cursor_Down: Final[int]
ISO_Fast_Cursor_Left: Final[int]
ISO_Fast_Cursor_Right: Final[int]
ISO_Fast_Cursor_Up: Final[int]
ISO_First_Group: Final[int]
ISO_First_Group_Lock: Final[int]
ISO_Group_Latch: Final[int]
ISO_Group_Lock: Final[int]
ISO_Group_Shift: Final[int]
ISO_Last_Group: Final[int]
ISO_Last_Group_Lock: Final[int]
ISO_Left_Tab: Final[int]
ISO_Level2_Latch: Final[int]
ISO_Level3_Latch: Final[int]
ISO_Level3_Lock: Final[int]
ISO_Level3_Shift: Final[int]
ISO_Level5_Latch: Final[int]
ISO_Level5_Lock: Final[int]
ISO_Level5_Shift: Final[int]
ISO_Lock: Final[int]
ISO_Move_Line_Down: Final[int]
ISO_Move_Line_Up: Final[int]
ISO_Next_Group: Final[int]
ISO_Next_Group_Lock: Final[int]
ISO_Partial_Line_Down: Final[int]
ISO_Partial_Line_Up: Final[int]
ISO_Partial_Space_Left: Final[int]
ISO_Partial_Space_Right: Final[int]
ISO_Prev_Group: Final[int]
ISO_Prev_Group_Lock: Final[int]
ISO_Release_Both_Margins: Final[int]
ISO_Release_Margin_Left: Final[int]
ISO_Release_Margin_Right: Final[int]
ISO_Set_Margin_Left: Final[int]
ISO_Set_Margin_Right: Final[int]
Iabovedot: Final[int]
Iacute: Final[int]
Ibelowdot: Final[int]
Ibreve: Final[int]
Icircumflex: Final[int]
Idiaeresis: Final[int]
Igrave: Final[int]
Ihook: Final[int]
Imacron: Final[int]
Insert: Final[int]
Iogonek: Final[int]
Itilde: Final[int]
J: Final[int]
Jcircumflex: Final[int]
K: Final[int]
KEY_0: Final[int]
KEY_1: Final[int]
KEY_2: Final[int]
KEY_3: Final[int]
KEY_3270_AltCursor: Final[int]
KEY_3270_Attn: Final[int]
KEY_3270_BackTab: Final[int]
KEY_3270_ChangeScreen: Final[int]
KEY_3270_Copy: Final[int]
KEY_3270_CursorBlink: Final[int]
KEY_3270_CursorSelect: Final[int]
KEY_3270_DeleteWord: Final[int]
KEY_3270_Duplicate: Final[int]
KEY_3270_Enter: Final[int]
KEY_3270_EraseEOF: Final[int]
KEY_3270_EraseInput: Final[int]
KEY_3270_ExSelect: Final[int]
KEY_3270_FieldMark: Final[int]
KEY_3270_Ident: Final[int]
KEY_3270_Jump: Final[int]
KEY_3270_KeyClick: Final[int]
KEY_3270_Left2: Final[int]
KEY_3270_PA1: Final[int]
KEY_3270_PA2: Final[int]
KEY_3270_PA3: Final[int]
KEY_3270_Play: Final[int]
KEY_3270_PrintScreen: Final[int]
KEY_3270_Quit: Final[int]
KEY_3270_Record: Final[int]
KEY_3270_Reset: Final[int]
KEY_3270_Right2: Final[int]
KEY_3270_Rule: Final[int]
KEY_3270_Setup: Final[int]
KEY_3270_Test: Final[int]
KEY_4: Final[int]
KEY_5: Final[int]
KEY_6: Final[int]
KEY_7: Final[int]
KEY_8: Final[int]
KEY_9: Final[int]
KEY_A: Final[int]
KEY_AE: Final[int]
KEY_Aacute: Final[int]
KEY_Abelowdot: Final[int]
KEY_Abreve: Final[int]
KEY_Abreveacute: Final[int]
KEY_Abrevebelowdot: Final[int]
KEY_Abrevegrave: Final[int]
KEY_Abrevehook: Final[int]
KEY_Abrevetilde: Final[int]
KEY_AccessX_Enable: Final[int]
KEY_AccessX_Feedback_Enable: Final[int]
KEY_Acircumflex: Final[int]
KEY_Acircumflexacute: Final[int]
KEY_Acircumflexbelowdot: Final[int]
KEY_Acircumflexgrave: Final[int]
KEY_Acircumflexhook: Final[int]
KEY_Acircumflextilde: Final[int]
KEY_AddFavorite: Final[int]
KEY_Adiaeresis: Final[int]
KEY_Agrave: Final[int]
KEY_Ahook: Final[int]
KEY_Alt_L: Final[int]
KEY_Alt_R: Final[int]
KEY_Amacron: Final[int]
KEY_Aogonek: Final[int]
KEY_ApplicationLeft: Final[int]
KEY_ApplicationRight: Final[int]
KEY_Arabic_0: Final[int]
KEY_Arabic_1: Final[int]
KEY_Arabic_2: Final[int]
KEY_Arabic_3: Final[int]
KEY_Arabic_4: Final[int]
KEY_Arabic_5: Final[int]
KEY_Arabic_6: Final[int]
KEY_Arabic_7: Final[int]
KEY_Arabic_8: Final[int]
KEY_Arabic_9: Final[int]
KEY_Arabic_ain: Final[int]
KEY_Arabic_alef: Final[int]
KEY_Arabic_alefmaksura: Final[int]
KEY_Arabic_beh: Final[int]
KEY_Arabic_comma: Final[int]
KEY_Arabic_dad: Final[int]
KEY_Arabic_dal: Final[int]
KEY_Arabic_damma: Final[int]
KEY_Arabic_dammatan: Final[int]
KEY_Arabic_ddal: Final[int]
KEY_Arabic_farsi_yeh: Final[int]
KEY_Arabic_fatha: Final[int]
KEY_Arabic_fathatan: Final[int]
KEY_Arabic_feh: Final[int]
KEY_Arabic_fullstop: Final[int]
KEY_Arabic_gaf: Final[int]
KEY_Arabic_ghain: Final[int]
KEY_Arabic_ha: Final[int]
KEY_Arabic_hah: Final[int]
KEY_Arabic_hamza: Final[int]
KEY_Arabic_hamza_above: Final[int]
KEY_Arabic_hamza_below: Final[int]
KEY_Arabic_hamzaonalef: Final[int]
KEY_Arabic_hamzaonwaw: Final[int]
KEY_Arabic_hamzaonyeh: Final[int]
KEY_Arabic_hamzaunderalef: Final[int]
KEY_Arabic_heh: Final[int]
KEY_Arabic_heh_doachashmee: Final[int]
KEY_Arabic_heh_goal: Final[int]
KEY_Arabic_jeem: Final[int]
KEY_Arabic_jeh: Final[int]
KEY_Arabic_kaf: Final[int]
KEY_Arabic_kasra: Final[int]
KEY_Arabic_kasratan: Final[int]
KEY_Arabic_keheh: Final[int]
KEY_Arabic_khah: Final[int]
KEY_Arabic_lam: Final[int]
KEY_Arabic_madda_above: Final[int]
KEY_Arabic_maddaonalef: Final[int]
KEY_Arabic_meem: Final[int]
KEY_Arabic_noon: Final[int]
KEY_Arabic_noon_ghunna: Final[int]
KEY_Arabic_peh: Final[int]
KEY_Arabic_percent: Final[int]
KEY_Arabic_qaf: Final[int]
KEY_Arabic_question_mark: Final[int]
KEY_Arabic_ra: Final[int]
KEY_Arabic_rreh: Final[int]
KEY_Arabic_sad: Final[int]
KEY_Arabic_seen: Final[int]
KEY_Arabic_semicolon: Final[int]
KEY_Arabic_shadda: Final[int]
KEY_Arabic_sheen: Final[int]
KEY_Arabic_sukun: Final[int]
KEY_Arabic_superscript_alef: Final[int]
KEY_Arabic_switch: Final[int]
KEY_Arabic_tah: Final[int]
KEY_Arabic_tatweel: Final[int]
KEY_Arabic_tcheh: Final[int]
KEY_Arabic_teh: Final[int]
KEY_Arabic_tehmarbuta: Final[int]
KEY_Arabic_thal: Final[int]
KEY_Arabic_theh: Final[int]
KEY_Arabic_tteh: Final[int]
KEY_Arabic_veh: Final[int]
KEY_Arabic_waw: Final[int]
KEY_Arabic_yeh: Final[int]
KEY_Arabic_yeh_baree: Final[int]
KEY_Arabic_zah: Final[int]
KEY_Arabic_zain: Final[int]
KEY_Aring: Final[int]
KEY_Armenian_AT: Final[int]
KEY_Armenian_AYB: Final[int]
KEY_Armenian_BEN: Final[int]
KEY_Armenian_CHA: Final[int]
KEY_Armenian_DA: Final[int]
KEY_Armenian_DZA: Final[int]
KEY_Armenian_E: Final[int]
KEY_Armenian_FE: Final[int]
KEY_Armenian_GHAT: Final[int]
KEY_Armenian_GIM: Final[int]
KEY_Armenian_HI: Final[int]
KEY_Armenian_HO: Final[int]
KEY_Armenian_INI: Final[int]
KEY_Armenian_JE: Final[int]
KEY_Armenian_KE: Final[int]
KEY_Armenian_KEN: Final[int]
KEY_Armenian_KHE: Final[int]
KEY_Armenian_LYUN: Final[int]
KEY_Armenian_MEN: Final[int]
KEY_Armenian_NU: Final[int]
KEY_Armenian_O: Final[int]
KEY_Armenian_PE: Final[int]
KEY_Armenian_PYUR: Final[int]
KEY_Armenian_RA: Final[int]
KEY_Armenian_RE: Final[int]
KEY_Armenian_SE: Final[int]
KEY_Armenian_SHA: Final[int]
KEY_Armenian_TCHE: Final[int]
KEY_Armenian_TO: Final[int]
KEY_Armenian_TSA: Final[int]
KEY_Armenian_TSO: Final[int]
KEY_Armenian_TYUN: Final[int]
KEY_Armenian_VEV: Final[int]
KEY_Armenian_VO: Final[int]
KEY_Armenian_VYUN: Final[int]
KEY_Armenian_YECH: Final[int]
KEY_Armenian_ZA: Final[int]
KEY_Armenian_ZHE: Final[int]
KEY_Armenian_accent: Final[int]
KEY_Armenian_amanak: Final[int]
KEY_Armenian_apostrophe: Final[int]
KEY_Armenian_at: Final[int]
KEY_Armenian_ayb: Final[int]
KEY_Armenian_ben: Final[int]
KEY_Armenian_but: Final[int]
KEY_Armenian_cha: Final[int]
KEY_Armenian_da: Final[int]
KEY_Armenian_dza: Final[int]
KEY_Armenian_e: Final[int]
KEY_Armenian_exclam: Final[int]
KEY_Armenian_fe: Final[int]
KEY_Armenian_full_stop: Final[int]
KEY_Armenian_ghat: Final[int]
KEY_Armenian_gim: Final[int]
KEY_Armenian_hi: Final[int]
KEY_Armenian_ho: Final[int]
KEY_Armenian_hyphen: Final[int]
KEY_Armenian_ini: Final[int]
KEY_Armenian_je: Final[int]
KEY_Armenian_ke: Final[int]
KEY_Armenian_ken: Final[int]
KEY_Armenian_khe: Final[int]
KEY_Armenian_ligature_ew: Final[int]
KEY_Armenian_lyun: Final[int]
KEY_Armenian_men: Final[int]
KEY_Armenian_nu: Final[int]
KEY_Armenian_o: Final[int]
KEY_Armenian_paruyk: Final[int]
KEY_Armenian_pe: Final[int]
KEY_Armenian_pyur: Final[int]
KEY_Armenian_question: Final[int]
KEY_Armenian_ra: Final[int]
KEY_Armenian_re: Final[int]
KEY_Armenian_se: Final[int]
KEY_Armenian_separation_mark: Final[int]
KEY_Armenian_sha: Final[int]
KEY_Armenian_shesht: Final[int]
KEY_Armenian_tche: Final[int]
KEY_Armenian_to: Final[int]
KEY_Armenian_tsa: Final[int]
KEY_Armenian_tso: Final[int]
KEY_Armenian_tyun: Final[int]
KEY_Armenian_verjaket: Final[int]
KEY_Armenian_vev: Final[int]
KEY_Armenian_vo: Final[int]
KEY_Armenian_vyun: Final[int]
KEY_Armenian_yech: Final[int]
KEY_Armenian_yentamna: Final[int]
KEY_Armenian_za: Final[int]
KEY_Armenian_zhe: Final[int]
KEY_Atilde: Final[int]
KEY_AudibleBell_Enable: Final[int]
KEY_AudioCycleTrack: Final[int]
KEY_AudioForward: Final[int]
KEY_AudioLowerVolume: Final[int]
KEY_AudioMedia: Final[int]
KEY_AudioMicMute: Final[int]
KEY_AudioMute: Final[int]
KEY_AudioNext: Final[int]
KEY_AudioPause: Final[int]
KEY_AudioPlay: Final[int]
KEY_AudioPreset: Final[int]
KEY_AudioPrev: Final[int]
KEY_AudioRaiseVolume: Final[int]
KEY_AudioRandomPlay: Final[int]
KEY_AudioRecord: Final[int]
KEY_AudioRepeat: Final[int]
KEY_AudioRewind: Final[int]
KEY_AudioStop: Final[int]
KEY_Away: Final[int]
KEY_B: Final[int]
KEY_Babovedot: Final[int]
KEY_Back: Final[int]
KEY_BackForward: Final[int]
KEY_BackSpace: Final[int]
KEY_Battery: Final[int]
KEY_Begin: Final[int]
KEY_Blue: Final[int]
KEY_Bluetooth: Final[int]
KEY_Book: Final[int]
KEY_BounceKeys_Enable: Final[int]
KEY_Break: Final[int]
KEY_BrightnessAdjust: Final[int]
KEY_Byelorussian_SHORTU: Final[int]
KEY_Byelorussian_shortu: Final[int]
KEY_C: Final[int]
KEY_CD: Final[int]
KEY_CH: Final[int]
KEY_C_H: Final[int]
KEY_C_h: Final[int]
KEY_Cabovedot: Final[int]
KEY_Cacute: Final[int]
KEY_Calculator: Final[int]
KEY_Calendar: Final[int]
KEY_Cancel: Final[int]
KEY_Caps_Lock: Final[int]
KEY_Ccaron: Final[int]
KEY_Ccedilla: Final[int]
KEY_Ccircumflex: Final[int]
KEY_Ch: Final[int]
KEY_Clear: Final[int]
KEY_ClearGrab: Final[int]
KEY_Close: Final[int]
KEY_Codeinput: Final[int]
KEY_ColonSign: Final[int]
KEY_Community: Final[int]
KEY_ContrastAdjust: Final[int]
KEY_Control_L: Final[int]
KEY_Control_R: Final[int]
KEY_Copy: Final[int]
KEY_CruzeiroSign: Final[int]
KEY_Cut: Final[int]
KEY_CycleAngle: Final[int]
KEY_Cyrillic_A: Final[int]
KEY_Cyrillic_BE: Final[int]
KEY_Cyrillic_CHE: Final[int]
KEY_Cyrillic_CHE_descender: Final[int]
KEY_Cyrillic_CHE_vertstroke: Final[int]
KEY_Cyrillic_DE: Final[int]
KEY_Cyrillic_DZHE: Final[int]
KEY_Cyrillic_E: Final[int]
KEY_Cyrillic_EF: Final[int]
KEY_Cyrillic_EL: Final[int]
KEY_Cyrillic_EM: Final[int]
KEY_Cyrillic_EN: Final[int]
KEY_Cyrillic_EN_descender: Final[int]
KEY_Cyrillic_ER: Final[int]
KEY_Cyrillic_ES: Final[int]
KEY_Cyrillic_GHE: Final[int]
KEY_Cyrillic_GHE_bar: Final[int]
KEY_Cyrillic_HA: Final[int]
KEY_Cyrillic_HARDSIGN: Final[int]
KEY_Cyrillic_HA_descender: Final[int]
KEY_Cyrillic_I: Final[int]
KEY_Cyrillic_IE: Final[int]
KEY_Cyrillic_IO: Final[int]
KEY_Cyrillic_I_macron: Final[int]
KEY_Cyrillic_JE: Final[int]
KEY_Cyrillic_KA: Final[int]
KEY_Cyrillic_KA_descender: Final[int]
KEY_Cyrillic_KA_vertstroke: Final[int]
KEY_Cyrillic_LJE: Final[int]
KEY_Cyrillic_NJE: Final[int]
KEY_Cyrillic_O: Final[int]
KEY_Cyrillic_O_bar: Final[int]
KEY_Cyrillic_PE: Final[int]
KEY_Cyrillic_SCHWA: Final[int]
KEY_Cyrillic_SHA: Final[int]
KEY_Cyrillic_SHCHA: Final[int]
KEY_Cyrillic_SHHA: Final[int]
KEY_Cyrillic_SHORTI: Final[int]
KEY_Cyrillic_SOFTSIGN: Final[int]
KEY_Cyrillic_TE: Final[int]
KEY_Cyrillic_TSE: Final[int]
KEY_Cyrillic_U: Final[int]
KEY_Cyrillic_U_macron: Final[int]
KEY_Cyrillic_U_straight: Final[int]
KEY_Cyrillic_U_straight_bar: Final[int]
KEY_Cyrillic_VE: Final[int]
KEY_Cyrillic_YA: Final[int]
KEY_Cyrillic_YERU: Final[int]
KEY_Cyrillic_YU: Final[int]
KEY_Cyrillic_ZE: Final[int]
KEY_Cyrillic_ZHE: Final[int]
KEY_Cyrillic_ZHE_descender: Final[int]
KEY_Cyrillic_a: Final[int]
KEY_Cyrillic_be: Final[int]
KEY_Cyrillic_che: Final[int]
KEY_Cyrillic_che_descender: Final[int]
KEY_Cyrillic_che_vertstroke: Final[int]
KEY_Cyrillic_de: Final[int]
KEY_Cyrillic_dzhe: Final[int]
KEY_Cyrillic_e: Final[int]
KEY_Cyrillic_ef: Final[int]
KEY_Cyrillic_el: Final[int]
KEY_Cyrillic_em: Final[int]
KEY_Cyrillic_en: Final[int]
KEY_Cyrillic_en_descender: Final[int]
KEY_Cyrillic_er: Final[int]
KEY_Cyrillic_es: Final[int]
KEY_Cyrillic_ghe: Final[int]
KEY_Cyrillic_ghe_bar: Final[int]
KEY_Cyrillic_ha: Final[int]
KEY_Cyrillic_ha_descender: Final[int]
KEY_Cyrillic_hardsign: Final[int]
KEY_Cyrillic_i: Final[int]
KEY_Cyrillic_i_macron: Final[int]
KEY_Cyrillic_ie: Final[int]
KEY_Cyrillic_io: Final[int]
KEY_Cyrillic_je: Final[int]
KEY_Cyrillic_ka: Final[int]
KEY_Cyrillic_ka_descender: Final[int]
KEY_Cyrillic_ka_vertstroke: Final[int]
KEY_Cyrillic_lje: Final[int]
KEY_Cyrillic_nje: Final[int]
KEY_Cyrillic_o: Final[int]
KEY_Cyrillic_o_bar: Final[int]
KEY_Cyrillic_pe: Final[int]
KEY_Cyrillic_schwa: Final[int]
KEY_Cyrillic_sha: Final[int]
KEY_Cyrillic_shcha: Final[int]
KEY_Cyrillic_shha: Final[int]
KEY_Cyrillic_shorti: Final[int]
KEY_Cyrillic_softsign: Final[int]
KEY_Cyrillic_te: Final[int]
KEY_Cyrillic_tse: Final[int]
KEY_Cyrillic_u: Final[int]
KEY_Cyrillic_u_macron: Final[int]
KEY_Cyrillic_u_straight: Final[int]
KEY_Cyrillic_u_straight_bar: Final[int]
KEY_Cyrillic_ve: Final[int]
KEY_Cyrillic_ya: Final[int]
KEY_Cyrillic_yeru: Final[int]
KEY_Cyrillic_yu: Final[int]
KEY_Cyrillic_ze: Final[int]
KEY_Cyrillic_zhe: Final[int]
KEY_Cyrillic_zhe_descender: Final[int]
KEY_D: Final[int]
KEY_DOS: Final[int]
KEY_Dabovedot: Final[int]
KEY_Dcaron: Final[int]
KEY_Delete: Final[int]
KEY_Display: Final[int]
KEY_Documents: Final[int]
KEY_DongSign: Final[int]
KEY_Down: Final[int]
KEY_Dstroke: Final[int]
KEY_E: Final[int]
KEY_ENG: Final[int]
KEY_ETH: Final[int]
KEY_EZH: Final[int]
KEY_Eabovedot: Final[int]
KEY_Eacute: Final[int]
KEY_Ebelowdot: Final[int]
KEY_Ecaron: Final[int]
KEY_Ecircumflex: Final[int]
KEY_Ecircumflexacute: Final[int]
KEY_Ecircumflexbelowdot: Final[int]
KEY_Ecircumflexgrave: Final[int]
KEY_Ecircumflexhook: Final[int]
KEY_Ecircumflextilde: Final[int]
KEY_EcuSign: Final[int]
KEY_Ediaeresis: Final[int]
KEY_Egrave: Final[int]
KEY_Ehook: Final[int]
KEY_Eisu_Shift: Final[int]
KEY_Eisu_toggle: Final[int]
KEY_Eject: Final[int]
KEY_Emacron: Final[int]
KEY_End: Final[int]
KEY_Eogonek: Final[int]
KEY_Escape: Final[int]
KEY_Eth: Final[int]
KEY_Etilde: Final[int]
KEY_EuroSign: Final[int]
KEY_Excel: Final[int]
KEY_Execute: Final[int]
KEY_Explorer: Final[int]
KEY_F: Final[int]
KEY_F1: Final[int]
KEY_F10: Final[int]
KEY_F11: Final[int]
KEY_F12: Final[int]
KEY_F13: Final[int]
KEY_F14: Final[int]
KEY_F15: Final[int]
KEY_F16: Final[int]
KEY_F17: Final[int]
KEY_F18: Final[int]
KEY_F19: Final[int]
KEY_F2: Final[int]
KEY_F20: Final[int]
KEY_F21: Final[int]
KEY_F22: Final[int]
KEY_F23: Final[int]
KEY_F24: Final[int]
KEY_F25: Final[int]
KEY_F26: Final[int]
KEY_F27: Final[int]
KEY_F28: Final[int]
KEY_F29: Final[int]
KEY_F3: Final[int]
KEY_F30: Final[int]
KEY_F31: Final[int]
KEY_F32: Final[int]
KEY_F33: Final[int]
KEY_F34: Final[int]
KEY_F35: Final[int]
KEY_F4: Final[int]
KEY_F5: Final[int]
KEY_F6: Final[int]
KEY_F7: Final[int]
KEY_F8: Final[int]
KEY_F9: Final[int]
KEY_FFrancSign: Final[int]
KEY_Fabovedot: Final[int]
KEY_Farsi_0: Final[int]
KEY_Farsi_1: Final[int]
KEY_Farsi_2: Final[int]
KEY_Farsi_3: Final[int]
KEY_Farsi_4: Final[int]
KEY_Farsi_5: Final[int]
KEY_Farsi_6: Final[int]
KEY_Farsi_7: Final[int]
KEY_Farsi_8: Final[int]
KEY_Farsi_9: Final[int]
KEY_Farsi_yeh: Final[int]
KEY_Favorites: Final[int]
KEY_Finance: Final[int]
KEY_Find: Final[int]
KEY_First_Virtual_Screen: Final[int]
KEY_Forward: Final[int]
KEY_FrameBack: Final[int]
KEY_FrameForward: Final[int]
KEY_G: Final[int]
KEY_Gabovedot: Final[int]
KEY_Game: Final[int]
KEY_Gbreve: Final[int]
KEY_Gcaron: Final[int]
KEY_Gcedilla: Final[int]
KEY_Gcircumflex: Final[int]
KEY_Georgian_an: Final[int]
KEY_Georgian_ban: Final[int]
KEY_Georgian_can: Final[int]
KEY_Georgian_char: Final[int]
KEY_Georgian_chin: Final[int]
KEY_Georgian_cil: Final[int]
KEY_Georgian_don: Final[int]
KEY_Georgian_en: Final[int]
KEY_Georgian_fi: Final[int]
KEY_Georgian_gan: Final[int]
KEY_Georgian_ghan: Final[int]
KEY_Georgian_hae: Final[int]
KEY_Georgian_har: Final[int]
KEY_Georgian_he: Final[int]
KEY_Georgian_hie: Final[int]
KEY_Georgian_hoe: Final[int]
KEY_Georgian_in: Final[int]
KEY_Georgian_jhan: Final[int]
KEY_Georgian_jil: Final[int]
KEY_Georgian_kan: Final[int]
KEY_Georgian_khar: Final[int]
KEY_Georgian_las: Final[int]
KEY_Georgian_man: Final[int]
KEY_Georgian_nar: Final[int]
KEY_Georgian_on: Final[int]
KEY_Georgian_par: Final[int]
KEY_Georgian_phar: Final[int]
KEY_Georgian_qar: Final[int]
KEY_Georgian_rae: Final[int]
KEY_Georgian_san: Final[int]
KEY_Georgian_shin: Final[int]
KEY_Georgian_tan: Final[int]
KEY_Georgian_tar: Final[int]
KEY_Georgian_un: Final[int]
KEY_Georgian_vin: Final[int]
KEY_Georgian_we: Final[int]
KEY_Georgian_xan: Final[int]
KEY_Georgian_zen: Final[int]
KEY_Georgian_zhar: Final[int]
KEY_Go: Final[int]
KEY_Greek_ALPHA: Final[int]
KEY_Greek_ALPHAaccent: Final[int]
KEY_Greek_BETA: Final[int]
KEY_Greek_CHI: Final[int]
KEY_Greek_DELTA: Final[int]
KEY_Greek_EPSILON: Final[int]
KEY_Greek_EPSILONaccent: Final[int]
KEY_Greek_ETA: Final[int]
KEY_Greek_ETAaccent: Final[int]
KEY_Greek_GAMMA: Final[int]
KEY_Greek_IOTA: Final[int]
KEY_Greek_IOTAaccent: Final[int]
KEY_Greek_IOTAdiaeresis: Final[int]
KEY_Greek_IOTAdieresis: Final[int]
KEY_Greek_KAPPA: Final[int]
KEY_Greek_LAMBDA: Final[int]
KEY_Greek_LAMDA: Final[int]
KEY_Greek_MU: Final[int]
KEY_Greek_NU: Final[int]
KEY_Greek_OMEGA: Final[int]
KEY_Greek_OMEGAaccent: Final[int]
KEY_Greek_OMICRON: Final[int]
KEY_Greek_OMICRONaccent: Final[int]
KEY_Greek_PHI: Final[int]
KEY_Greek_PI: Final[int]
KEY_Greek_PSI: Final[int]
KEY_Greek_RHO: Final[int]
KEY_Greek_SIGMA: Final[int]
KEY_Greek_TAU: Final[int]
KEY_Greek_THETA: Final[int]
KEY_Greek_UPSILON: Final[int]
KEY_Greek_UPSILONaccent: Final[int]
KEY_Greek_UPSILONdieresis: Final[int]
KEY_Greek_XI: Final[int]
KEY_Greek_ZETA: Final[int]
KEY_Greek_accentdieresis: Final[int]
KEY_Greek_alpha: Final[int]
KEY_Greek_alphaaccent: Final[int]
KEY_Greek_beta: Final[int]
KEY_Greek_chi: Final[int]
KEY_Greek_delta: Final[int]
KEY_Greek_epsilon: Final[int]
KEY_Greek_epsilonaccent: Final[int]
KEY_Greek_eta: Final[int]
KEY_Greek_etaaccent: Final[int]
KEY_Greek_finalsmallsigma: Final[int]
KEY_Greek_gamma: Final[int]
KEY_Greek_horizbar: Final[int]
KEY_Greek_iota: Final[int]
KEY_Greek_iotaaccent: Final[int]
KEY_Greek_iotaaccentdieresis: Final[int]
KEY_Greek_iotadieresis: Final[int]
KEY_Greek_kappa: Final[int]
KEY_Greek_lambda: Final[int]
KEY_Greek_lamda: Final[int]
KEY_Greek_mu: Final[int]
KEY_Greek_nu: Final[int]
KEY_Greek_omega: Final[int]
KEY_Greek_omegaaccent: Final[int]
KEY_Greek_omicron: Final[int]
KEY_Greek_omicronaccent: Final[int]
KEY_Greek_phi: Final[int]
KEY_Greek_pi: Final[int]
KEY_Greek_psi: Final[int]
KEY_Greek_rho: Final[int]
KEY_Greek_sigma: Final[int]
KEY_Greek_switch: Final[int]
KEY_Greek_tau: Final[int]
KEY_Greek_theta: Final[int]
KEY_Greek_upsilon: Final[int]
KEY_Greek_upsilonaccent: Final[int]
KEY_Greek_upsilonaccentdieresis: Final[int]
KEY_Greek_upsilondieresis: Final[int]
KEY_Greek_xi: Final[int]
KEY_Greek_zeta: Final[int]
KEY_Green: Final[int]
KEY_H: Final[int]
KEY_Hangul: Final[int]
KEY_Hangul_A: Final[int]
KEY_Hangul_AE: Final[int]
KEY_Hangul_AraeA: Final[int]
KEY_Hangul_AraeAE: Final[int]
KEY_Hangul_Banja: Final[int]
KEY_Hangul_Cieuc: Final[int]
KEY_Hangul_Codeinput: Final[int]
KEY_Hangul_Dikeud: Final[int]
KEY_Hangul_E: Final[int]
KEY_Hangul_EO: Final[int]
KEY_Hangul_EU: Final[int]
KEY_Hangul_End: Final[int]
KEY_Hangul_Hanja: Final[int]
KEY_Hangul_Hieuh: Final[int]
KEY_Hangul_I: Final[int]
KEY_Hangul_Ieung: Final[int]
KEY_Hangul_J_Cieuc: Final[int]
KEY_Hangul_J_Dikeud: Final[int]
KEY_Hangul_J_Hieuh: Final[int]
KEY_Hangul_J_Ieung: Final[int]
KEY_Hangul_J_Jieuj: Final[int]
KEY_Hangul_J_Khieuq: Final[int]
KEY_Hangul_J_Kiyeog: Final[int]
KEY_Hangul_J_KiyeogSios: Final[int]
KEY_Hangul_J_KkogjiDalrinIeung: Final[int]
KEY_Hangul_J_Mieum: Final[int]
KEY_Hangul_J_Nieun: Final[int]
KEY_Hangul_J_NieunHieuh: Final[int]
KEY_Hangul_J_NieunJieuj: Final[int]
KEY_Hangul_J_PanSios: Final[int]
KEY_Hangul_J_Phieuf: Final[int]
KEY_Hangul_J_Pieub: Final[int]
KEY_Hangul_J_PieubSios: Final[int]
KEY_Hangul_J_Rieul: Final[int]
KEY_Hangul_J_RieulHieuh: Final[int]
KEY_Hangul_J_RieulKiyeog: Final[int]
KEY_Hangul_J_RieulMieum: Final[int]
KEY_Hangul_J_RieulPhieuf: Final[int]
KEY_Hangul_J_RieulPieub: Final[int]
KEY_Hangul_J_RieulSios: Final[int]
KEY_Hangul_J_RieulTieut: Final[int]
KEY_Hangul_J_Sios: Final[int]
KEY_Hangul_J_SsangKiyeog: Final[int]
KEY_Hangul_J_SsangSios: Final[int]
KEY_Hangul_J_Tieut: Final[int]
KEY_Hangul_J_YeorinHieuh: Final[int]
KEY_Hangul_Jamo: Final[int]
KEY_Hangul_Jeonja: Final[int]
KEY_Hangul_Jieuj: Final[int]
KEY_Hangul_Khieuq: Final[int]
KEY_Hangul_Kiyeog: Final[int]
KEY_Hangul_KiyeogSios: Final[int]
KEY_Hangul_KkogjiDalrinIeung: Final[int]
KEY_Hangul_Mieum: Final[int]
KEY_Hangul_MultipleCandidate: Final[int]
KEY_Hangul_Nieun: Final[int]
KEY_Hangul_NieunHieuh: Final[int]
KEY_Hangul_NieunJieuj: Final[int]
KEY_Hangul_O: Final[int]
KEY_Hangul_OE: Final[int]
KEY_Hangul_PanSios: Final[int]
KEY_Hangul_Phieuf: Final[int]
KEY_Hangul_Pieub: Final[int]
KEY_Hangul_PieubSios: Final[int]
KEY_Hangul_PostHanja: Final[int]
KEY_Hangul_PreHanja: Final[int]
KEY_Hangul_PreviousCandidate: Final[int]
KEY_Hangul_Rieul: Final[int]
KEY_Hangul_RieulHieuh: Final[int]
KEY_Hangul_RieulKiyeog: Final[int]
KEY_Hangul_RieulMieum: Final[int]
KEY_Hangul_RieulPhieuf: Final[int]
KEY_Hangul_RieulPieub: Final[int]
KEY_Hangul_RieulSios: Final[int]
KEY_Hangul_RieulTieut: Final[int]
KEY_Hangul_RieulYeorinHieuh: Final[int]
KEY_Hangul_Romaja: Final[int]
KEY_Hangul_SingleCandidate: Final[int]
KEY_Hangul_Sios: Final[int]
KEY_Hangul_Special: Final[int]
KEY_Hangul_SsangDikeud: Final[int]
KEY_Hangul_SsangJieuj: Final[int]
KEY_Hangul_SsangKiyeog: Final[int]
KEY_Hangul_SsangPieub: Final[int]
KEY_Hangul_SsangSios: Final[int]
KEY_Hangul_Start: Final[int]
KEY_Hangul_SunkyeongeumMieum: Final[int]
KEY_Hangul_SunkyeongeumPhieuf: Final[int]
KEY_Hangul_SunkyeongeumPieub: Final[int]
KEY_Hangul_Tieut: Final[int]
KEY_Hangul_U: Final[int]
KEY_Hangul_WA: Final[int]
KEY_Hangul_WAE: Final[int]
KEY_Hangul_WE: Final[int]
KEY_Hangul_WEO: Final[int]
KEY_Hangul_WI: Final[int]
KEY_Hangul_YA: Final[int]
KEY_Hangul_YAE: Final[int]
KEY_Hangul_YE: Final[int]
KEY_Hangul_YEO: Final[int]
KEY_Hangul_YI: Final[int]
KEY_Hangul_YO: Final[int]
KEY_Hangul_YU: Final[int]
KEY_Hangul_YeorinHieuh: Final[int]
KEY_Hangul_switch: Final[int]
KEY_Hankaku: Final[int]
KEY_Hcircumflex: Final[int]
KEY_Hebrew_switch: Final[int]
KEY_Help: Final[int]
KEY_Henkan: Final[int]
KEY_Henkan_Mode: Final[int]
KEY_Hibernate: Final[int]
KEY_Hiragana: Final[int]
KEY_Hiragana_Katakana: Final[int]
KEY_History: Final[int]
KEY_Home: Final[int]
KEY_HomePage: Final[int]
KEY_HotLinks: Final[int]
KEY_Hstroke: Final[int]
KEY_Hyper_L: Final[int]
KEY_Hyper_R: Final[int]
KEY_I: Final[int]
KEY_ISO_Center_Object: Final[int]
KEY_ISO_Continuous_Underline: Final[int]
KEY_ISO_Discontinuous_Underline: Final[int]
KEY_ISO_Emphasize: Final[int]
KEY_ISO_Enter: Final[int]
KEY_ISO_Fast_Cursor_Down: Final[int]
KEY_ISO_Fast_Cursor_Left: Final[int]
KEY_ISO_Fast_Cursor_Right: Final[int]
KEY_ISO_Fast_Cursor_Up: Final[int]
KEY_ISO_First_Group: Final[int]
KEY_ISO_First_Group_Lock: Final[int]
KEY_ISO_Group_Latch: Final[int]
KEY_ISO_Group_Lock: Final[int]
KEY_ISO_Group_Shift: Final[int]
KEY_ISO_Last_Group: Final[int]
KEY_ISO_Last_Group_Lock: Final[int]
KEY_ISO_Left_Tab: Final[int]
KEY_ISO_Level2_Latch: Final[int]
KEY_ISO_Level3_Latch: Final[int]
KEY_ISO_Level3_Lock: Final[int]
KEY_ISO_Level3_Shift: Final[int]
KEY_ISO_Level5_Latch: Final[int]
KEY_ISO_Level5_Lock: Final[int]
KEY_ISO_Level5_Shift: Final[int]
KEY_ISO_Lock: Final[int]
KEY_ISO_Move_Line_Down: Final[int]
KEY_ISO_Move_Line_Up: Final[int]
KEY_ISO_Next_Group: Final[int]
KEY_ISO_Next_Group_Lock: Final[int]
KEY_ISO_Partial_Line_Down: Final[int]
KEY_ISO_Partial_Line_Up: Final[int]
KEY_ISO_Partial_Space_Left: Final[int]
KEY_ISO_Partial_Space_Right: Final[int]
KEY_ISO_Prev_Group: Final[int]
KEY_ISO_Prev_Group_Lock: Final[int]
KEY_ISO_Release_Both_Margins: Final[int]
KEY_ISO_Release_Margin_Left: Final[int]
KEY_ISO_Release_Margin_Right: Final[int]
KEY_ISO_Set_Margin_Left: Final[int]
KEY_ISO_Set_Margin_Right: Final[int]
KEY_Iabovedot: Final[int]
KEY_Iacute: Final[int]
KEY_Ibelowdot: Final[int]
KEY_Ibreve: Final[int]
KEY_Icircumflex: Final[int]
KEY_Idiaeresis: Final[int]
KEY_Igrave: Final[int]
KEY_Ihook: Final[int]
KEY_Imacron: Final[int]
KEY_Insert: Final[int]
KEY_Iogonek: Final[int]
KEY_Itilde: Final[int]
KEY_J: Final[int]
KEY_Jcircumflex: Final[int]
KEY_K: Final[int]
KEY_KP_0: Final[int]
KEY_KP_1: Final[int]
KEY_KP_2: Final[int]
KEY_KP_3: Final[int]
KEY_KP_4: Final[int]
KEY_KP_5: Final[int]
KEY_KP_6: Final[int]
KEY_KP_7: Final[int]
KEY_KP_8: Final[int]
KEY_KP_9: Final[int]
KEY_KP_Add: Final[int]
KEY_KP_Begin: Final[int]
KEY_KP_Decimal: Final[int]
KEY_KP_Delete: Final[int]
KEY_KP_Divide: Final[int]
KEY_KP_Down: Final[int]
KEY_KP_End: Final[int]
KEY_KP_Enter: Final[int]
KEY_KP_Equal: Final[int]
KEY_KP_F1: Final[int]
KEY_KP_F2: Final[int]
KEY_KP_F3: Final[int]
KEY_KP_F4: Final[int]
KEY_KP_Home: Final[int]
KEY_KP_Insert: Final[int]
KEY_KP_Left: Final[int]
KEY_KP_Multiply: Final[int]
KEY_KP_Next: Final[int]
KEY_KP_Page_Down: Final[int]
KEY_KP_Page_Up: Final[int]
KEY_KP_Prior: Final[int]
KEY_KP_Right: Final[int]
KEY_KP_Separator: Final[int]
KEY_KP_Space: Final[int]
KEY_KP_Subtract: Final[int]
KEY_KP_Tab: Final[int]
KEY_KP_Up: Final[int]
KEY_Kana_Lock: Final[int]
KEY_Kana_Shift: Final[int]
KEY_Kanji: Final[int]
KEY_Kanji_Bangou: Final[int]
KEY_Katakana: Final[int]
KEY_KbdBrightnessDown: Final[int]
KEY_KbdBrightnessUp: Final[int]
KEY_KbdLightOnOff: Final[int]
KEY_Kcedilla: Final[int]
KEY_Keyboard: Final[int]
KEY_Korean_Won: Final[int]
KEY_L: Final[int]
KEY_L1: Final[int]
KEY_L10: Final[int]
KEY_L2: Final[int]
KEY_L3: Final[int]
KEY_L4: Final[int]
KEY_L5: Final[int]
KEY_L6: Final[int]
KEY_L7: Final[int]
KEY_L8: Final[int]
KEY_L9: Final[int]
KEY_Lacute: Final[int]
KEY_Last_Virtual_Screen: Final[int]
KEY_Launch0: Final[int]
KEY_Launch1: Final[int]
KEY_Launch2: Final[int]
KEY_Launch3: Final[int]
KEY_Launch4: Final[int]
KEY_Launch5: Final[int]
KEY_Launch6: Final[int]
KEY_Launch7: Final[int]
KEY_Launch8: Final[int]
KEY_Launch9: Final[int]
KEY_LaunchA: Final[int]
KEY_LaunchB: Final[int]
KEY_LaunchC: Final[int]
KEY_LaunchD: Final[int]
KEY_LaunchE: Final[int]
KEY_LaunchF: Final[int]
KEY_Lbelowdot: Final[int]
KEY_Lcaron: Final[int]
KEY_Lcedilla: Final[int]
KEY_Left: Final[int]
KEY_LightBulb: Final[int]
KEY_Linefeed: Final[int]
KEY_LiraSign: Final[int]
KEY_LogGrabInfo: Final[int]
KEY_LogOff: Final[int]
KEY_LogWindowTree: Final[int]
KEY_Lstroke: Final[int]
KEY_M: Final[int]
KEY_Mabovedot: Final[int]
KEY_Macedonia_DSE: Final[int]
KEY_Macedonia_GJE: Final[int]
KEY_Macedonia_KJE: Final[int]
KEY_Macedonia_dse: Final[int]
KEY_Macedonia_gje: Final[int]
KEY_Macedonia_kje: Final[int]
KEY_Mae_Koho: Final[int]
KEY_Mail: Final[int]
KEY_MailForward: Final[int]
KEY_Market: Final[int]
KEY_Massyo: Final[int]
KEY_Meeting: Final[int]
KEY_Memo: Final[int]
KEY_Menu: Final[int]
KEY_MenuKB: Final[int]
KEY_MenuPB: Final[int]
KEY_Messenger: Final[int]
KEY_Meta_L: Final[int]
KEY_Meta_R: Final[int]
KEY_MillSign: Final[int]
KEY_ModeLock: Final[int]
KEY_Mode_switch: Final[int]
KEY_MonBrightnessDown: Final[int]
KEY_MonBrightnessUp: Final[int]
KEY_MouseKeys_Accel_Enable: Final[int]
KEY_MouseKeys_Enable: Final[int]
KEY_Muhenkan: Final[int]
KEY_Multi_key: Final[int]
KEY_MultipleCandidate: Final[int]
KEY_Music: Final[int]
KEY_MyComputer: Final[int]
KEY_MySites: Final[int]
KEY_N: Final[int]
KEY_Nacute: Final[int]
KEY_NairaSign: Final[int]
KEY_Ncaron: Final[int]
KEY_Ncedilla: Final[int]
KEY_New: Final[int]
KEY_NewSheqelSign: Final[int]
KEY_News: Final[int]
KEY_Next: Final[int]
KEY_Next_VMode: Final[int]
KEY_Next_Virtual_Screen: Final[int]
KEY_Ntilde: Final[int]
KEY_Num_Lock: Final[int]
KEY_O: Final[int]
KEY_OE: Final[int]
KEY_Oacute: Final[int]
KEY_Obarred: Final[int]
KEY_Obelowdot: Final[int]
KEY_Ocaron: Final[int]
KEY_Ocircumflex: Final[int]
KEY_Ocircumflexacute: Final[int]
KEY_Ocircumflexbelowdot: Final[int]
KEY_Ocircumflexgrave: Final[int]
KEY_Ocircumflexhook: Final[int]
KEY_Ocircumflextilde: Final[int]
KEY_Odiaeresis: Final[int]
KEY_Odoubleacute: Final[int]
KEY_OfficeHome: Final[int]
KEY_Ograve: Final[int]
KEY_Ohook: Final[int]
KEY_Ohorn: Final[int]
KEY_Ohornacute: Final[int]
KEY_Ohornbelowdot: Final[int]
KEY_Ohorngrave: Final[int]
KEY_Ohornhook: Final[int]
KEY_Ohorntilde: Final[int]
KEY_Omacron: Final[int]
KEY_Ooblique: Final[int]
KEY_Open: Final[int]
KEY_OpenURL: Final[int]
KEY_Option: Final[int]
KEY_Oslash: Final[int]
KEY_Otilde: Final[int]
KEY_Overlay1_Enable: Final[int]
KEY_Overlay2_Enable: Final[int]
KEY_P: Final[int]
KEY_Pabovedot: Final[int]
KEY_Page_Down: Final[int]
KEY_Page_Up: Final[int]
KEY_Paste: Final[int]
KEY_Pause: Final[int]
KEY_PesetaSign: Final[int]
KEY_Phone: Final[int]
KEY_Pictures: Final[int]
KEY_Pointer_Accelerate: Final[int]
KEY_Pointer_Button1: Final[int]
KEY_Pointer_Button2: Final[int]
KEY_Pointer_Button3: Final[int]
KEY_Pointer_Button4: Final[int]
KEY_Pointer_Button5: Final[int]
KEY_Pointer_Button_Dflt: Final[int]
KEY_Pointer_DblClick1: Final[int]
KEY_Pointer_DblClick2: Final[int]
KEY_Pointer_DblClick3: Final[int]
KEY_Pointer_DblClick4: Final[int]
KEY_Pointer_DblClick5: Final[int]
KEY_Pointer_DblClick_Dflt: Final[int]
KEY_Pointer_DfltBtnNext: Final[int]
KEY_Pointer_DfltBtnPrev: Final[int]
KEY_Pointer_Down: Final[int]
KEY_Pointer_DownLeft: Final[int]
KEY_Pointer_DownRight: Final[int]
KEY_Pointer_Drag1: Final[int]
KEY_Pointer_Drag2: Final[int]
KEY_Pointer_Drag3: Final[int]
KEY_Pointer_Drag4: Final[int]
KEY_Pointer_Drag5: Final[int]
KEY_Pointer_Drag_Dflt: Final[int]
KEY_Pointer_EnableKeys: Final[int]
KEY_Pointer_Left: Final[int]
KEY_Pointer_Right: Final[int]
KEY_Pointer_Up: Final[int]
KEY_Pointer_UpLeft: Final[int]
KEY_Pointer_UpRight: Final[int]
KEY_PowerDown: Final[int]
KEY_PowerOff: Final[int]
KEY_Prev_VMode: Final[int]
KEY_Prev_Virtual_Screen: Final[int]
KEY_PreviousCandidate: Final[int]
KEY_Print: Final[int]
KEY_Prior: Final[int]
KEY_Q: Final[int]
KEY_R: Final[int]
KEY_R1: Final[int]
KEY_R10: Final[int]
KEY_R11: Final[int]
KEY_R12: Final[int]
KEY_R13: Final[int]
KEY_R14: Final[int]
KEY_R15: Final[int]
KEY_R2: Final[int]
KEY_R3: Final[int]
KEY_R4: Final[int]
KEY_R5: Final[int]
KEY_R6: Final[int]
KEY_R7: Final[int]
KEY_R8: Final[int]
KEY_R9: Final[int]
KEY_RFKill: Final[int]
KEY_Racute: Final[int]
KEY_Rcaron: Final[int]
KEY_Rcedilla: Final[int]
KEY_Red: Final[int]
KEY_Redo: Final[int]
KEY_Refresh: Final[int]
KEY_Reload: Final[int]
KEY_RepeatKeys_Enable: Final[int]
KEY_Reply: Final[int]
KEY_Return: Final[int]
KEY_Right: Final[int]
KEY_RockerDown: Final[int]
KEY_RockerEnter: Final[int]
KEY_RockerUp: Final[int]
KEY_Romaji: Final[int]
KEY_RotateWindows: Final[int]
KEY_RotationKB: Final[int]
KEY_RotationPB: Final[int]
KEY_RupeeSign: Final[int]
KEY_S: Final[int]
KEY_SCHWA: Final[int]
KEY_Sabovedot: Final[int]
KEY_Sacute: Final[int]
KEY_Save: Final[int]
KEY_Scaron: Final[int]
KEY_Scedilla: Final[int]
KEY_Scircumflex: Final[int]
KEY_ScreenSaver: Final[int]
KEY_ScrollClick: Final[int]
KEY_ScrollDown: Final[int]
KEY_ScrollUp: Final[int]
KEY_Scroll_Lock: Final[int]
KEY_Search: Final[int]
KEY_Select: Final[int]
KEY_SelectButton: Final[int]
KEY_Send: Final[int]
KEY_Serbian_DJE: Final[int]
KEY_Serbian_DZE: Final[int]
KEY_Serbian_JE: Final[int]
KEY_Serbian_LJE: Final[int]
KEY_Serbian_NJE: Final[int]
KEY_Serbian_TSHE: Final[int]
KEY_Serbian_dje: Final[int]
KEY_Serbian_dze: Final[int]
KEY_Serbian_je: Final[int]
KEY_Serbian_lje: Final[int]
KEY_Serbian_nje: Final[int]
KEY_Serbian_tshe: Final[int]
KEY_Shift_L: Final[int]
KEY_Shift_Lock: Final[int]
KEY_Shift_R: Final[int]
KEY_Shop: Final[int]
KEY_SingleCandidate: Final[int]
KEY_Sinh_a: Final[int]
KEY_Sinh_aa: Final[int]
KEY_Sinh_aa2: Final[int]
KEY_Sinh_ae: Final[int]
KEY_Sinh_ae2: Final[int]
KEY_Sinh_aee: Final[int]
KEY_Sinh_aee2: Final[int]
KEY_Sinh_ai: Final[int]
KEY_Sinh_ai2: Final[int]
KEY_Sinh_al: Final[int]
KEY_Sinh_au: Final[int]
KEY_Sinh_au2: Final[int]
KEY_Sinh_ba: Final[int]
KEY_Sinh_bha: Final[int]
KEY_Sinh_ca: Final[int]
KEY_Sinh_cha: Final[int]
KEY_Sinh_dda: Final[int]
KEY_Sinh_ddha: Final[int]
KEY_Sinh_dha: Final[int]
KEY_Sinh_dhha: Final[int]
KEY_Sinh_e: Final[int]
KEY_Sinh_e2: Final[int]
KEY_Sinh_ee: Final[int]
KEY_Sinh_ee2: Final[int]
KEY_Sinh_fa: Final[int]
KEY_Sinh_ga: Final[int]
KEY_Sinh_gha: Final[int]
KEY_Sinh_h2: Final[int]
KEY_Sinh_ha: Final[int]
KEY_Sinh_i: Final[int]
KEY_Sinh_i2: Final[int]
KEY_Sinh_ii: Final[int]
KEY_Sinh_ii2: Final[int]
KEY_Sinh_ja: Final[int]
KEY_Sinh_jha: Final[int]
KEY_Sinh_jnya: Final[int]
KEY_Sinh_ka: Final[int]
KEY_Sinh_kha: Final[int]
KEY_Sinh_kunddaliya: Final[int]
KEY_Sinh_la: Final[int]
KEY_Sinh_lla: Final[int]
KEY_Sinh_lu: Final[int]
KEY_Sinh_lu2: Final[int]
KEY_Sinh_luu: Final[int]
KEY_Sinh_luu2: Final[int]
KEY_Sinh_ma: Final[int]
KEY_Sinh_mba: Final[int]
KEY_Sinh_na: Final[int]
KEY_Sinh_ndda: Final[int]
KEY_Sinh_ndha: Final[int]
KEY_Sinh_ng: Final[int]
KEY_Sinh_ng2: Final[int]
KEY_Sinh_nga: Final[int]
KEY_Sinh_nja: Final[int]
KEY_Sinh_nna: Final[int]
KEY_Sinh_nya: Final[int]
KEY_Sinh_o: Final[int]
KEY_Sinh_o2: Final[int]
KEY_Sinh_oo: Final[int]
KEY_Sinh_oo2: Final[int]
KEY_Sinh_pa: Final[int]
KEY_Sinh_pha: Final[int]
KEY_Sinh_ra: Final[int]
KEY_Sinh_ri: Final[int]
KEY_Sinh_rii: Final[int]
KEY_Sinh_ru2: Final[int]
KEY_Sinh_ruu2: Final[int]
KEY_Sinh_sa: Final[int]
KEY_Sinh_sha: Final[int]
KEY_Sinh_ssha: Final[int]
KEY_Sinh_tha: Final[int]
KEY_Sinh_thha: Final[int]
KEY_Sinh_tta: Final[int]
KEY_Sinh_ttha: Final[int]
KEY_Sinh_u: Final[int]
KEY_Sinh_u2: Final[int]
KEY_Sinh_uu: Final[int]
KEY_Sinh_uu2: Final[int]
KEY_Sinh_va: Final[int]
KEY_Sinh_ya: Final[int]
KEY_Sleep: Final[int]
KEY_SlowKeys_Enable: Final[int]
KEY_Spell: Final[int]
KEY_SplitScreen: Final[int]
KEY_Standby: Final[int]
KEY_Start: Final[int]
KEY_StickyKeys_Enable: Final[int]
KEY_Stop: Final[int]
KEY_Subtitle: Final[int]
KEY_Super_L: Final[int]
KEY_Super_R: Final[int]
KEY_Support: Final[int]
KEY_Suspend: Final[int]
KEY_Switch_VT_1: Final[int]
KEY_Switch_VT_10: Final[int]
KEY_Switch_VT_11: Final[int]
KEY_Switch_VT_12: Final[int]
KEY_Switch_VT_2: Final[int]
KEY_Switch_VT_3: Final[int]
KEY_Switch_VT_4: Final[int]
KEY_Switch_VT_5: Final[int]
KEY_Switch_VT_6: Final[int]
KEY_Switch_VT_7: Final[int]
KEY_Switch_VT_8: Final[int]
KEY_Switch_VT_9: Final[int]
KEY_Sys_Req: Final[int]
KEY_T: Final[int]
KEY_THORN: Final[int]
KEY_Tab: Final[int]
KEY_Tabovedot: Final[int]
KEY_TaskPane: Final[int]
KEY_Tcaron: Final[int]
KEY_Tcedilla: Final[int]
KEY_Terminal: Final[int]
KEY_Terminate_Server: Final[int]
KEY_Thai_baht: Final[int]
KEY_Thai_bobaimai: Final[int]
KEY_Thai_chochan: Final[int]
KEY_Thai_chochang: Final[int]
KEY_Thai_choching: Final[int]
KEY_Thai_chochoe: Final[int]
KEY_Thai_dochada: Final[int]
KEY_Thai_dodek: Final[int]
KEY_Thai_fofa: Final[int]
KEY_Thai_fofan: Final[int]
KEY_Thai_hohip: Final[int]
KEY_Thai_honokhuk: Final[int]
KEY_Thai_khokhai: Final[int]
KEY_Thai_khokhon: Final[int]
KEY_Thai_khokhuat: Final[int]
KEY_Thai_khokhwai: Final[int]
KEY_Thai_khorakhang: Final[int]
KEY_Thai_kokai: Final[int]
KEY_Thai_lakkhangyao: Final[int]
KEY_Thai_lekchet: Final[int]
KEY_Thai_lekha: Final[int]
KEY_Thai_lekhok: Final[int]
KEY_Thai_lekkao: Final[int]
KEY_Thai_leknung: Final[int]
KEY_Thai_lekpaet: Final[int]
KEY_Thai_leksam: Final[int]
KEY_Thai_leksi: Final[int]
KEY_Thai_leksong: Final[int]
KEY_Thai_leksun: Final[int]
KEY_Thai_lochula: Final[int]
KEY_Thai_loling: Final[int]
KEY_Thai_lu: Final[int]
KEY_Thai_maichattawa: Final[int]
KEY_Thai_maiek: Final[int]
KEY_Thai_maihanakat: Final[int]
KEY_Thai_maihanakat_maitho: Final[int]
KEY_Thai_maitaikhu: Final[int]
KEY_Thai_maitho: Final[int]
KEY_Thai_maitri: Final[int]
KEY_Thai_maiyamok: Final[int]
KEY_Thai_moma: Final[int]
KEY_Thai_ngongu: Final[int]
KEY_Thai_nikhahit: Final[int]
KEY_Thai_nonen: Final[int]
KEY_Thai_nonu: Final[int]
KEY_Thai_oang: Final[int]
KEY_Thai_paiyannoi: Final[int]
KEY_Thai_phinthu: Final[int]
KEY_Thai_phophan: Final[int]
KEY_Thai_phophung: Final[int]
KEY_Thai_phosamphao: Final[int]
KEY_Thai_popla: Final[int]
KEY_Thai_rorua: Final[int]
KEY_Thai_ru: Final[int]
KEY_Thai_saraa: Final[int]
KEY_Thai_saraaa: Final[int]
KEY_Thai_saraae: Final[int]
KEY_Thai_saraaimaimalai: Final[int]
KEY_Thai_saraaimaimuan: Final[int]
KEY_Thai_saraam: Final[int]
KEY_Thai_sarae: Final[int]
KEY_Thai_sarai: Final[int]
KEY_Thai_saraii: Final[int]
KEY_Thai_sarao: Final[int]
KEY_Thai_sarau: Final[int]
KEY_Thai_saraue: Final[int]
KEY_Thai_sarauee: Final[int]
KEY_Thai_sarauu: Final[int]
KEY_Thai_sorusi: Final[int]
KEY_Thai_sosala: Final[int]
KEY_Thai_soso: Final[int]
KEY_Thai_sosua: Final[int]
KEY_Thai_thanthakhat: Final[int]
KEY_Thai_thonangmontho: Final[int]
KEY_Thai_thophuthao: Final[int]
KEY_Thai_thothahan: Final[int]
KEY_Thai_thothan: Final[int]
KEY_Thai_thothong: Final[int]
KEY_Thai_thothung: Final[int]
KEY_Thai_topatak: Final[int]
KEY_Thai_totao: Final[int]
KEY_Thai_wowaen: Final[int]
KEY_Thai_yoyak: Final[int]
KEY_Thai_yoying: Final[int]
KEY_Thorn: Final[int]
KEY_Time: Final[int]
KEY_ToDoList: Final[int]
KEY_Tools: Final[int]
KEY_TopMenu: Final[int]
KEY_TouchpadOff: Final[int]
KEY_TouchpadOn: Final[int]
KEY_TouchpadToggle: Final[int]
KEY_Touroku: Final[int]
KEY_Travel: Final[int]
KEY_Tslash: Final[int]
KEY_U: Final[int]
KEY_UWB: Final[int]
KEY_Uacute: Final[int]
KEY_Ubelowdot: Final[int]
KEY_Ubreve: Final[int]
KEY_Ucircumflex: Final[int]
KEY_Udiaeresis: Final[int]
KEY_Udoubleacute: Final[int]
KEY_Ugrave: Final[int]
KEY_Uhook: Final[int]
KEY_Uhorn: Final[int]
KEY_Uhornacute: Final[int]
KEY_Uhornbelowdot: Final[int]
KEY_Uhorngrave: Final[int]
KEY_Uhornhook: Final[int]
KEY_Uhorntilde: Final[int]
KEY_Ukrainian_GHE_WITH_UPTURN: Final[int]
KEY_Ukrainian_I: Final[int]
KEY_Ukrainian_IE: Final[int]
KEY_Ukrainian_YI: Final[int]
KEY_Ukrainian_ghe_with_upturn: Final[int]
KEY_Ukrainian_i: Final[int]
KEY_Ukrainian_ie: Final[int]
KEY_Ukrainian_yi: Final[int]
KEY_Ukranian_I: Final[int]
KEY_Ukranian_JE: Final[int]
KEY_Ukranian_YI: Final[int]
KEY_Ukranian_i: Final[int]
KEY_Ukranian_je: Final[int]
KEY_Ukranian_yi: Final[int]
KEY_Umacron: Final[int]
KEY_Undo: Final[int]
KEY_Ungrab: Final[int]
KEY_Uogonek: Final[int]
KEY_Up: Final[int]
KEY_Uring: Final[int]
KEY_User1KB: Final[int]
KEY_User2KB: Final[int]
KEY_UserPB: Final[int]
KEY_Utilde: Final[int]
KEY_V: Final[int]
KEY_VendorHome: Final[int]
KEY_Video: Final[int]
KEY_View: Final[int]
KEY_VoidSymbol: Final[int]
KEY_W: Final[int]
KEY_WLAN: Final[int]
KEY_WWAN: Final[int]
KEY_WWW: Final[int]
KEY_Wacute: Final[int]
KEY_WakeUp: Final[int]
KEY_Wcircumflex: Final[int]
KEY_Wdiaeresis: Final[int]
KEY_WebCam: Final[int]
KEY_Wgrave: Final[int]
KEY_WheelButton: Final[int]
KEY_WindowClear: Final[int]
KEY_WonSign: Final[int]
KEY_Word: Final[int]
KEY_X: Final[int]
KEY_Xabovedot: Final[int]
KEY_Xfer: Final[int]
KEY_Y: Final[int]
KEY_Yacute: Final[int]
KEY_Ybelowdot: Final[int]
KEY_Ycircumflex: Final[int]
KEY_Ydiaeresis: Final[int]
KEY_Yellow: Final[int]
KEY_Ygrave: Final[int]
KEY_Yhook: Final[int]
KEY_Ytilde: Final[int]
KEY_Z: Final[int]
KEY_Zabovedot: Final[int]
KEY_Zacute: Final[int]
KEY_Zcaron: Final[int]
KEY_Zen_Koho: Final[int]
KEY_Zenkaku: Final[int]
KEY_Zenkaku_Hankaku: Final[int]
KEY_ZoomIn: Final[int]
KEY_ZoomOut: Final[int]
KEY_Zstroke: Final[int]
KEY_a: Final[int]
KEY_aacute: Final[int]
KEY_abelowdot: Final[int]
KEY_abovedot: Final[int]
KEY_abreve: Final[int]
KEY_abreveacute: Final[int]
KEY_abrevebelowdot: Final[int]
KEY_abrevegrave: Final[int]
KEY_abrevehook: Final[int]
KEY_abrevetilde: Final[int]
KEY_acircumflex: Final[int]
KEY_acircumflexacute: Final[int]
KEY_acircumflexbelowdot: Final[int]
KEY_acircumflexgrave: Final[int]
KEY_acircumflexhook: Final[int]
KEY_acircumflextilde: Final[int]
KEY_acute: Final[int]
KEY_adiaeresis: Final[int]
KEY_ae: Final[int]
KEY_agrave: Final[int]
KEY_ahook: Final[int]
KEY_amacron: Final[int]
KEY_ampersand: Final[int]
KEY_aogonek: Final[int]
KEY_apostrophe: Final[int]
KEY_approxeq: Final[int]
KEY_approximate: Final[int]
KEY_aring: Final[int]
KEY_asciicircum: Final[int]
KEY_asciitilde: Final[int]
KEY_asterisk: Final[int]
KEY_at: Final[int]
KEY_atilde: Final[int]
KEY_b: Final[int]
KEY_babovedot: Final[int]
KEY_backslash: Final[int]
KEY_ballotcross: Final[int]
KEY_bar: Final[int]
KEY_because: Final[int]
KEY_blank: Final[int]
KEY_botintegral: Final[int]
KEY_botleftparens: Final[int]
KEY_botleftsqbracket: Final[int]
KEY_botleftsummation: Final[int]
KEY_botrightparens: Final[int]
KEY_botrightsqbracket: Final[int]
KEY_botrightsummation: Final[int]
KEY_bott: Final[int]
KEY_botvertsummationconnector: Final[int]
KEY_braceleft: Final[int]
KEY_braceright: Final[int]
KEY_bracketleft: Final[int]
KEY_bracketright: Final[int]
KEY_braille_blank: Final[int]
KEY_braille_dot_1: Final[int]
KEY_braille_dot_10: Final[int]
KEY_braille_dot_2: Final[int]
KEY_braille_dot_3: Final[int]
KEY_braille_dot_4: Final[int]
KEY_braille_dot_5: Final[int]
KEY_braille_dot_6: Final[int]
KEY_braille_dot_7: Final[int]
KEY_braille_dot_8: Final[int]
KEY_braille_dot_9: Final[int]
KEY_braille_dots_1: Final[int]
KEY_braille_dots_12: Final[int]
KEY_braille_dots_123: Final[int]
KEY_braille_dots_1234: Final[int]
KEY_braille_dots_12345: Final[int]
KEY_braille_dots_123456: Final[int]
KEY_braille_dots_1234567: Final[int]
KEY_braille_dots_12345678: Final[int]
KEY_braille_dots_1234568: Final[int]
KEY_braille_dots_123457: Final[int]
KEY_braille_dots_1234578: Final[int]
KEY_braille_dots_123458: Final[int]
KEY_braille_dots_12346: Final[int]
KEY_braille_dots_123467: Final[int]
KEY_braille_dots_1234678: Final[int]
KEY_braille_dots_123468: Final[int]
KEY_braille_dots_12347: Final[int]
KEY_braille_dots_123478: Final[int]
KEY_braille_dots_12348: Final[int]
KEY_braille_dots_1235: Final[int]
KEY_braille_dots_12356: Final[int]
KEY_braille_dots_123567: Final[int]
KEY_braille_dots_1235678: Final[int]
KEY_braille_dots_123568: Final[int]
KEY_braille_dots_12357: Final[int]
KEY_braille_dots_123578: Final[int]
KEY_braille_dots_12358: Final[int]
KEY_braille_dots_1236: Final[int]
KEY_braille_dots_12367: Final[int]
KEY_braille_dots_123678: Final[int]
KEY_braille_dots_12368: Final[int]
KEY_braille_dots_1237: Final[int]
KEY_braille_dots_12378: Final[int]
KEY_braille_dots_1238: Final[int]
KEY_braille_dots_124: Final[int]
KEY_braille_dots_1245: Final[int]
KEY_braille_dots_12456: Final[int]
KEY_braille_dots_124567: Final[int]
KEY_braille_dots_1245678: Final[int]
KEY_braille_dots_124568: Final[int]
KEY_braille_dots_12457: Final[int]
KEY_braille_dots_124578: Final[int]
KEY_braille_dots_12458: Final[int]
KEY_braille_dots_1246: Final[int]
KEY_braille_dots_12467: Final[int]
KEY_braille_dots_124678: Final[int]
KEY_braille_dots_12468: Final[int]
KEY_braille_dots_1247: Final[int]
KEY_braille_dots_12478: Final[int]
KEY_braille_dots_1248: Final[int]
KEY_braille_dots_125: Final[int]
KEY_braille_dots_1256: Final[int]
KEY_braille_dots_12567: Final[int]
KEY_braille_dots_125678: Final[int]
KEY_braille_dots_12568: Final[int]
KEY_braille_dots_1257: Final[int]
KEY_braille_dots_12578: Final[int]
KEY_braille_dots_1258: Final[int]
KEY_braille_dots_126: Final[int]
KEY_braille_dots_1267: Final[int]
KEY_braille_dots_12678: Final[int]
KEY_braille_dots_1268: Final[int]
KEY_braille_dots_127: Final[int]
KEY_braille_dots_1278: Final[int]
KEY_braille_dots_128: Final[int]
KEY_braille_dots_13: Final[int]
KEY_braille_dots_134: Final[int]
KEY_braille_dots_1345: Final[int]
KEY_braille_dots_13456: Final[int]
KEY_braille_dots_134567: Final[int]
KEY_braille_dots_1345678: Final[int]
KEY_braille_dots_134568: Final[int]
KEY_braille_dots_13457: Final[int]
KEY_braille_dots_134578: Final[int]
KEY_braille_dots_13458: Final[int]
KEY_braille_dots_1346: Final[int]
KEY_braille_dots_13467: Final[int]
KEY_braille_dots_134678: Final[int]
KEY_braille_dots_13468: Final[int]
KEY_braille_dots_1347: Final[int]
KEY_braille_dots_13478: Final[int]
KEY_braille_dots_1348: Final[int]
KEY_braille_dots_135: Final[int]
KEY_braille_dots_1356: Final[int]
KEY_braille_dots_13567: Final[int]
KEY_braille_dots_135678: Final[int]
KEY_braille_dots_13568: Final[int]
KEY_braille_dots_1357: Final[int]
KEY_braille_dots_13578: Final[int]
KEY_braille_dots_1358: Final[int]
KEY_braille_dots_136: Final[int]
KEY_braille_dots_1367: Final[int]
KEY_braille_dots_13678: Final[int]
KEY_braille_dots_1368: Final[int]
KEY_braille_dots_137: Final[int]
KEY_braille_dots_1378: Final[int]
KEY_braille_dots_138: Final[int]
KEY_braille_dots_14: Final[int]
KEY_braille_dots_145: Final[int]
KEY_braille_dots_1456: Final[int]
KEY_braille_dots_14567: Final[int]
KEY_braille_dots_145678: Final[int]
KEY_braille_dots_14568: Final[int]
KEY_braille_dots_1457: Final[int]
KEY_braille_dots_14578: Final[int]
KEY_braille_dots_1458: Final[int]
KEY_braille_dots_146: Final[int]
KEY_braille_dots_1467: Final[int]
KEY_braille_dots_14678: Final[int]
KEY_braille_dots_1468: Final[int]
KEY_braille_dots_147: Final[int]
KEY_braille_dots_1478: Final[int]
KEY_braille_dots_148: Final[int]
KEY_braille_dots_15: Final[int]
KEY_braille_dots_156: Final[int]
KEY_braille_dots_1567: Final[int]
KEY_braille_dots_15678: Final[int]
KEY_braille_dots_1568: Final[int]
KEY_braille_dots_157: Final[int]
KEY_braille_dots_1578: Final[int]
KEY_braille_dots_158: Final[int]
KEY_braille_dots_16: Final[int]
KEY_braille_dots_167: Final[int]
KEY_braille_dots_1678: Final[int]
KEY_braille_dots_168: Final[int]
KEY_braille_dots_17: Final[int]
KEY_braille_dots_178: Final[int]
KEY_braille_dots_18: Final[int]
KEY_braille_dots_2: Final[int]
KEY_braille_dots_23: Final[int]
KEY_braille_dots_234: Final[int]
KEY_braille_dots_2345: Final[int]
KEY_braille_dots_23456: Final[int]
KEY_braille_dots_234567: Final[int]
KEY_braille_dots_2345678: Final[int]
KEY_braille_dots_234568: Final[int]
KEY_braille_dots_23457: Final[int]
KEY_braille_dots_234578: Final[int]
KEY_braille_dots_23458: Final[int]
KEY_braille_dots_2346: Final[int]
KEY_braille_dots_23467: Final[int]
KEY_braille_dots_234678: Final[int]
KEY_braille_dots_23468: Final[int]
KEY_braille_dots_2347: Final[int]
KEY_braille_dots_23478: Final[int]
KEY_braille_dots_2348: Final[int]
KEY_braille_dots_235: Final[int]
KEY_braille_dots_2356: Final[int]
KEY_braille_dots_23567: Final[int]
KEY_braille_dots_235678: Final[int]
KEY_braille_dots_23568: Final[int]
KEY_braille_dots_2357: Final[int]
KEY_braille_dots_23578: Final[int]
KEY_braille_dots_2358: Final[int]
KEY_braille_dots_236: Final[int]
KEY_braille_dots_2367: Final[int]
KEY_braille_dots_23678: Final[int]
KEY_braille_dots_2368: Final[int]
KEY_braille_dots_237: Final[int]
KEY_braille_dots_2378: Final[int]
KEY_braille_dots_238: Final[int]
KEY_braille_dots_24: Final[int]
KEY_braille_dots_245: Final[int]
KEY_braille_dots_2456: Final[int]
KEY_braille_dots_24567: Final[int]
KEY_braille_dots_245678: Final[int]
KEY_braille_dots_24568: Final[int]
KEY_braille_dots_2457: Final[int]
KEY_braille_dots_24578: Final[int]
KEY_braille_dots_2458: Final[int]
KEY_braille_dots_246: Final[int]
KEY_braille_dots_2467: Final[int]
KEY_braille_dots_24678: Final[int]
KEY_braille_dots_2468: Final[int]
KEY_braille_dots_247: Final[int]
KEY_braille_dots_2478: Final[int]
KEY_braille_dots_248: Final[int]
KEY_braille_dots_25: Final[int]
KEY_braille_dots_256: Final[int]
KEY_braille_dots_2567: Final[int]
KEY_braille_dots_25678: Final[int]
KEY_braille_dots_2568: Final[int]
KEY_braille_dots_257: Final[int]
KEY_braille_dots_2578: Final[int]
KEY_braille_dots_258: Final[int]
KEY_braille_dots_26: Final[int]
KEY_braille_dots_267: Final[int]
KEY_braille_dots_2678: Final[int]
KEY_braille_dots_268: Final[int]
KEY_braille_dots_27: Final[int]
KEY_braille_dots_278: Final[int]
KEY_braille_dots_28: Final[int]
KEY_braille_dots_3: Final[int]
KEY_braille_dots_34: Final[int]
KEY_braille_dots_345: Final[int]
KEY_braille_dots_3456: Final[int]
KEY_braille_dots_34567: Final[int]
KEY_braille_dots_345678: Final[int]
KEY_braille_dots_34568: Final[int]
KEY_braille_dots_3457: Final[int]
KEY_braille_dots_34578: Final[int]
KEY_braille_dots_3458: Final[int]
KEY_braille_dots_346: Final[int]
KEY_braille_dots_3467: Final[int]
KEY_braille_dots_34678: Final[int]
KEY_braille_dots_3468: Final[int]
KEY_braille_dots_347: Final[int]
KEY_braille_dots_3478: Final[int]
KEY_braille_dots_348: Final[int]
KEY_braille_dots_35: Final[int]
KEY_braille_dots_356: Final[int]
KEY_braille_dots_3567: Final[int]
KEY_braille_dots_35678: Final[int]
KEY_braille_dots_3568: Final[int]
KEY_braille_dots_357: Final[int]
KEY_braille_dots_3578: Final[int]
KEY_braille_dots_358: Final[int]
KEY_braille_dots_36: Final[int]
KEY_braille_dots_367: Final[int]
KEY_braille_dots_3678: Final[int]
KEY_braille_dots_368: Final[int]
KEY_braille_dots_37: Final[int]
KEY_braille_dots_378: Final[int]
KEY_braille_dots_38: Final[int]
KEY_braille_dots_4: Final[int]
KEY_braille_dots_45: Final[int]
KEY_braille_dots_456: Final[int]
KEY_braille_dots_4567: Final[int]
KEY_braille_dots_45678: Final[int]
KEY_braille_dots_4568: Final[int]
KEY_braille_dots_457: Final[int]
KEY_braille_dots_4578: Final[int]
KEY_braille_dots_458: Final[int]
KEY_braille_dots_46: Final[int]
KEY_braille_dots_467: Final[int]
KEY_braille_dots_4678: Final[int]
KEY_braille_dots_468: Final[int]
KEY_braille_dots_47: Final[int]
KEY_braille_dots_478: Final[int]
KEY_braille_dots_48: Final[int]
KEY_braille_dots_5: Final[int]
KEY_braille_dots_56: Final[int]
KEY_braille_dots_567: Final[int]
KEY_braille_dots_5678: Final[int]
KEY_braille_dots_568: Final[int]
KEY_braille_dots_57: Final[int]
KEY_braille_dots_578: Final[int]
KEY_braille_dots_58: Final[int]
KEY_braille_dots_6: Final[int]
KEY_braille_dots_67: Final[int]
KEY_braille_dots_678: Final[int]
KEY_braille_dots_68: Final[int]
KEY_braille_dots_7: Final[int]
KEY_braille_dots_78: Final[int]
KEY_braille_dots_8: Final[int]
KEY_breve: Final[int]
KEY_brokenbar: Final[int]
KEY_c: Final[int]
KEY_c_h: Final[int]
KEY_cabovedot: Final[int]
KEY_cacute: Final[int]
KEY_careof: Final[int]
KEY_caret: Final[int]
KEY_caron: Final[int]
KEY_ccaron: Final[int]
KEY_ccedilla: Final[int]
KEY_ccircumflex: Final[int]
KEY_cedilla: Final[int]
KEY_cent: Final[int]
KEY_ch: Final[int]
KEY_checkerboard: Final[int]
KEY_checkmark: Final[int]
KEY_circle: Final[int]
KEY_club: Final[int]
KEY_colon: Final[int]
KEY_comma: Final[int]
KEY_containsas: Final[int]
KEY_copyright: Final[int]
KEY_cr: Final[int]
KEY_crossinglines: Final[int]
KEY_cuberoot: Final[int]
KEY_currency: Final[int]
KEY_cursor: Final[int]
KEY_d: Final[int]
KEY_dabovedot: Final[int]
KEY_dagger: Final[int]
KEY_dcaron: Final[int]
KEY_dead_A: Final[int]
KEY_dead_E: Final[int]
KEY_dead_I: Final[int]
KEY_dead_O: Final[int]
KEY_dead_U: Final[int]
KEY_dead_a: Final[int]
KEY_dead_abovecomma: Final[int]
KEY_dead_abovedot: Final[int]
KEY_dead_abovereversedcomma: Final[int]
KEY_dead_abovering: Final[int]
KEY_dead_aboveverticalline: Final[int]
KEY_dead_acute: Final[int]
KEY_dead_belowbreve: Final[int]
KEY_dead_belowcircumflex: Final[int]
KEY_dead_belowcomma: Final[int]
KEY_dead_belowdiaeresis: Final[int]
KEY_dead_belowdot: Final[int]
KEY_dead_belowmacron: Final[int]
KEY_dead_belowring: Final[int]
KEY_dead_belowtilde: Final[int]
KEY_dead_belowverticalline: Final[int]
KEY_dead_breve: Final[int]
KEY_dead_capital_schwa: Final[int]
KEY_dead_caron: Final[int]
KEY_dead_cedilla: Final[int]
KEY_dead_circumflex: Final[int]
KEY_dead_currency: Final[int]
KEY_dead_dasia: Final[int]
KEY_dead_diaeresis: Final[int]
KEY_dead_doubleacute: Final[int]
KEY_dead_doublegrave: Final[int]
KEY_dead_e: Final[int]
KEY_dead_grave: Final[int]
KEY_dead_greek: Final[int]
KEY_dead_hook: Final[int]
KEY_dead_horn: Final[int]
KEY_dead_i: Final[int]
KEY_dead_invertedbreve: Final[int]
KEY_dead_iota: Final[int]
KEY_dead_longsolidusoverlay: Final[int]
KEY_dead_lowline: Final[int]
KEY_dead_macron: Final[int]
KEY_dead_o: Final[int]
KEY_dead_ogonek: Final[int]
KEY_dead_perispomeni: Final[int]
KEY_dead_psili: Final[int]
KEY_dead_semivoiced_sound: Final[int]
KEY_dead_small_schwa: Final[int]
KEY_dead_stroke: Final[int]
KEY_dead_tilde: Final[int]
KEY_dead_u: Final[int]
KEY_dead_voiced_sound: Final[int]
KEY_decimalpoint: Final[int]
KEY_degree: Final[int]
KEY_diaeresis: Final[int]
KEY_diamond: Final[int]
KEY_digitspace: Final[int]
KEY_dintegral: Final[int]
KEY_division: Final[int]
KEY_dollar: Final[int]
KEY_doubbaselinedot: Final[int]
KEY_doubleacute: Final[int]
KEY_doubledagger: Final[int]
KEY_doublelowquotemark: Final[int]
KEY_downarrow: Final[int]
KEY_downcaret: Final[int]
KEY_downshoe: Final[int]
KEY_downstile: Final[int]
KEY_downtack: Final[int]
KEY_dstroke: Final[int]
KEY_e: Final[int]
KEY_eabovedot: Final[int]
KEY_eacute: Final[int]
KEY_ebelowdot: Final[int]
KEY_ecaron: Final[int]
KEY_ecircumflex: Final[int]
KEY_ecircumflexacute: Final[int]
KEY_ecircumflexbelowdot: Final[int]
KEY_ecircumflexgrave: Final[int]
KEY_ecircumflexhook: Final[int]
KEY_ecircumflextilde: Final[int]
KEY_ediaeresis: Final[int]
KEY_egrave: Final[int]
KEY_ehook: Final[int]
KEY_eightsubscript: Final[int]
KEY_eightsuperior: Final[int]
KEY_elementof: Final[int]
KEY_ellipsis: Final[int]
KEY_em3space: Final[int]
KEY_em4space: Final[int]
KEY_emacron: Final[int]
KEY_emdash: Final[int]
KEY_emfilledcircle: Final[int]
KEY_emfilledrect: Final[int]
KEY_emopencircle: Final[int]
KEY_emopenrectangle: Final[int]
KEY_emptyset: Final[int]
KEY_emspace: Final[int]
KEY_endash: Final[int]
KEY_enfilledcircbullet: Final[int]
KEY_enfilledsqbullet: Final[int]
KEY_eng: Final[int]
KEY_enopencircbullet: Final[int]
KEY_enopensquarebullet: Final[int]
KEY_enspace: Final[int]
KEY_eogonek: Final[int]
KEY_equal: Final[int]
KEY_eth: Final[int]
KEY_etilde: Final[int]
KEY_exclam: Final[int]
KEY_exclamdown: Final[int]
KEY_ezh: Final[int]
KEY_f: Final[int]
KEY_fabovedot: Final[int]
KEY_femalesymbol: Final[int]
KEY_ff: Final[int]
KEY_figdash: Final[int]
KEY_filledlefttribullet: Final[int]
KEY_filledrectbullet: Final[int]
KEY_filledrighttribullet: Final[int]
KEY_filledtribulletdown: Final[int]
KEY_filledtribulletup: Final[int]
KEY_fiveeighths: Final[int]
KEY_fivesixths: Final[int]
KEY_fivesubscript: Final[int]
KEY_fivesuperior: Final[int]
KEY_fourfifths: Final[int]
KEY_foursubscript: Final[int]
KEY_foursuperior: Final[int]
KEY_fourthroot: Final[int]
KEY_function: Final[int]
KEY_g: Final[int]
KEY_gabovedot: Final[int]
KEY_gbreve: Final[int]
KEY_gcaron: Final[int]
KEY_gcedilla: Final[int]
KEY_gcircumflex: Final[int]
KEY_grave: Final[int]
KEY_greater: Final[int]
KEY_greaterthanequal: Final[int]
KEY_guillemotleft: Final[int]
KEY_guillemotright: Final[int]
KEY_h: Final[int]
KEY_hairspace: Final[int]
KEY_hcircumflex: Final[int]
KEY_heart: Final[int]
KEY_hebrew_aleph: Final[int]
KEY_hebrew_ayin: Final[int]
KEY_hebrew_bet: Final[int]
KEY_hebrew_beth: Final[int]
KEY_hebrew_chet: Final[int]
KEY_hebrew_dalet: Final[int]
KEY_hebrew_daleth: Final[int]
KEY_hebrew_doublelowline: Final[int]
KEY_hebrew_finalkaph: Final[int]
KEY_hebrew_finalmem: Final[int]
KEY_hebrew_finalnun: Final[int]
KEY_hebrew_finalpe: Final[int]
KEY_hebrew_finalzade: Final[int]
KEY_hebrew_finalzadi: Final[int]
KEY_hebrew_gimel: Final[int]
KEY_hebrew_gimmel: Final[int]
KEY_hebrew_he: Final[int]
KEY_hebrew_het: Final[int]
KEY_hebrew_kaph: Final[int]
KEY_hebrew_kuf: Final[int]
KEY_hebrew_lamed: Final[int]
KEY_hebrew_mem: Final[int]
KEY_hebrew_nun: Final[int]
KEY_hebrew_pe: Final[int]
KEY_hebrew_qoph: Final[int]
KEY_hebrew_resh: Final[int]
KEY_hebrew_samech: Final[int]
KEY_hebrew_samekh: Final[int]
KEY_hebrew_shin: Final[int]
KEY_hebrew_taf: Final[int]
KEY_hebrew_taw: Final[int]
KEY_hebrew_tet: Final[int]
KEY_hebrew_teth: Final[int]
KEY_hebrew_waw: Final[int]
KEY_hebrew_yod: Final[int]
KEY_hebrew_zade: Final[int]
KEY_hebrew_zadi: Final[int]
KEY_hebrew_zain: Final[int]
KEY_hebrew_zayin: Final[int]
KEY_hexagram: Final[int]
KEY_horizconnector: Final[int]
KEY_horizlinescan1: Final[int]
KEY_horizlinescan3: Final[int]
KEY_horizlinescan5: Final[int]
KEY_horizlinescan7: Final[int]
KEY_horizlinescan9: Final[int]
KEY_hstroke: Final[int]
KEY_ht: Final[int]
KEY_hyphen: Final[int]
KEY_i: Final[int]
KEY_iTouch: Final[int]
KEY_iacute: Final[int]
KEY_ibelowdot: Final[int]
KEY_ibreve: Final[int]
KEY_icircumflex: Final[int]
KEY_identical: Final[int]
KEY_idiaeresis: Final[int]
KEY_idotless: Final[int]
KEY_ifonlyif: Final[int]
KEY_igrave: Final[int]
KEY_ihook: Final[int]
KEY_imacron: Final[int]
KEY_implies: Final[int]
KEY_includedin: Final[int]
KEY_includes: Final[int]
KEY_infinity: Final[int]
KEY_integral: Final[int]
KEY_intersection: Final[int]
KEY_iogonek: Final[int]
KEY_itilde: Final[int]
KEY_j: Final[int]
KEY_jcircumflex: Final[int]
KEY_jot: Final[int]
KEY_k: Final[int]
KEY_kana_A: Final[int]
KEY_kana_CHI: Final[int]
KEY_kana_E: Final[int]
KEY_kana_FU: Final[int]
KEY_kana_HA: Final[int]
KEY_kana_HE: Final[int]
KEY_kana_HI: Final[int]
KEY_kana_HO: Final[int]
KEY_kana_HU: Final[int]
KEY_kana_I: Final[int]
KEY_kana_KA: Final[int]
KEY_kana_KE: Final[int]
KEY_kana_KI: Final[int]
KEY_kana_KO: Final[int]
KEY_kana_KU: Final[int]
KEY_kana_MA: Final[int]
KEY_kana_ME: Final[int]
KEY_kana_MI: Final[int]
KEY_kana_MO: Final[int]
KEY_kana_MU: Final[int]
KEY_kana_N: Final[int]
KEY_kana_NA: Final[int]
KEY_kana_NE: Final[int]
KEY_kana_NI: Final[int]
KEY_kana_NO: Final[int]
KEY_kana_NU: Final[int]
KEY_kana_O: Final[int]
KEY_kana_RA: Final[int]
KEY_kana_RE: Final[int]
KEY_kana_RI: Final[int]
KEY_kana_RO: Final[int]
KEY_kana_RU: Final[int]
KEY_kana_SA: Final[int]
KEY_kana_SE: Final[int]
KEY_kana_SHI: Final[int]
KEY_kana_SO: Final[int]
KEY_kana_SU: Final[int]
KEY_kana_TA: Final[int]
KEY_kana_TE: Final[int]
KEY_kana_TI: Final[int]
KEY_kana_TO: Final[int]
KEY_kana_TSU: Final[int]
KEY_kana_TU: Final[int]
KEY_kana_U: Final[int]
KEY_kana_WA: Final[int]
KEY_kana_WO: Final[int]
KEY_kana_YA: Final[int]
KEY_kana_YO: Final[int]
KEY_kana_YU: Final[int]
KEY_kana_a: Final[int]
KEY_kana_closingbracket: Final[int]
KEY_kana_comma: Final[int]
KEY_kana_conjunctive: Final[int]
KEY_kana_e: Final[int]
KEY_kana_fullstop: Final[int]
KEY_kana_i: Final[int]
KEY_kana_middledot: Final[int]
KEY_kana_o: Final[int]
KEY_kana_openingbracket: Final[int]
KEY_kana_switch: Final[int]
KEY_kana_tsu: Final[int]
KEY_kana_tu: Final[int]
KEY_kana_u: Final[int]
KEY_kana_ya: Final[int]
KEY_kana_yo: Final[int]
KEY_kana_yu: Final[int]
KEY_kappa: Final[int]
KEY_kcedilla: Final[int]
KEY_kra: Final[int]
KEY_l: Final[int]
KEY_lacute: Final[int]
KEY_latincross: Final[int]
KEY_lbelowdot: Final[int]
KEY_lcaron: Final[int]
KEY_lcedilla: Final[int]
KEY_leftanglebracket: Final[int]
KEY_leftarrow: Final[int]
KEY_leftcaret: Final[int]
KEY_leftdoublequotemark: Final[int]
KEY_leftmiddlecurlybrace: Final[int]
KEY_leftopentriangle: Final[int]
KEY_leftpointer: Final[int]
KEY_leftradical: Final[int]
KEY_leftshoe: Final[int]
KEY_leftsinglequotemark: Final[int]
KEY_leftt: Final[int]
KEY_lefttack: Final[int]
KEY_less: Final[int]
KEY_lessthanequal: Final[int]
KEY_lf: Final[int]
KEY_logicaland: Final[int]
KEY_logicalor: Final[int]
KEY_lowleftcorner: Final[int]
KEY_lowrightcorner: Final[int]
KEY_lstroke: Final[int]
KEY_m: Final[int]
KEY_mabovedot: Final[int]
KEY_macron: Final[int]
KEY_malesymbol: Final[int]
KEY_maltesecross: Final[int]
KEY_marker: Final[int]
KEY_masculine: Final[int]
KEY_minus: Final[int]
KEY_minutes: Final[int]
KEY_mu: Final[int]
KEY_multiply: Final[int]
KEY_musicalflat: Final[int]
KEY_musicalsharp: Final[int]
KEY_n: Final[int]
KEY_nabla: Final[int]
KEY_nacute: Final[int]
KEY_ncaron: Final[int]
KEY_ncedilla: Final[int]
KEY_ninesubscript: Final[int]
KEY_ninesuperior: Final[int]
KEY_nl: Final[int]
KEY_nobreakspace: Final[int]
KEY_notapproxeq: Final[int]
KEY_notelementof: Final[int]
KEY_notequal: Final[int]
KEY_notidentical: Final[int]
KEY_notsign: Final[int]
KEY_ntilde: Final[int]
KEY_numbersign: Final[int]
KEY_numerosign: Final[int]
KEY_o: Final[int]
KEY_oacute: Final[int]
KEY_obarred: Final[int]
KEY_obelowdot: Final[int]
KEY_ocaron: Final[int]
KEY_ocircumflex: Final[int]
KEY_ocircumflexacute: Final[int]
KEY_ocircumflexbelowdot: Final[int]
KEY_ocircumflexgrave: Final[int]
KEY_ocircumflexhook: Final[int]
KEY_ocircumflextilde: Final[int]
KEY_odiaeresis: Final[int]
KEY_odoubleacute: Final[int]
KEY_oe: Final[int]
KEY_ogonek: Final[int]
KEY_ograve: Final[int]
KEY_ohook: Final[int]
KEY_ohorn: Final[int]
KEY_ohornacute: Final[int]
KEY_ohornbelowdot: Final[int]
KEY_ohorngrave: Final[int]
KEY_ohornhook: Final[int]
KEY_ohorntilde: Final[int]
KEY_omacron: Final[int]
KEY_oneeighth: Final[int]
KEY_onefifth: Final[int]
KEY_onehalf: Final[int]
KEY_onequarter: Final[int]
KEY_onesixth: Final[int]
KEY_onesubscript: Final[int]
KEY_onesuperior: Final[int]
KEY_onethird: Final[int]
KEY_ooblique: Final[int]
KEY_openrectbullet: Final[int]
KEY_openstar: Final[int]
KEY_opentribulletdown: Final[int]
KEY_opentribulletup: Final[int]
KEY_ordfeminine: Final[int]
KEY_oslash: Final[int]
KEY_otilde: Final[int]
KEY_overbar: Final[int]
KEY_overline: Final[int]
KEY_p: Final[int]
KEY_pabovedot: Final[int]
KEY_paragraph: Final[int]
KEY_parenleft: Final[int]
KEY_parenright: Final[int]
KEY_partdifferential: Final[int]
KEY_partialderivative: Final[int]
KEY_percent: Final[int]
KEY_period: Final[int]
KEY_periodcentered: Final[int]
KEY_permille: Final[int]
KEY_phonographcopyright: Final[int]
KEY_plus: Final[int]
KEY_plusminus: Final[int]
KEY_prescription: Final[int]
KEY_prolongedsound: Final[int]
KEY_punctspace: Final[int]
KEY_q: Final[int]
KEY_quad: Final[int]
KEY_question: Final[int]
KEY_questiondown: Final[int]
KEY_quotedbl: Final[int]
KEY_quoteleft: Final[int]
KEY_quoteright: Final[int]
KEY_r: Final[int]
KEY_racute: Final[int]
KEY_radical: Final[int]
KEY_rcaron: Final[int]
KEY_rcedilla: Final[int]
KEY_registered: Final[int]
KEY_rightanglebracket: Final[int]
KEY_rightarrow: Final[int]
KEY_rightcaret: Final[int]
KEY_rightdoublequotemark: Final[int]
KEY_rightmiddlecurlybrace: Final[int]
KEY_rightmiddlesummation: Final[int]
KEY_rightopentriangle: Final[int]
KEY_rightpointer: Final[int]
KEY_rightshoe: Final[int]
KEY_rightsinglequotemark: Final[int]
KEY_rightt: Final[int]
KEY_righttack: Final[int]
KEY_s: Final[int]
KEY_sabovedot: Final[int]
KEY_sacute: Final[int]
KEY_scaron: Final[int]
KEY_scedilla: Final[int]
KEY_schwa: Final[int]
KEY_scircumflex: Final[int]
KEY_script_switch: Final[int]
KEY_seconds: Final[int]
KEY_section: Final[int]
KEY_semicolon: Final[int]
KEY_semivoicedsound: Final[int]
KEY_seveneighths: Final[int]
KEY_sevensubscript: Final[int]
KEY_sevensuperior: Final[int]
KEY_signaturemark: Final[int]
KEY_signifblank: Final[int]
KEY_similarequal: Final[int]
KEY_singlelowquotemark: Final[int]
KEY_sixsubscript: Final[int]
KEY_sixsuperior: Final[int]
KEY_slash: Final[int]
KEY_soliddiamond: Final[int]
KEY_space: Final[int]
KEY_squareroot: Final[int]
KEY_ssharp: Final[int]
KEY_sterling: Final[int]
KEY_stricteq: Final[int]
KEY_t: Final[int]
KEY_tabovedot: Final[int]
KEY_tcaron: Final[int]
KEY_tcedilla: Final[int]
KEY_telephone: Final[int]
KEY_telephonerecorder: Final[int]
KEY_therefore: Final[int]
KEY_thinspace: Final[int]
KEY_thorn: Final[int]
KEY_threeeighths: Final[int]
KEY_threefifths: Final[int]
KEY_threequarters: Final[int]
KEY_threesubscript: Final[int]
KEY_threesuperior: Final[int]
KEY_tintegral: Final[int]
KEY_topintegral: Final[int]
KEY_topleftparens: Final[int]
KEY_topleftradical: Final[int]
KEY_topleftsqbracket: Final[int]
KEY_topleftsummation: Final[int]
KEY_toprightparens: Final[int]
KEY_toprightsqbracket: Final[int]
KEY_toprightsummation: Final[int]
KEY_topt: Final[int]
KEY_topvertsummationconnector: Final[int]
KEY_trademark: Final[int]
KEY_trademarkincircle: Final[int]
KEY_tslash: Final[int]
KEY_twofifths: Final[int]
KEY_twosubscript: Final[int]
KEY_twosuperior: Final[int]
KEY_twothirds: Final[int]
KEY_u: Final[int]
KEY_uacute: Final[int]
KEY_ubelowdot: Final[int]
KEY_ubreve: Final[int]
KEY_ucircumflex: Final[int]
KEY_udiaeresis: Final[int]
KEY_udoubleacute: Final[int]
KEY_ugrave: Final[int]
KEY_uhook: Final[int]
KEY_uhorn: Final[int]
KEY_uhornacute: Final[int]
KEY_uhornbelowdot: Final[int]
KEY_uhorngrave: Final[int]
KEY_uhornhook: Final[int]
KEY_uhorntilde: Final[int]
KEY_umacron: Final[int]
KEY_underbar: Final[int]
KEY_underscore: Final[int]
KEY_union: Final[int]
KEY_uogonek: Final[int]
KEY_uparrow: Final[int]
KEY_upcaret: Final[int]
KEY_upleftcorner: Final[int]
KEY_uprightcorner: Final[int]
KEY_upshoe: Final[int]
KEY_upstile: Final[int]
KEY_uptack: Final[int]
KEY_uring: Final[int]
KEY_utilde: Final[int]
KEY_v: Final[int]
KEY_variation: Final[int]
KEY_vertbar: Final[int]
KEY_vertconnector: Final[int]
KEY_voicedsound: Final[int]
KEY_vt: Final[int]
KEY_w: Final[int]
KEY_wacute: Final[int]
KEY_wcircumflex: Final[int]
KEY_wdiaeresis: Final[int]
KEY_wgrave: Final[int]
KEY_x: Final[int]
KEY_xabovedot: Final[int]
KEY_y: Final[int]
KEY_yacute: Final[int]
KEY_ybelowdot: Final[int]
KEY_ycircumflex: Final[int]
KEY_ydiaeresis: Final[int]
KEY_yen: Final[int]
KEY_ygrave: Final[int]
KEY_yhook: Final[int]
KEY_ytilde: Final[int]
KEY_z: Final[int]
KEY_zabovedot: Final[int]
KEY_zacute: Final[int]
KEY_zcaron: Final[int]
KEY_zerosubscript: Final[int]
KEY_zerosuperior: Final[int]
KEY_zstroke: Final[int]
KP_0: Final[int]
KP_1: Final[int]
KP_2: Final[int]
KP_3: Final[int]
KP_4: Final[int]
KP_5: Final[int]
KP_6: Final[int]
KP_7: Final[int]
KP_8: Final[int]
KP_9: Final[int]
KP_Add: Final[int]
KP_Begin: Final[int]
KP_Decimal: Final[int]
KP_Delete: Final[int]
KP_Divide: Final[int]
KP_Down: Final[int]
KP_End: Final[int]
KP_Enter: Final[int]
KP_Equal: Final[int]
KP_F1: Final[int]
KP_F2: Final[int]
KP_F3: Final[int]
KP_F4: Final[int]
KP_Home: Final[int]
KP_Insert: Final[int]
KP_Left: Final[int]
KP_Multiply: Final[int]
KP_Next: Final[int]
KP_Page_Down: Final[int]
KP_Page_Up: Final[int]
KP_Prior: Final[int]
KP_Right: Final[int]
KP_Separator: Final[int]
KP_Space: Final[int]
KP_Subtract: Final[int]
KP_Tab: Final[int]
KP_Up: Final[int]
Kana_Lock: Final[int]
Kana_Shift: Final[int]
Kanji: Final[int]
Kanji_Bangou: Final[int]
Katakana: Final[int]
Kcedilla: Final[int]
Korean_Won: Final[int]
L: Final[int]
L1: Final[int]
L10: Final[int]
L2: Final[int]
L3: Final[int]
L4: Final[int]
L5: Final[int]
L6: Final[int]
L7: Final[int]
L8: Final[int]
L9: Final[int]
Lacute: Final[int]
Last_Virtual_Screen: Final[int]
Lbelowdot: Final[int]
Lcaron: Final[int]
Lcedilla: Final[int]
Left: Final[int]
Linefeed: Final[int]
LiraSign: Final[int]
Lstroke: Final[int]
M: Final[int]
MAJOR_VERSION: Final[int]
MAX_COMPOSE_LEN: Final[int]
MICRO_VERSION: Final[int]
MINOR_VERSION: Final[int]
Mabovedot: Final[int]
Macedonia_DSE: Final[int]
Macedonia_GJE: Final[int]
Macedonia_KJE: Final[int]
Macedonia_dse: Final[int]
Macedonia_gje: Final[int]
Macedonia_kje: Final[int]
Mae_Koho: Final[int]
Massyo: Final[int]
Menu: Final[int]
Meta_L: Final[int]
Meta_R: Final[int]
MillSign: Final[int]
Mode_switch: Final[int]
MouseKeys_Accel_Enable: Final[int]
MouseKeys_Enable: Final[int]
Muhenkan: Final[int]
Multi_key: Final[int]
MultipleCandidate: Final[int]
N: Final[int]
Nacute: Final[int]
NairaSign: Final[int]
Ncaron: Final[int]
Ncedilla: Final[int]
NewSheqelSign: Final[int]
Next: Final[int]
Next_Virtual_Screen: Final[int]
Ntilde: Final[int]
Num_Lock: Final[int]
O: Final[int]
OE: Final[int]
Oacute: Final[int]
Obarred: Final[int]
Obelowdot: Final[int]
Ocaron: Final[int]
Ocircumflex: Final[int]
Ocircumflexacute: Final[int]
Ocircumflexbelowdot: Final[int]
Ocircumflexgrave: Final[int]
Ocircumflexhook: Final[int]
Ocircumflextilde: Final[int]
Odiaeresis: Final[int]
Odoubleacute: Final[int]
Ograve: Final[int]
Ohook: Final[int]
Ohorn: Final[int]
Ohornacute: Final[int]
Ohornbelowdot: Final[int]
Ohorngrave: Final[int]
Ohornhook: Final[int]
Ohorntilde: Final[int]
Omacron: Final[int]
Ooblique: Final[int]
Oslash: Final[int]
Otilde: Final[int]
Overlay1_Enable: Final[int]
Overlay2_Enable: Final[int]
P: Final[int]
PATH_CONFIG: Final = "/org/freedesktop/IBus/Config"
PATH_FACTORY: Final = "/org/freedesktop/IBus/Factory"
PATH_IBUS: Final = "/org/freedesktop/IBus"
PATH_INPUT_CONTEXT: Final = "/org/freedesktop/IBus/InputContext_%d"
PATH_NOTIFICATIONS: Final = "/org/freedesktop/IBus/Notifications"
PATH_PANEL: Final = "/org/freedesktop/IBus/Panel"
PATH_PANEL_EXTENSION_EMOJI: Final = "/org/freedesktop/IBus/Panel/Extension/Emoji"
Pabovedot: Final[int]
Page_Down: Final[int]
Page_Up: Final[int]
Pause: Final[int]
PesetaSign: Final[int]
Pointer_Accelerate: Final[int]
Pointer_Button1: Final[int]
Pointer_Button2: Final[int]
Pointer_Button3: Final[int]
Pointer_Button4: Final[int]
Pointer_Button5: Final[int]
Pointer_Button_Dflt: Final[int]
Pointer_DblClick1: Final[int]
Pointer_DblClick2: Final[int]
Pointer_DblClick3: Final[int]
Pointer_DblClick4: Final[int]
Pointer_DblClick5: Final[int]
Pointer_DblClick_Dflt: Final[int]
Pointer_DfltBtnNext: Final[int]
Pointer_DfltBtnPrev: Final[int]
Pointer_Down: Final[int]
Pointer_DownLeft: Final[int]
Pointer_DownRight: Final[int]
Pointer_Drag1: Final[int]
Pointer_Drag2: Final[int]
Pointer_Drag3: Final[int]
Pointer_Drag4: Final[int]
Pointer_Drag5: Final[int]
Pointer_Drag_Dflt: Final[int]
Pointer_EnableKeys: Final[int]
Pointer_Left: Final[int]
Pointer_Right: Final[int]
Pointer_Up: Final[int]
Pointer_UpLeft: Final[int]
Pointer_UpRight: Final[int]
Prev_Virtual_Screen: Final[int]
PreviousCandidate: Final[int]
Print: Final[int]
Prior: Final[int]
Q: Final[int]
R: Final[int]
R1: Final[int]
R10: Final[int]
R11: Final[int]
R12: Final[int]
R13: Final[int]
R14: Final[int]
R15: Final[int]
R2: Final[int]
R3: Final[int]
R4: Final[int]
R5: Final[int]
R6: Final[int]
R7: Final[int]
R8: Final[int]
R9: Final[int]
Racute: Final[int]
Rcaron: Final[int]
Rcedilla: Final[int]
Redo: Final[int]
RepeatKeys_Enable: Final[int]
Return: Final[int]
Right: Final[int]
Romaji: Final[int]
RupeeSign: Final[int]
S: Final[int]
SCHWA: Final[int]
SERVICE_CONFIG: Final = "org.freedesktop.IBus.Config"
SERVICE_IBUS: Final = "org.freedesktop.IBus"
SERVICE_NOTIFICATIONS: Final = "org.freedesktop.IBus.Notifications"
SERVICE_PANEL: Final = "org.freedesktop.IBus.Panel"
SERVICE_PANEL_EXTENSION: Final = "org.freedesktop.IBus.Panel.Extension"
SERVICE_PANEL_EXTENSION_EMOJI: Final = "org.freedesktop.IBus.Panel.Extension.Emoji"
SERVICE_PORTAL: Final = "org.freedesktop.portal.IBus"
Sabovedot: Final[int]
Sacute: Final[int]
Scaron: Final[int]
Scedilla: Final[int]
Scircumflex: Final[int]
Scroll_Lock: Final[int]
Select: Final[int]
Serbian_DJE: Final[int]
Serbian_DZE: Final[int]
Serbian_JE: Final[int]
Serbian_LJE: Final[int]
Serbian_NJE: Final[int]
Serbian_TSHE: Final[int]
Serbian_dje: Final[int]
Serbian_dze: Final[int]
Serbian_je: Final[int]
Serbian_lje: Final[int]
Serbian_nje: Final[int]
Serbian_tshe: Final[int]
Shift_L: Final[int]
Shift_Lock: Final[int]
Shift_R: Final[int]
SingleCandidate: Final[int]
SlowKeys_Enable: Final[int]
StickyKeys_Enable: Final[int]
Super_L: Final[int]
Super_R: Final[int]
Sys_Req: Final[int]
T: Final[int]
THORN: Final[int]
Tab: Final[int]
Tabovedot: Final[int]
Tcaron: Final[int]
Tcedilla: Final[int]
Terminate_Server: Final[int]
Thai_baht: Final[int]
Thai_bobaimai: Final[int]
Thai_chochan: Final[int]
Thai_chochang: Final[int]
Thai_choching: Final[int]
Thai_chochoe: Final[int]
Thai_dochada: Final[int]
Thai_dodek: Final[int]
Thai_fofa: Final[int]
Thai_fofan: Final[int]
Thai_hohip: Final[int]
Thai_honokhuk: Final[int]
Thai_khokhai: Final[int]
Thai_khokhon: Final[int]
Thai_khokhuat: Final[int]
Thai_khokhwai: Final[int]
Thai_khorakhang: Final[int]
Thai_kokai: Final[int]
Thai_lakkhangyao: Final[int]
Thai_lekchet: Final[int]
Thai_lekha: Final[int]
Thai_lekhok: Final[int]
Thai_lekkao: Final[int]
Thai_leknung: Final[int]
Thai_lekpaet: Final[int]
Thai_leksam: Final[int]
Thai_leksi: Final[int]
Thai_leksong: Final[int]
Thai_leksun: Final[int]
Thai_lochula: Final[int]
Thai_loling: Final[int]
Thai_lu: Final[int]
Thai_maichattawa: Final[int]
Thai_maiek: Final[int]
Thai_maihanakat: Final[int]
Thai_maihanakat_maitho: Final[int]
Thai_maitaikhu: Final[int]
Thai_maitho: Final[int]
Thai_maitri: Final[int]
Thai_maiyamok: Final[int]
Thai_moma: Final[int]
Thai_ngongu: Final[int]
Thai_nikhahit: Final[int]
Thai_nonen: Final[int]
Thai_nonu: Final[int]
Thai_oang: Final[int]
Thai_paiyannoi: Final[int]
Thai_phinthu: Final[int]
Thai_phophan: Final[int]
Thai_phophung: Final[int]
Thai_phosamphao: Final[int]
Thai_popla: Final[int]
Thai_rorua: Final[int]
Thai_ru: Final[int]
Thai_saraa: Final[int]
Thai_saraaa: Final[int]
Thai_saraae: Final[int]
Thai_saraaimaimalai: Final[int]
Thai_saraaimaimuan: Final[int]
Thai_saraam: Final[int]
Thai_sarae: Final[int]
Thai_sarai: Final[int]
Thai_saraii: Final[int]
Thai_sarao: Final[int]
Thai_sarau: Final[int]
Thai_saraue: Final[int]
Thai_sarauee: Final[int]
Thai_sarauu: Final[int]
Thai_sorusi: Final[int]
Thai_sosala: Final[int]
Thai_soso: Final[int]
Thai_sosua: Final[int]
Thai_thanthakhat: Final[int]
Thai_thonangmontho: Final[int]
Thai_thophuthao: Final[int]
Thai_thothahan: Final[int]
Thai_thothan: Final[int]
Thai_thothong: Final[int]
Thai_thothung: Final[int]
Thai_topatak: Final[int]
Thai_totao: Final[int]
Thai_wowaen: Final[int]
Thai_yoyak: Final[int]
Thai_yoying: Final[int]
Thorn: Final[int]
Touroku: Final[int]
Tslash: Final[int]
U: Final[int]
Uacute: Final[int]
Ubelowdot: Final[int]
Ubreve: Final[int]
Ucircumflex: Final[int]
Udiaeresis: Final[int]
Udoubleacute: Final[int]
Ugrave: Final[int]
Uhook: Final[int]
Uhorn: Final[int]
Uhornacute: Final[int]
Uhornbelowdot: Final[int]
Uhorngrave: Final[int]
Uhornhook: Final[int]
Uhorntilde: Final[int]
Ukrainian_GHE_WITH_UPTURN: Final[int]
Ukrainian_I: Final[int]
Ukrainian_IE: Final[int]
Ukrainian_YI: Final[int]
Ukrainian_ghe_with_upturn: Final[int]
Ukrainian_i: Final[int]
Ukrainian_ie: Final[int]
Ukrainian_yi: Final[int]
Ukranian_I: Final[int]
Ukranian_JE: Final[int]
Ukranian_YI: Final[int]
Ukranian_i: Final[int]
Ukranian_je: Final[int]
Ukranian_yi: Final[int]
Umacron: Final[int]
Undo: Final[int]
Uogonek: Final[int]
Up: Final[int]
Uring: Final[int]
Utilde: Final[int]
V: Final[int]
VoidSymbol: Final[int]
W: Final[int]
Wacute: Final[int]
Wcircumflex: Final[int]
Wdiaeresis: Final[int]
Wgrave: Final[int]
WonSign: Final[int]
X: Final[int]
Xabovedot: Final[int]
Y: Final[int]
Yacute: Final[int]
Ybelowdot: Final[int]
Ycircumflex: Final[int]
Ydiaeresis: Final[int]
Ygrave: Final[int]
Yhook: Final[int]
Ytilde: Final[int]
Z: Final[int]
Zabovedot: Final[int]
Zacute: Final[int]
Zcaron: Final[int]
Zen_Koho: Final[int]
Zenkaku: Final[int]
Zenkaku_Hankaku: Final[int]
Zstroke: Final[int]
a: Final[int]
aacute: Final[int]
abelowdot: Final[int]
abovedot: Final[int]
abreve: Final[int]
abreveacute: Final[int]
abrevebelowdot: Final[int]
abrevegrave: Final[int]
abrevehook: Final[int]
abrevetilde: Final[int]
acircumflex: Final[int]
acircumflexacute: Final[int]
acircumflexbelowdot: Final[int]
acircumflexgrave: Final[int]
acircumflexhook: Final[int]
acircumflextilde: Final[int]
acute: Final[int]
adiaeresis: Final[int]
ae: Final[int]
agrave: Final[int]
ahook: Final[int]
amacron: Final[int]
ampersand: Final[int]
aogonek: Final[int]
apostrophe: Final[int]
approxeq: Final[int]
approximate: Final[int]
aring: Final[int]
asciicircum: Final[int]
asciitilde: Final[int]
asterisk: Final[int]
at: Final[int]
atilde: Final[int]
b: Final[int]
babovedot: Final[int]
backslash: Final[int]
ballotcross: Final[int]
bar: Final[int]
because: Final[int]
blank: Final[int]
botintegral: Final[int]
botleftparens: Final[int]
botleftsqbracket: Final[int]
botleftsummation: Final[int]
botrightparens: Final[int]
botrightsqbracket: Final[int]
botrightsummation: Final[int]
bott: Final[int]
botvertsummationconnector: Final[int]
braceleft: Final[int]
braceright: Final[int]
bracketleft: Final[int]
bracketright: Final[int]
braille_blank: Final[int]
braille_dot_1: Final[int]
braille_dot_10: Final[int]
braille_dot_2: Final[int]
braille_dot_3: Final[int]
braille_dot_4: Final[int]
braille_dot_5: Final[int]
braille_dot_6: Final[int]
braille_dot_7: Final[int]
braille_dot_8: Final[int]
braille_dot_9: Final[int]
braille_dots_1: Final[int]
braille_dots_12: Final[int]
braille_dots_123: Final[int]
braille_dots_1234: Final[int]
braille_dots_12345: Final[int]
braille_dots_123456: Final[int]
braille_dots_1234567: Final[int]
braille_dots_12345678: Final[int]
braille_dots_1234568: Final[int]
braille_dots_123457: Final[int]
braille_dots_1234578: Final[int]
braille_dots_123458: Final[int]
braille_dots_12346: Final[int]
braille_dots_123467: Final[int]
braille_dots_1234678: Final[int]
braille_dots_123468: Final[int]
braille_dots_12347: Final[int]
braille_dots_123478: Final[int]
braille_dots_12348: Final[int]
braille_dots_1235: Final[int]
braille_dots_12356: Final[int]
braille_dots_123567: Final[int]
braille_dots_1235678: Final[int]
braille_dots_123568: Final[int]
braille_dots_12357: Final[int]
braille_dots_123578: Final[int]
braille_dots_12358: Final[int]
braille_dots_1236: Final[int]
braille_dots_12367: Final[int]
braille_dots_123678: Final[int]
braille_dots_12368: Final[int]
braille_dots_1237: Final[int]
braille_dots_12378: Final[int]
braille_dots_1238: Final[int]
braille_dots_124: Final[int]
braille_dots_1245: Final[int]
braille_dots_12456: Final[int]
braille_dots_124567: Final[int]
braille_dots_1245678: Final[int]
braille_dots_124568: Final[int]
braille_dots_12457: Final[int]
braille_dots_124578: Final[int]
braille_dots_12458: Final[int]
braille_dots_1246: Final[int]
braille_dots_12467: Final[int]
braille_dots_124678: Final[int]
braille_dots_12468: Final[int]
braille_dots_1247: Final[int]
braille_dots_12478: Final[int]
braille_dots_1248: Final[int]
braille_dots_125: Final[int]
braille_dots_1256: Final[int]
braille_dots_12567: Final[int]
braille_dots_125678: Final[int]
braille_dots_12568: Final[int]
braille_dots_1257: Final[int]
braille_dots_12578: Final[int]
braille_dots_1258: Final[int]
braille_dots_126: Final[int]
braille_dots_1267: Final[int]
braille_dots_12678: Final[int]
braille_dots_1268: Final[int]
braille_dots_127: Final[int]
braille_dots_1278: Final[int]
braille_dots_128: Final[int]
braille_dots_13: Final[int]
braille_dots_134: Final[int]
braille_dots_1345: Final[int]
braille_dots_13456: Final[int]
braille_dots_134567: Final[int]
braille_dots_1345678: Final[int]
braille_dots_134568: Final[int]
braille_dots_13457: Final[int]
braille_dots_134578: Final[int]
braille_dots_13458: Final[int]
braille_dots_1346: Final[int]
braille_dots_13467: Final[int]
braille_dots_134678: Final[int]
braille_dots_13468: Final[int]
braille_dots_1347: Final[int]
braille_dots_13478: Final[int]
braille_dots_1348: Final[int]
braille_dots_135: Final[int]
braille_dots_1356: Final[int]
braille_dots_13567: Final[int]
braille_dots_135678: Final[int]
braille_dots_13568: Final[int]
braille_dots_1357: Final[int]
braille_dots_13578: Final[int]
braille_dots_1358: Final[int]
braille_dots_136: Final[int]
braille_dots_1367: Final[int]
braille_dots_13678: Final[int]
braille_dots_1368: Final[int]
braille_dots_137: Final[int]
braille_dots_1378: Final[int]
braille_dots_138: Final[int]
braille_dots_14: Final[int]
braille_dots_145: Final[int]
braille_dots_1456: Final[int]
braille_dots_14567: Final[int]
braille_dots_145678: Final[int]
braille_dots_14568: Final[int]
braille_dots_1457: Final[int]
braille_dots_14578: Final[int]
braille_dots_1458: Final[int]
braille_dots_146: Final[int]
braille_dots_1467: Final[int]
braille_dots_14678: Final[int]
braille_dots_1468: Final[int]
braille_dots_147: Final[int]
braille_dots_1478: Final[int]
braille_dots_148: Final[int]
braille_dots_15: Final[int]
braille_dots_156: Final[int]
braille_dots_1567: Final[int]
braille_dots_15678: Final[int]
braille_dots_1568: Final[int]
braille_dots_157: Final[int]
braille_dots_1578: Final[int]
braille_dots_158: Final[int]
braille_dots_16: Final[int]
braille_dots_167: Final[int]
braille_dots_1678: Final[int]
braille_dots_168: Final[int]
braille_dots_17: Final[int]
braille_dots_178: Final[int]
braille_dots_18: Final[int]
braille_dots_2: Final[int]
braille_dots_23: Final[int]
braille_dots_234: Final[int]
braille_dots_2345: Final[int]
braille_dots_23456: Final[int]
braille_dots_234567: Final[int]
braille_dots_2345678: Final[int]
braille_dots_234568: Final[int]
braille_dots_23457: Final[int]
braille_dots_234578: Final[int]
braille_dots_23458: Final[int]
braille_dots_2346: Final[int]
braille_dots_23467: Final[int]
braille_dots_234678: Final[int]
braille_dots_23468: Final[int]
braille_dots_2347: Final[int]
braille_dots_23478: Final[int]
braille_dots_2348: Final[int]
braille_dots_235: Final[int]
braille_dots_2356: Final[int]
braille_dots_23567: Final[int]
braille_dots_235678: Final[int]
braille_dots_23568: Final[int]
braille_dots_2357: Final[int]
braille_dots_23578: Final[int]
braille_dots_2358: Final[int]
braille_dots_236: Final[int]
braille_dots_2367: Final[int]
braille_dots_23678: Final[int]
braille_dots_2368: Final[int]
braille_dots_237: Final[int]
braille_dots_2378: Final[int]
braille_dots_238: Final[int]
braille_dots_24: Final[int]
braille_dots_245: Final[int]
braille_dots_2456: Final[int]
braille_dots_24567: Final[int]
braille_dots_245678: Final[int]
braille_dots_24568: Final[int]
braille_dots_2457: Final[int]
braille_dots_24578: Final[int]
braille_dots_2458: Final[int]
braille_dots_246: Final[int]
braille_dots_2467: Final[int]
braille_dots_24678: Final[int]
braille_dots_2468: Final[int]
braille_dots_247: Final[int]
braille_dots_2478: Final[int]
braille_dots_248: Final[int]
braille_dots_25: Final[int]
braille_dots_256: Final[int]
braille_dots_2567: Final[int]
braille_dots_25678: Final[int]
braille_dots_2568: Final[int]
braille_dots_257: Final[int]
braille_dots_2578: Final[int]
braille_dots_258: Final[int]
braille_dots_26: Final[int]
braille_dots_267: Final[int]
braille_dots_2678: Final[int]
braille_dots_268: Final[int]
braille_dots_27: Final[int]
braille_dots_278: Final[int]
braille_dots_28: Final[int]
braille_dots_3: Final[int]
braille_dots_34: Final[int]
braille_dots_345: Final[int]
braille_dots_3456: Final[int]
braille_dots_34567: Final[int]
braille_dots_345678: Final[int]
braille_dots_34568: Final[int]
braille_dots_3457: Final[int]
braille_dots_34578: Final[int]
braille_dots_3458: Final[int]
braille_dots_346: Final[int]
braille_dots_3467: Final[int]
braille_dots_34678: Final[int]
braille_dots_3468: Final[int]
braille_dots_347: Final[int]
braille_dots_3478: Final[int]
braille_dots_348: Final[int]
braille_dots_35: Final[int]
braille_dots_356: Final[int]
braille_dots_3567: Final[int]
braille_dots_35678: Final[int]
braille_dots_3568: Final[int]
braille_dots_357: Final[int]
braille_dots_3578: Final[int]
braille_dots_358: Final[int]
braille_dots_36: Final[int]
braille_dots_367: Final[int]
braille_dots_3678: Final[int]
braille_dots_368: Final[int]
braille_dots_37: Final[int]
braille_dots_378: Final[int]
braille_dots_38: Final[int]
braille_dots_4: Final[int]
braille_dots_45: Final[int]
braille_dots_456: Final[int]
braille_dots_4567: Final[int]
braille_dots_45678: Final[int]
braille_dots_4568: Final[int]
braille_dots_457: Final[int]
braille_dots_4578: Final[int]
braille_dots_458: Final[int]
braille_dots_46: Final[int]
braille_dots_467: Final[int]
braille_dots_4678: Final[int]
braille_dots_468: Final[int]
braille_dots_47: Final[int]
braille_dots_478: Final[int]
braille_dots_48: Final[int]
braille_dots_5: Final[int]
braille_dots_56: Final[int]
braille_dots_567: Final[int]
braille_dots_5678: Final[int]
braille_dots_568: Final[int]
braille_dots_57: Final[int]
braille_dots_578: Final[int]
braille_dots_58: Final[int]
braille_dots_6: Final[int]
braille_dots_67: Final[int]
braille_dots_678: Final[int]
braille_dots_68: Final[int]
braille_dots_7: Final[int]
braille_dots_78: Final[int]
braille_dots_8: Final[int]
breve: Final[int]
brokenbar: Final[int]
c: Final[int]
cabovedot: Final[int]
cacute: Final[int]
careof: Final[int]
caret: Final[int]
caron: Final[int]
ccaron: Final[int]
ccedilla: Final[int]
ccircumflex: Final[int]
cedilla: Final[int]
cent: Final[int]
checkerboard: Final[int]
checkmark: Final[int]
circle: Final[int]
club: Final[int]
colon: Final[int]
comma: Final[int]
containsas: Final[int]
copyright: Final[int]
cr: Final[int]
crossinglines: Final[int]
cuberoot: Final[int]
currency: Final[int]
cursor: Final[int]
d: Final[int]
dabovedot: Final[int]
dagger: Final[int]
dcaron: Final[int]
dead_abovecomma: Final[int]
dead_abovedot: Final[int]
dead_abovereversedcomma: Final[int]
dead_abovering: Final[int]
dead_acute: Final[int]
dead_belowbreve: Final[int]
dead_belowcircumflex: Final[int]
dead_belowdiaeresis: Final[int]
dead_belowdot: Final[int]
dead_belowmacron: Final[int]
dead_belowring: Final[int]
dead_belowtilde: Final[int]
dead_breve: Final[int]
dead_caron: Final[int]
dead_cedilla: Final[int]
dead_circumflex: Final[int]
dead_dasia: Final[int]
dead_diaeresis: Final[int]
dead_doubleacute: Final[int]
dead_grave: Final[int]
dead_hook: Final[int]
dead_horn: Final[int]
dead_iota: Final[int]
dead_macron: Final[int]
dead_ogonek: Final[int]
dead_perispomeni: Final[int]
dead_psili: Final[int]
dead_semivoiced_sound: Final[int]
dead_stroke: Final[int]
dead_tilde: Final[int]
dead_voiced_sound: Final[int]
decimalpoint: Final[int]
degree: Final[int]
diaeresis: Final[int]
diamond: Final[int]
digitspace: Final[int]
dintegral: Final[int]
division: Final[int]
dollar: Final[int]
doubbaselinedot: Final[int]
doubleacute: Final[int]
doubledagger: Final[int]
doublelowquotemark: Final[int]
downarrow: Final[int]
downcaret: Final[int]
downshoe: Final[int]
downstile: Final[int]
downtack: Final[int]
dstroke: Final[int]
e: Final[int]
eabovedot: Final[int]
eacute: Final[int]
ebelowdot: Final[int]
ecaron: Final[int]
ecircumflex: Final[int]
ecircumflexacute: Final[int]
ecircumflexbelowdot: Final[int]
ecircumflexgrave: Final[int]
ecircumflexhook: Final[int]
ecircumflextilde: Final[int]
ediaeresis: Final[int]
egrave: Final[int]
ehook: Final[int]
eightsubscript: Final[int]
eightsuperior: Final[int]
elementof: Final[int]
ellipsis: Final[int]
em3space: Final[int]
em4space: Final[int]
emacron: Final[int]
emdash: Final[int]
emfilledcircle: Final[int]
emfilledrect: Final[int]
emopencircle: Final[int]
emopenrectangle: Final[int]
emptyset: Final[int]
emspace: Final[int]
endash: Final[int]
enfilledcircbullet: Final[int]
enfilledsqbullet: Final[int]
eng: Final[int]
enopencircbullet: Final[int]
enopensquarebullet: Final[int]
enspace: Final[int]
eogonek: Final[int]
equal: Final[int]
eth: Final[int]
etilde: Final[int]
exclam: Final[int]
exclamdown: Final[int]
f: Final[int]
fabovedot: Final[int]
femalesymbol: Final[int]
ff: Final[int]
figdash: Final[int]
filledlefttribullet: Final[int]
filledrectbullet: Final[int]
filledrighttribullet: Final[int]
filledtribulletdown: Final[int]
filledtribulletup: Final[int]
fiveeighths: Final[int]
fivesixths: Final[int]
fivesubscript: Final[int]
fivesuperior: Final[int]
fourfifths: Final[int]
foursubscript: Final[int]
foursuperior: Final[int]
fourthroot: Final[int]
function: Final[int]
g: Final[int]
gabovedot: Final[int]
gbreve: Final[int]
gcaron: Final[int]
gcedilla: Final[int]
gcircumflex: Final[int]
grave: Final[int]
greater: Final[int]
greaterthanequal: Final[int]
guillemotleft: Final[int]
guillemotright: Final[int]
h: Final[int]
hairspace: Final[int]
hcircumflex: Final[int]
heart: Final[int]
hebrew_aleph: Final[int]
hebrew_ayin: Final[int]
hebrew_bet: Final[int]
hebrew_beth: Final[int]
hebrew_chet: Final[int]
hebrew_dalet: Final[int]
hebrew_daleth: Final[int]
hebrew_doublelowline: Final[int]
hebrew_finalkaph: Final[int]
hebrew_finalmem: Final[int]
hebrew_finalnun: Final[int]
hebrew_finalpe: Final[int]
hebrew_finalzade: Final[int]
hebrew_finalzadi: Final[int]
hebrew_gimel: Final[int]
hebrew_gimmel: Final[int]
hebrew_he: Final[int]
hebrew_het: Final[int]
hebrew_kaph: Final[int]
hebrew_kuf: Final[int]
hebrew_lamed: Final[int]
hebrew_mem: Final[int]
hebrew_nun: Final[int]
hebrew_pe: Final[int]
hebrew_qoph: Final[int]
hebrew_resh: Final[int]
hebrew_samech: Final[int]
hebrew_samekh: Final[int]
hebrew_shin: Final[int]
hebrew_taf: Final[int]
hebrew_taw: Final[int]
hebrew_tet: Final[int]
hebrew_teth: Final[int]
hebrew_waw: Final[int]
hebrew_yod: Final[int]
hebrew_zade: Final[int]
hebrew_zadi: Final[int]
hebrew_zain: Final[int]
hebrew_zayin: Final[int]
hexagram: Final[int]
horizconnector: Final[int]
horizlinescan1: Final[int]
horizlinescan3: Final[int]
horizlinescan5: Final[int]
horizlinescan7: Final[int]
horizlinescan9: Final[int]
hstroke: Final[int]
ht: Final[int]
hyphen: Final[int]
i: Final[int]
iacute: Final[int]
ibelowdot: Final[int]
ibreve: Final[int]
icircumflex: Final[int]
identical: Final[int]
idiaeresis: Final[int]
idotless: Final[int]
ifonlyif: Final[int]
igrave: Final[int]
ihook: Final[int]
imacron: Final[int]
implies: Final[int]
includedin: Final[int]
includes: Final[int]
infinity: Final[int]
integral: Final[int]
intersection: Final[int]
iogonek: Final[int]
itilde: Final[int]
j: Final[int]
jcircumflex: Final[int]
jot: Final[int]
k: Final[int]
kana_A: Final[int]
kana_CHI: Final[int]
kana_E: Final[int]
kana_FU: Final[int]
kana_HA: Final[int]
kana_HE: Final[int]
kana_HI: Final[int]
kana_HO: Final[int]
kana_HU: Final[int]
kana_I: Final[int]
kana_KA: Final[int]
kana_KE: Final[int]
kana_KI: Final[int]
kana_KO: Final[int]
kana_KU: Final[int]
kana_MA: Final[int]
kana_ME: Final[int]
kana_MI: Final[int]
kana_MO: Final[int]
kana_MU: Final[int]
kana_N: Final[int]
kana_NA: Final[int]
kana_NE: Final[int]
kana_NI: Final[int]
kana_NO: Final[int]
kana_NU: Final[int]
kana_O: Final[int]
kana_RA: Final[int]
kana_RE: Final[int]
kana_RI: Final[int]
kana_RO: Final[int]
kana_RU: Final[int]
kana_SA: Final[int]
kana_SE: Final[int]
kana_SHI: Final[int]
kana_SO: Final[int]
kana_SU: Final[int]
kana_TA: Final[int]
kana_TE: Final[int]
kana_TI: Final[int]
kana_TO: Final[int]
kana_TSU: Final[int]
kana_TU: Final[int]
kana_U: Final[int]
kana_WA: Final[int]
kana_WO: Final[int]
kana_YA: Final[int]
kana_YO: Final[int]
kana_YU: Final[int]
kana_a: Final[int]
kana_closingbracket: Final[int]
kana_comma: Final[int]
kana_conjunctive: Final[int]
kana_e: Final[int]
kana_fullstop: Final[int]
kana_i: Final[int]
kana_middledot: Final[int]
kana_o: Final[int]
kana_openingbracket: Final[int]
kana_switch: Final[int]
kana_tsu: Final[int]
kana_tu: Final[int]
kana_u: Final[int]
kana_ya: Final[int]
kana_yo: Final[int]
kana_yu: Final[int]
kappa: Final[int]
kcedilla: Final[int]
kra: Final[int]
l: Final[int]
lacute: Final[int]
latincross: Final[int]
lbelowdot: Final[int]
lcaron: Final[int]
lcedilla: Final[int]
leftanglebracket: Final[int]
leftarrow: Final[int]
leftcaret: Final[int]
leftdoublequotemark: Final[int]
leftmiddlecurlybrace: Final[int]
leftopentriangle: Final[int]
leftpointer: Final[int]
leftradical: Final[int]
leftshoe: Final[int]
leftsinglequotemark: Final[int]
leftt: Final[int]
lefttack: Final[int]
less: Final[int]
lessthanequal: Final[int]
lf: Final[int]
logicaland: Final[int]
logicalor: Final[int]
lowleftcorner: Final[int]
lowrightcorner: Final[int]
lstroke: Final[int]
m: Final[int]
mabovedot: Final[int]
macron: Final[int]
malesymbol: Final[int]
maltesecross: Final[int]
marker: Final[int]
masculine: Final[int]
minus: Final[int]
minutes: Final[int]
mu: Final[int]
multiply: Final[int]
musicalflat: Final[int]
musicalsharp: Final[int]
n: Final[int]
nabla: Final[int]
nacute: Final[int]
ncaron: Final[int]
ncedilla: Final[int]
ninesubscript: Final[int]
ninesuperior: Final[int]
nl: Final[int]
nobreakspace: Final[int]
notapproxeq: Final[int]
notelementof: Final[int]
notequal: Final[int]
notidentical: Final[int]
notsign: Final[int]
ntilde: Final[int]
numbersign: Final[int]
numerosign: Final[int]
o: Final[int]
oacute: Final[int]
obarred: Final[int]
obelowdot: Final[int]
ocaron: Final[int]
ocircumflex: Final[int]
ocircumflexacute: Final[int]
ocircumflexbelowdot: Final[int]
ocircumflexgrave: Final[int]
ocircumflexhook: Final[int]
ocircumflextilde: Final[int]
odiaeresis: Final[int]
odoubleacute: Final[int]
oe: Final[int]
ogonek: Final[int]
ograve: Final[int]
ohook: Final[int]
ohorn: Final[int]
ohornacute: Final[int]
ohornbelowdot: Final[int]
ohorngrave: Final[int]
ohornhook: Final[int]
ohorntilde: Final[int]
omacron: Final[int]
oneeighth: Final[int]
onefifth: Final[int]
onehalf: Final[int]
onequarter: Final[int]
onesixth: Final[int]
onesubscript: Final[int]
onesuperior: Final[int]
onethird: Final[int]
ooblique: Final[int]
openrectbullet: Final[int]
openstar: Final[int]
opentribulletdown: Final[int]
opentribulletup: Final[int]
ordfeminine: Final[int]
oslash: Final[int]
otilde: Final[int]
overbar: Final[int]
overline: Final[int]
p: Final[int]
pabovedot: Final[int]
paragraph: Final[int]
parenleft: Final[int]
parenright: Final[int]
partdifferential: Final[int]
partialderivative: Final[int]
percent: Final[int]
period: Final[int]
periodcentered: Final[int]
phonographcopyright: Final[int]
plus: Final[int]
plusminus: Final[int]
prescription: Final[int]
prolongedsound: Final[int]
punctspace: Final[int]
q: Final[int]
quad: Final[int]
question: Final[int]
questiondown: Final[int]
quotedbl: Final[int]
quoteleft: Final[int]
quoteright: Final[int]
r: Final[int]
racute: Final[int]
radical: Final[int]
rcaron: Final[int]
rcedilla: Final[int]
registered: Final[int]
rightanglebracket: Final[int]
rightarrow: Final[int]
rightcaret: Final[int]
rightdoublequotemark: Final[int]
rightmiddlecurlybrace: Final[int]
rightmiddlesummation: Final[int]
rightopentriangle: Final[int]
rightpointer: Final[int]
rightshoe: Final[int]
rightsinglequotemark: Final[int]
rightt: Final[int]
righttack: Final[int]
s: Final[int]
sabovedot: Final[int]
sacute: Final[int]
scaron: Final[int]
scedilla: Final[int]
schwa: Final[int]
scircumflex: Final[int]
script_switch: Final[int]
seconds: Final[int]
section: Final[int]
semicolon: Final[int]
semivoicedsound: Final[int]
seveneighths: Final[int]
sevensubscript: Final[int]
sevensuperior: Final[int]
signaturemark: Final[int]
signifblank: Final[int]
similarequal: Final[int]
singlelowquotemark: Final[int]
sixsubscript: Final[int]
sixsuperior: Final[int]
slash: Final[int]
soliddiamond: Final[int]
space: Final[int]
squareroot: Final[int]
ssharp: Final[int]
sterling: Final[int]
stricteq: Final[int]
t: Final[int]
tabovedot: Final[int]
tcaron: Final[int]
tcedilla: Final[int]
telephone: Final[int]
telephonerecorder: Final[int]
therefore: Final[int]
thinspace: Final[int]
thorn: Final[int]
threeeighths: Final[int]
threefifths: Final[int]
threequarters: Final[int]
threesubscript: Final[int]
threesuperior: Final[int]
tintegral: Final[int]
topintegral: Final[int]
topleftparens: Final[int]
topleftradical: Final[int]
topleftsqbracket: Final[int]
topleftsummation: Final[int]
toprightparens: Final[int]
toprightsqbracket: Final[int]
toprightsummation: Final[int]
topt: Final[int]
topvertsummationconnector: Final[int]
trademark: Final[int]
trademarkincircle: Final[int]
tslash: Final[int]
twofifths: Final[int]
twosubscript: Final[int]
twosuperior: Final[int]
twothirds: Final[int]
u: Final[int]
uacute: Final[int]
ubelowdot: Final[int]
ubreve: Final[int]
ucircumflex: Final[int]
udiaeresis: Final[int]
udoubleacute: Final[int]
ugrave: Final[int]
uhook: Final[int]
uhorn: Final[int]
uhornacute: Final[int]
uhornbelowdot: Final[int]
uhorngrave: Final[int]
uhornhook: Final[int]
uhorntilde: Final[int]
umacron: Final[int]
underbar: Final[int]
underscore: Final[int]
union: Final[int]
uogonek: Final[int]
uparrow: Final[int]
upcaret: Final[int]
upleftcorner: Final[int]
uprightcorner: Final[int]
upshoe: Final[int]
upstile: Final[int]
uptack: Final[int]
uring: Final[int]
utilde: Final[int]
v: Final[int]
variation: Final[int]
vertbar: Final[int]
vertconnector: Final[int]
voicedsound: Final[int]
vt: Final[int]
w: Final[int]
wacute: Final[int]
wcircumflex: Final[int]
wdiaeresis: Final[int]
wgrave: Final[int]
x: Final[int]
xabovedot: Final[int]
y: Final[int]
yacute: Final[int]
ybelowdot: Final[int]
ycircumflex: Final[int]
ydiaeresis: Final[int]
yen: Final[int]
ygrave: Final[int]
yhook: Final[int]
ytilde: Final[int]
z: Final[int]
zabovedot: Final[int]
zacute: Final[int]
zcaron: Final[int]
zerosubscript: Final[int]
zerosuperior: Final[int]
zstroke: Final[int]

def accelerator_name(accelerator_key: int, accelerator_mods: ModifierType) -> str: ...
def accelerator_parse(accelerator: str) -> tuple[int, ModifierType]: ...
def accelerator_valid(keyval: int, modifiers: ModifierType) -> bool: ...
def attr_background_new(color: int, start_index: int, end_index: int) -> Attribute: ...
def attr_foreground_new(color: int, start_index: int, end_index: int) -> Attribute: ...
def attr_underline_new(
    underline_type: int, start_index: int, end_index: int
) -> Attribute: ...
def emoji_dict_load(path: str) -> dict[str, None]: ...
def emoji_dict_lookup(dict: dict[str, EmojiData], emoji: str) -> EmojiData: ...
def emoji_dict_save(path: str, dict: dict[str, None]) -> None: ...
def error_quark() -> int: ...
def free_strv(strv: str) -> None: ...
def get_address() -> str: ...
def get_daemon_uid() -> int: ...
def get_language_name(_locale: str) -> str: ...
def get_local_machine_id() -> str: ...
def get_socket_path() -> str: ...
def get_timeout() -> int: ...
def get_untranslated_language_name(_locale: str) -> str: ...
def get_user_name() -> str: ...
def init() -> None: ...
def key_event_from_string(string: str) -> tuple[bool, int, int]: ...
def key_event_to_string(keyval: int, modifiers: int) -> str: ...
def keyval_convert_case(symbol: int) -> tuple[int, int]: ...
def keyval_from_name(keyval_name: str) -> int: ...
def keyval_name(keyval: int) -> str: ...
def keyval_to_lower(keyval: int) -> int: ...
def keyval_to_unicode(keyval: int) -> str: ...
def keyval_to_upper(keyval: int) -> int: ...
def main() -> None: ...
def quit() -> None: ...
def set_display(display: str) -> None: ...
def set_log_handler(verbose: bool) -> None: ...
def unicode_to_keyval(wc: str) -> int: ...
def unset_log_handler() -> None: ...
def write_address(address: str) -> None: ...
def xml_parse_buffer(buffer: str) -> XML: ...
def xml_parse_file(name: str) -> XML: ...

class AttrList(Serializable):
    """
    :Constructors:

    ::

        AttrList(**properties)
        new() -> IBus.AttrList

    Object IBusAttrList

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Serializable
    attributes: list[None]
    def append(self, attr: Attribute) -> None: ...
    def get(self, index: int) -> Attribute: ...
    @classmethod
    def new(cls) -> AttrList: ...

class AttrListClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AttrListClass()
    """

    parent: SerializableClass

class Attribute(Serializable):
    """
    :Constructors:

    ::

        Attribute(**properties)
        new(type:int, value:int, start_index:int, end_index:int) -> IBus.Attribute

    Object IBusAttribute

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Serializable
    type: int
    value: int
    start_index: int
    end_index: int
    def get_attr_type(self) -> int: ...
    def get_end_index(self) -> int: ...
    def get_start_index(self) -> int: ...
    def get_value(self) -> int: ...
    @classmethod
    def new(
        cls, type: int, value: int, start_index: int, end_index: int
    ) -> Attribute: ...

class AttributeClass(GObject.GPointer):
    """
    :Constructors:

    ::

        AttributeClass()
    """

    parent: SerializableClass

class Bus(Object):
    """
    :Constructors:

    ::

        Bus(**properties)
        new() -> IBus.Bus
        new_async() -> IBus.Bus
        new_async_client() -> IBus.Bus

    Object IBusBus

    Signals from IBusBus:
      connected ()
      disconnected ()
      global-engine-changed (gchararray)
      name-owner-changed (gchararray, gchararray, gchararray)
      global-shortcut-key-responded (guchar, gboolean, gboolean)

    Properties from IBusBus:
      connect-async -> gboolean: Connect Async
        Connect asynchronously to the bus
      client-only -> gboolean: ClientOnly
        Client use only

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props(Object.Props):
        client_only: bool
        connect_async: bool

    @property
    def props(self) -> Props: ...
    parent: Object
    @property
    def priv(self) -> BusPrivate: ...
    def __init__(self, client_only: bool = ..., connect_async: bool = ...) -> None: ...
    def add_match(self, rule: str) -> bool: ...
    def add_match_async(
        self,
        rule: str,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def add_match_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def create_input_context(self, client_name: str) -> InputContext: ...
    def create_input_context_async(
        self,
        client_name: str,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def create_input_context_async_finish(
        self, res: Gio.AsyncResult
    ) -> InputContext: ...
    def current_input_context(self) -> str: ...
    def current_input_context_async(
        self,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def current_input_context_async_finish(self, res: Gio.AsyncResult) -> str: ...
    def exit(self, restart: bool) -> bool: ...
    def exit_async(
        self,
        restart: bool,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def exit_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def get_config(self) -> Config: ...
    def get_connection(self) -> Gio.DBusConnection: ...
    def get_engines_by_names(self, names: Sequence[str]) -> list[EngineDesc]: ...
    def get_global_engine(self) -> EngineDesc: ...
    def get_global_engine_async(
        self,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def get_global_engine_async_finish(self, res: Gio.AsyncResult) -> EngineDesc: ...
    def get_ibus_property(self, property_name: str) -> GLib.Variant: ...
    def get_ibus_property_async(
        self,
        property_name: str,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def get_ibus_property_async_finish(self, res: Gio.AsyncResult) -> GLib.Variant: ...
    def get_name_owner(self, name: str) -> str: ...
    def get_name_owner_async(
        self,
        name: str,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def get_name_owner_async_finish(self, res: Gio.AsyncResult) -> str: ...
    def get_service_name(self) -> str: ...
    def get_use_global_engine(self) -> bool: ...
    def get_use_global_engine_async(
        self,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def get_use_global_engine_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def get_use_sys_layout(self) -> bool: ...
    def get_use_sys_layout_async(
        self,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def get_use_sys_layout_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def hello(self) -> str: ...
    def is_connected(self) -> bool: ...
    def is_global_engine_enabled(self) -> bool: ...
    def is_global_engine_enabled_async(
        self,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def is_global_engine_enabled_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def list_active_engines(self) -> list[EngineDesc]: ...
    def list_active_engines_async(
        self,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def list_active_engines_async_finish(
        self, res: Gio.AsyncResult
    ) -> list[EngineDesc]: ...
    def list_engines(self) -> list[EngineDesc]: ...
    def list_engines_async(
        self,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def list_engines_async_finish(self, res: Gio.AsyncResult) -> list[EngineDesc]: ...
    def list_names(self) -> list[str]: ...
    def list_queued_owners(self, name: str) -> list[str]: ...
    def name_has_owner(self, name: str) -> bool: ...
    def name_has_owner_async(
        self,
        name: str,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def name_has_owner_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    @classmethod
    def new(cls) -> Bus: ...
    @classmethod
    def new_async(cls) -> Bus: ...
    @classmethod
    def new_async_client(cls) -> Bus: ...
    def preload_engines(self, names: Sequence[str]) -> bool: ...
    def preload_engines_async(
        self,
        names: Sequence[str],
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def preload_engines_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def register_component(self, component: Component) -> bool: ...
    def register_component_async(
        self,
        component: Component,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def register_component_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def release_name(self, name: str) -> int: ...
    def release_name_async(
        self,
        name: str,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def release_name_async_finish(self, res: Gio.AsyncResult) -> int: ...
    def remove_match(self, rule: str) -> bool: ...
    def remove_match_async(
        self,
        rule: str,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def remove_match_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def request_name(self, name: str, flags: int) -> int: ...
    def request_name_async(
        self,
        name: str,
        flags: int,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def request_name_async_finish(self, res: Gio.AsyncResult) -> int: ...
    def set_global_engine(self, global_engine: str) -> bool: ...
    def set_global_engine_async(
        self,
        global_engine: str,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def set_global_engine_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def set_global_shortcut_keys(
        self, gtype: BusGlobalBindingType, keys: Sequence[ProcessKeyEventData]
    ) -> bool: ...
    def set_global_shortcut_keys_async(
        self,
        gtype: BusGlobalBindingType,
        keys: Sequence[ProcessKeyEventData],
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def set_global_shortcut_keys_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def set_ibus_property(self, property_name: str, value: GLib.Variant) -> None: ...
    def set_ibus_property_async(
        self,
        property_name: str,
        value: GLib.Variant,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def set_ibus_property_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def set_watch_dbus_signal(self, watch: bool) -> None: ...
    def set_watch_ibus_signal(self, watch: bool) -> None: ...

class BusClass(GObject.GPointer):
    """
    :Constructors:

    ::

        BusClass()
    """

    parent: ObjectClass

class BusPrivate(GObject.GPointer): ...

class Component(Serializable):
    """
    :Constructors:

    ::

        Component(**properties)
        new(name:str, description:str, version:str, license:str, author:str, homepage:str, command_line:str, textdomain:str) -> IBus.Component
        new_from_file(filename:str) -> IBus.Component
        new_from_xml_node(node:IBus.XML) -> IBus.Component

    Object IBusComponent

    Properties from IBusComponent:
      name -> gchararray: component name
        The name of component
      description -> gchararray: component description
        The description of component
      version -> gchararray: component version
        The version of component
      license -> gchararray: component license
        The license of component
      author -> gchararray: component author
        The author of component
      homepage -> gchararray: component homepage
        The homepage of component
      command-line -> gchararray: component command-line
        The command line of component
      textdomain -> gchararray: component textdomain
        The textdomain path of component

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props(Serializable.Props):
        author: str
        command_line: str
        description: str
        homepage: str
        license: str
        name: str
        textdomain: str
        version: str

    @property
    def props(self) -> Props: ...
    parent: Serializable
    @property
    def priv(self) -> ComponentPrivate: ...
    pdummy: list[None]
    def __init__(
        self,
        author: str = ...,
        command_line: str = ...,
        description: str = ...,
        homepage: str = ...,
        license: str = ...,
        name: str = ...,
        textdomain: str = ...,
        version: str = ...,
    ) -> None: ...
    def add_engine(self, engine=None, **kwargs): ...  # FIXME Function
    def add_observed_path(self, path: str, access_fs: bool) -> None: ...
    def check_modification(self) -> bool: ...
    def get_author(self) -> str: ...
    def get_description(self) -> str: ...
    def get_engines(self) -> list[EngineDesc]: ...
    def get_exec(self) -> str: ...
    def get_homepage(self) -> str: ...
    def get_license(self) -> str: ...
    def get_name(self) -> str: ...
    def get_observed_paths(self) -> list[ObservedPath]: ...
    def get_textdomain(self) -> str: ...
    def get_version(self) -> str: ...
    @classmethod
    def new(
        cls,
        name: str,
        description: str,
        version: str,
        license: str,
        author: str,
        homepage: str,
        command_line: str,
        textdomain: str,
    ) -> Component: ...
    @classmethod
    def new_from_file(cls, filename: str) -> Component: ...
    @classmethod
    def new_from_xml_node(cls, node: XML) -> Component: ...
    def output(self, output: GLib.String, indent: int) -> None: ...
    def output_engines(self, output: GLib.String, indent: int) -> None: ...

class ComponentClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ComponentClass()
    """

    parent: SerializableClass

class ComponentPrivate(GObject.GPointer): ...

class Config(Proxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable):
    """
    :Constructors:

    ::

        Config(**properties)
        new(connection:Gio.DBusConnection, cancellable:Gio.Cancellable=None) -> IBus.Config
        new_async_finish(res:Gio.AsyncResult) -> IBus.Config

    Object IBusConfig

    Signals from IBusConfig:
      value-changed (gchararray, gchararray, GVariant)

    Signals from IBusProxy:
      destroy ()

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
      g-bus-type -> GBusType: g-bus-type
      g-name -> gchararray: g-name
      g-name-owner -> gchararray: g-name-owner
      g-flags -> GDBusProxyFlags: g-flags
      g-object-path -> gchararray: g-object-path
      g-interface-name -> gchararray: g-interface-name
      g-default-timeout -> gint: g-default-timeout
      g-interface-info -> GDBusInterfaceInfo: g-interface-info

    Signals from GObject:
      notify (GParam)
    """

    class Props(Proxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    parent: Proxy
    @property
    def priv(self) -> ConfigPrivate: ...
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
    ) -> None: ...
    def get_value(self, section, name, default=None): ...  # FIXME Function
    def get_value_async(
        self,
        section: str,
        name: str,
        timeout_ms: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def get_value_async_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    def get_values(self, section: str) -> GLib.Variant: ...
    def get_values_async(
        self,
        section: str,
        timeout_ms: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def get_values_async_finish(self, result: Gio.AsyncResult) -> GLib.Variant: ...
    @classmethod
    def new(
        cls,
        connection: Gio.DBusConnection,
        cancellable: Gio.Cancellable | None = None,
    ) -> Config: ...
    @staticmethod
    def new_async(
        connection: Gio.DBusConnection,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_async_finish(cls, res: Gio.AsyncResult) -> Config: ...
    def set_value(self, section, name, value): ...  # FIXME Function
    def set_value_async(
        self,
        section: str,
        name: str,
        value: GLib.Variant,
        timeout_ms: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def set_value_async_finish(self, result: Gio.AsyncResult) -> bool: ...
    def unset(self, section: str, name: str) -> bool: ...
    def unwatch(self, section: str | None = None, name: str | None = None) -> bool: ...
    def watch(self, section: str | None = None, name: str | None = None) -> bool: ...

class ConfigClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ConfigClass()
    """

    parent: ProxyClass

class ConfigPrivate(GObject.GPointer): ...

class ConfigService(Service):
    """
    :Constructors:

    ::

        ConfigService(**properties)
        new(connection:Gio.DBusConnection) -> IBus.ConfigService

    Object IBusConfigService

    Properties from IBusService:
      object-path -> gchararray: object path
        The path of service object
      connection -> GDBusConnection: connection
        The connection of service object

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props(Service.Props):
        connection: Gio.DBusConnection
        object_path: str

    @property
    def props(self) -> Props: ...
    parent: Service
    def __init__(
        self, connection: Gio.DBusConnection = ..., object_path: str = ...
    ) -> None: ...
    def do_get_value(self, section: str, name: str) -> GLib.Variant: ...
    def do_get_values(self, section: str) -> GLib.Variant: ...
    def do_set_value(self, section: str, name: str, value: GLib.Variant) -> bool: ...
    def do_unset_value(self, section: str, name: str) -> bool: ...
    @classmethod
    def new(cls, connection: Gio.DBusConnection) -> ConfigService: ...
    def value_changed(self, section: str, name: str, value: GLib.Variant) -> None: ...

class ConfigServiceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ConfigServiceClass()
    """

    parent: ServiceClass
    set_value: Callable[[ConfigService, str, str, GLib.Variant], bool]
    get_value: Callable[[ConfigService, str, str], GLib.Variant]
    unset_value: Callable[[ConfigService, str, str], bool]
    get_values: Callable[[ConfigService, str], GLib.Variant]
    pdummy: list[None]

class EmojiData(Serializable):
    """
    :Constructors:

    ::

        EmojiData(**properties)

    Object IBusEmojiData

    Properties from IBusEmojiData:
      emoji -> gchararray: emoji character
        The emoji character UTF-8
      annotations -> gpointer: emoji annotations
        The emoji annotation list
      description -> gchararray: emoji description
        The emoji description
      category -> gchararray: emoji category
        The emoji category

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props(Serializable.Props):
        annotations: None
        category: str
        description: str
        emoji: str

    @property
    def props(self) -> Props: ...
    parent: Serializable
    @property
    def priv(self) -> EmojiDataPrivate: ...
    def __init__(
        self,
        annotations: None = ...,
        category: str = ...,
        description: str = ...,
        emoji: str = ...,
    ) -> None: ...
    def get_annotations(self) -> list[str]: ...
    def get_category(self) -> str: ...
    def get_description(self) -> str: ...
    def get_emoji(self) -> str: ...
    @staticmethod
    def load(path: str) -> list[EmojiData]: ...
    @staticmethod
    def save(path: str, list: list[EmojiData]) -> None: ...
    def set_annotations(self, annotations: list[str]) -> None: ...
    def set_description(self, description: str) -> None: ...

class EmojiDataClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EmojiDataClass()
    """

    parent: SerializableClass

class EmojiDataPrivate(GObject.GPointer): ...

class Engine(Service):
    """
    :Constructors:

    ::

        Engine(**properties)
        new(engine_name:str, object_path:str, connection:Gio.DBusConnection) -> IBus.Engine
        new_with_type(engine_type:GType, engine_name:str, object_path:str, connection:Gio.DBusConnection) -> IBus.Engine

    Object IBusEngine

    Signals from IBusEngine:
      process-key-event (guint, guint, guint) -> gboolean
      focus-in ()
      focus-in-id (gchararray, gchararray)
      focus-out ()
      focus-out-id (gchararray)
      reset ()
      enable ()
      disable ()
      set-cursor-location (gint, gint, gint, gint)
      set-capabilities (guint)
      page-up ()
      page-down ()
      cursor-up ()
      cursor-down ()
      candidate-clicked (guint, guint, guint)
      property-activate (gchararray, guint)
      property-show (gchararray)
      property-hide (gchararray)
      process-hand-writing-event (gpointer, guint)
      cancel-hand-writing (guint)
      set-surrounding-text (GObject, guint, guint)
      set-content-type (guint, guint)

    Properties from IBusEngine:
      engine-name -> gchararray: engine name
        engine name
      has-focus-id -> gboolean: has focus id
        Has focus ID
      active-surrounding-text -> gboolean: enable surrounding text update by focus event
        Enable surrounding text update by focus event

    Properties from IBusService:
      object-path -> gchararray: object path
        The path of service object
      connection -> GDBusConnection: connection
        The connection of service object

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props(Service.Props):
        active_surrounding_text: bool
        engine_name: str
        has_focus_id: bool
        connection: Gio.DBusConnection
        object_path: str

    @property
    def props(self) -> Props: ...
    parent: Service
    @property
    def priv(self) -> EnginePrivate: ...
    enabled: bool
    has_focus: bool
    cursor_area: Rectangle
    client_capabilities: int
    def __init__(
        self,
        active_surrounding_text: bool = ...,
        engine_name: str = ...,
        has_focus_id: bool = ...,
        connection: Gio.DBusConnection = ...,
        object_path: str = ...,
    ) -> None: ...
    def commit_text(self, text: Text) -> None: ...
    def delete_surrounding_text(self, offset: int, nchars: int) -> None: ...
    def do_cancel_hand_writing(self, n_strokes: int) -> None: ...
    def do_candidate_clicked(self, index: int, button: int, state: int) -> None: ...
    def do_cursor_down(self) -> None: ...
    def do_cursor_up(self) -> None: ...
    def do_disable(self) -> None: ...
    def do_enable(self) -> None: ...
    def do_focus_in(self) -> None: ...
    def do_focus_in_id(self, object_path: str, client: str) -> None: ...
    def do_focus_out(self) -> None: ...
    def do_focus_out_id(self, object_path: str) -> None: ...
    def do_page_down(self) -> None: ...
    def do_page_up(self) -> None: ...
    def do_process_hand_writing_event(
        self, coordinates: float, coordinates_len: int
    ) -> None: ...
    def do_process_key_event(self, keyval: int, keycode: int, state: int) -> bool: ...
    def do_property_activate(self, prop_name: str, prop_state: int) -> None: ...
    def do_property_hide(self, prop_name: str) -> None: ...
    def do_property_show(self, prop_name: str) -> None: ...
    def do_reset(self) -> None: ...
    def do_set_capabilities(self, caps: int) -> None: ...
    def do_set_content_type(self, purpose: int, hints: int) -> None: ...
    def do_set_cursor_location(self, x: int, y: int, w: int, h: int) -> None: ...
    def do_set_surrounding_text(
        self, text: Text, cursor_index: int, anchor_pos: int
    ) -> None: ...
    def forward_key_event(self, keyval: int, keycode: int, state: int) -> None: ...
    def get_content_type(self) -> tuple[int, int]: ...
    def get_name(self) -> str: ...
    def get_surrounding_text(self) -> tuple[Text, int, int]: ...
    def hide_auxiliary_text(self) -> None: ...
    def hide_lookup_table(self) -> None: ...
    def hide_preedit_text(self) -> None: ...
    @classmethod
    def new(
        cls, engine_name: str, object_path: str, connection: Gio.DBusConnection
    ) -> Engine: ...
    @classmethod
    def new_with_type(
        cls,
        engine_type: type[Any],
        engine_name: str,
        object_path: str,
        connection: Gio.DBusConnection,
    ) -> Engine: ...
    def register_properties(self, prop_list: PropList) -> None: ...
    def show_auxiliary_text(self) -> None: ...
    def show_lookup_table(self) -> None: ...
    def show_preedit_text(self) -> None: ...
    def update_auxiliary_text(self, text: Text, visible: bool) -> None: ...
    def update_lookup_table(self, lookup_table: LookupTable, visible: bool) -> None: ...
    def update_lookup_table_fast(
        self, lookup_table: LookupTable, visible: bool
    ) -> None: ...
    def update_preedit_text(
        self, text: Text, cursor_pos: int, visible: bool
    ) -> None: ...
    def update_preedit_text_with_mode(
        self, text: Text, cursor_pos: int, visible: bool, mode: PreeditFocusMode
    ) -> None: ...
    def update_property(self, prop: Property) -> None: ...

class EngineClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EngineClass()
    """

    parent: ServiceClass
    process_key_event: Callable[[Engine, int, int, int], bool]
    focus_in: Callable[[Engine], None]
    focus_out: Callable[[Engine], None]
    reset: Callable[[Engine], None]
    enable: Callable[[Engine], None]
    disable: Callable[[Engine], None]
    set_cursor_location: Callable[[Engine, int, int, int, int], None]
    set_capabilities: Callable[[Engine, int], None]
    page_up: Callable[[Engine], None]
    page_down: Callable[[Engine], None]
    cursor_up: Callable[[Engine], None]
    cursor_down: Callable[[Engine], None]
    property_activate: Callable[[Engine, str, int], None]
    property_show: Callable[[Engine, str], None]
    property_hide: Callable[[Engine, str], None]
    candidate_clicked: Callable[[Engine, int, int, int], None]
    set_surrounding_text: Callable[[Engine, Text, int, int], None]
    process_hand_writing_event: Callable[[Engine, float, int], None]
    cancel_hand_writing: Callable[[Engine, int], None]
    set_content_type: Callable[[Engine, int, int], None]
    focus_in_id: Callable[[Engine, str, str], None]
    focus_out_id: Callable[[Engine, str], None]
    pdummy: list[None]

class EngineDesc(Serializable):
    """
    :Constructors:

    ::

        EngineDesc(**properties)
        new(name:str, longname:str, description:str, language:str, license:str, author:str, icon:str, layout:str) -> IBus.EngineDesc
        new_from_xml_node(node:IBus.XML) -> IBus.EngineDesc

    Object IBusEngineDesc

    Properties from IBusEngineDesc:
      name -> gchararray: description name
        The name of engine description
      longname -> gchararray: description longname
        The longname of engine description
      description -> gchararray: description description
        The description of engine description
      language -> gchararray: description language
        The language of engine description
      license -> gchararray: description license
        The license of engine description
      author -> gchararray: description author
        The author of engine description
      icon -> gchararray: description icon
        The icon of engine description
      layout -> gchararray: description layout
        The layout of engine description
      layout-variant -> gchararray: description keyboard variant
        The keyboard variant of engine description
      layout-option -> gchararray: description keyboard option
        The keyboard option of engine description
      rank -> guint: description rank
        The rank of engine description
      hotkeys -> gchararray: description hotkeys
        The hotkeys of engine description
      symbol -> gchararray: description symbol
        The icon symbol chars of engine description
      setup -> gchararray: setup args
        The exec lists of the engine setup command
      version -> gchararray: version number
        The version number of engine description
      textdomain -> gchararray: textdomain
        The textdomain of engine description
      icon-prop-key -> gchararray: icon property key
        The key of IBusProperty for the dynamic panel icon

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props(Serializable.Props):
        author: str
        description: str
        hotkeys: str
        icon: str
        icon_prop_key: str
        language: str
        layout: str
        layout_option: str
        layout_variant: str
        license: str
        longname: str
        name: str
        rank: int
        setup: str
        symbol: str
        textdomain: str
        version: str

    @property
    def props(self) -> Props: ...
    parent: Serializable
    @property
    def priv(self) -> EngineDescPrivate: ...
    def __init__(
        self,
        author: str = ...,
        description: str = ...,
        hotkeys: str = ...,
        icon: str = ...,
        icon_prop_key: str = ...,
        language: str = ...,
        layout: str = ...,
        layout_option: str = ...,
        layout_variant: str = ...,
        license: str = ...,
        longname: str = ...,
        name: str = ...,
        rank: int = ...,
        setup: str = ...,
        symbol: str = ...,
        textdomain: str = ...,
        version: str = ...,
    ) -> None: ...
    def get_author(self) -> str: ...
    def get_description(self) -> str: ...
    def get_hotkeys(self) -> str: ...
    def get_icon(self) -> str: ...
    def get_icon_prop_key(self) -> str: ...
    def get_language(self) -> str: ...
    def get_layout(self) -> str: ...
    def get_layout_option(self) -> str: ...
    def get_layout_variant(self) -> str: ...
    def get_license(self) -> str: ...
    def get_longname(self) -> str: ...
    def get_name(self) -> str: ...
    def get_rank(self) -> int: ...
    def get_setup(self) -> str: ...
    def get_symbol(self) -> str: ...
    def get_textdomain(self) -> str: ...
    def get_version(self) -> str: ...
    @classmethod
    def new(
        cls,
        name: str,
        longname: str,
        description: str,
        language: str,
        license: str,
        author: str,
        icon: str,
        layout: str,
    ) -> EngineDesc: ...
    @classmethod
    def new_from_xml_node(cls, node: XML) -> EngineDesc: ...
    def output(self, output: GLib.String, indent: int) -> None: ...

class EngineDescClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EngineDescClass()
    """

    parent: SerializableClass

class EngineDescPrivate(GObject.GPointer): ...
class EnginePrivate(GObject.GPointer): ...

class EngineSimple(Engine):
    """
    :Constructors:

    ::

        EngineSimple(**properties)

    Object IBusEngineSimple

    Signals from IBusEngine:
      process-key-event (guint, guint, guint) -> gboolean
      focus-in ()
      focus-in-id (gchararray, gchararray)
      focus-out ()
      focus-out-id (gchararray)
      reset ()
      enable ()
      disable ()
      set-cursor-location (gint, gint, gint, gint)
      set-capabilities (guint)
      page-up ()
      page-down ()
      cursor-up ()
      cursor-down ()
      candidate-clicked (guint, guint, guint)
      property-activate (gchararray, guint)
      property-show (gchararray)
      property-hide (gchararray)
      process-hand-writing-event (gpointer, guint)
      cancel-hand-writing (guint)
      set-surrounding-text (GObject, guint, guint)
      set-content-type (guint, guint)

    Properties from IBusEngine:
      engine-name -> gchararray: engine name
        engine name
      has-focus-id -> gboolean: has focus id
        Has focus ID
      active-surrounding-text -> gboolean: enable surrounding text update by focus event
        Enable surrounding text update by focus event

    Properties from IBusService:
      object-path -> gchararray: object path
        The path of service object
      connection -> GDBusConnection: connection
        The connection of service object

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props(Engine.Props):
        active_surrounding_text: bool
        engine_name: str
        has_focus_id: bool
        connection: Gio.DBusConnection
        object_path: str

    @property
    def props(self) -> Props: ...
    parent: Engine
    @property
    def priv(self) -> EngineSimplePrivate: ...
    def __init__(
        self,
        active_surrounding_text: bool = ...,
        engine_name: str = ...,
        has_focus_id: bool = ...,
        connection: Gio.DBusConnection = ...,
        object_path: str = ...,
    ) -> None: ...
    def add_compose_file(self, file: str) -> bool: ...
    def add_table(self, data: Sequence[int], max_seq_len: int, n_seqs: int) -> None: ...
    def add_table_by_locale(self, locale: str | None = None) -> bool: ...

class EngineSimpleClass(GObject.GPointer):
    """
    :Constructors:

    ::

        EngineSimpleClass()
    """

    parent: EngineClass
    pdummy: list[None]

class EngineSimplePrivate(GObject.GPointer): ...

class ExtensionEvent(Serializable):
    """
    :Constructors:

    ::

        ExtensionEvent(**properties)

    Object IBusExtensionEvent

    Properties from IBusExtensionEvent:
      version -> guint: version
        version
      name -> gchararray: name
        name of the extension
      is-enabled -> gboolean: is enabled
        if the extension is enabled
      is-extension -> gboolean: is extension
        if the event is called by an extension
      params -> gchararray: params
        Parameters to enable the extension

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props(Serializable.Props):
        is_enabled: bool
        is_extension: bool
        name: str
        params: str
        version: int

    @property
    def props(self) -> Props: ...
    parent: Serializable
    @property
    def priv(self) -> ExtensionEventPrivate: ...
    def __init__(
        self,
        is_enabled: bool = ...,
        is_extension: bool = ...,
        name: str = ...,
        params: str = ...,
    ) -> None: ...
    def get_name(self) -> str: ...
    def get_params(self) -> str: ...
    def get_version(self) -> int: ...
    def is_enabled(self) -> bool: ...
    def is_extension(self) -> bool: ...

class ExtensionEventClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ExtensionEventClass()
    """

    parent: SerializableClass
    pdummy: list[None]

class ExtensionEventPrivate(GObject.GPointer): ...

class Factory(Service):
    """
    :Constructors:

    ::

        Factory(**properties)
        new(connection:Gio.DBusConnection) -> IBus.Factory

    Object IBusFactory

    Signals from IBusFactory:
      create-engine (gchararray) -> IBusEngine

    Properties from IBusService:
      object-path -> gchararray: object path
        The path of service object
      connection -> GDBusConnection: connection
        The connection of service object

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props(Service.Props):
        connection: Gio.DBusConnection
        object_path: str

    @property
    def props(self) -> Props: ...
    parent: Service
    @property
    def priv(self) -> FactoryPrivate: ...
    def __init__(
        self, connection: Gio.DBusConnection = ..., object_path: str = ...
    ) -> None: ...
    def add_engine(self, engine_name: str, engine_type: type[Any]) -> None: ...
    def create_engine(self, engine_name: str) -> Engine: ...
    def do_create_engine(self, engine_name: str) -> Engine: ...
    @classmethod
    def new(cls, connection: Gio.DBusConnection) -> Factory: ...

class FactoryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        FactoryClass()
    """

    parent: ServiceClass
    create_engine: Callable[[Factory, str], Engine]
    pdummy: list[None]

class FactoryPrivate(GObject.GPointer): ...

class HotkeyProfile(Serializable):
    """
    :Constructors:

    ::

        HotkeyProfile(**properties)
        new() -> IBus.HotkeyProfile

    Object IBusHotkeyProfile

    Signals from IBusHotkeyProfile:
      trigger (guint, gpointer)

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Serializable
    def add_hotkey(self, keyval: int, modifiers: int, event: int) -> bool: ...
    def add_hotkey_from_string(self, str: str, event: int) -> bool: ...
    def do_trigger(self, event: int, *user_data: Any) -> None: ...
    def filter_key_event(
        self,
        keyval: int,
        modifiers: int,
        prev_keyval: int,
        prev_modifiers: int,
        user_data: None,
    ) -> int: ...
    def lookup_hotkey(self, keyval: int, modifiers: int) -> int: ...
    @classmethod
    def new(cls) -> HotkeyProfile: ...
    def remove_hotkey(self, keyval: int, modifiers: int) -> bool: ...
    def remove_hotkey_by_event(self, event: int) -> bool: ...

class HotkeyProfileClass(GObject.GPointer):
    """
    :Constructors:

    ::

        HotkeyProfileClass()
    """

    parent: SerializableClass
    trigger: Callable[..., None]

class InputContext(Proxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable):
    """
    :Constructors:

    ::

        InputContext(**properties)
        new(path:str, connection:Gio.DBusConnection, cancellable:Gio.Cancellable=None) -> IBus.InputContext
        new_async_finish(res:Gio.AsyncResult) -> IBus.InputContext

    Object IBusInputContext

    Signals from IBusInputContext:
      enabled ()
      disabled ()
      commit-text (IBusText)
      forward-key-event (guint, guint, guint)
      delete-surrounding-text (gint, guint)
      update-preedit-text (IBusText, guint, gboolean)
      update-preedit-text-with-mode (IBusText, guint, gboolean, guint)
      show-preedit-text ()
      hide-preedit-text ()
      update-auxiliary-text (IBusText, gboolean)
      show-auxiliary-text ()
      hide-auxiliary-text ()
      update-lookup-table (IBusLookupTable, gboolean)
      show-lookup-table ()
      hide-lookup-table ()
      page-up-lookup-table ()
      page-down-lookup-table ()
      cursor-up-lookup-table ()
      cursor-down-lookup-table ()
      register-properties (IBusPropList)
      update-property (IBusProperty)
      require-surrounding-text ()

    Signals from IBusProxy:
      destroy ()

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
      g-bus-type -> GBusType: g-bus-type
      g-name -> gchararray: g-name
      g-name-owner -> gchararray: g-name-owner
      g-flags -> GDBusProxyFlags: g-flags
      g-object-path -> gchararray: g-object-path
      g-interface-name -> gchararray: g-interface-name
      g-default-timeout -> gint: g-default-timeout
      g-interface-info -> GDBusInterfaceInfo: g-interface-info

    Signals from GObject:
      notify (GParam)
    """

    class Props(Proxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    parent: Proxy
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
    ) -> None: ...
    def cancel_hand_writing(self, n_strokes: int) -> None: ...
    def focus_in(self) -> None: ...
    def focus_out(self) -> None: ...
    def get_engine(self) -> EngineDesc: ...
    def get_engine_async(
        self,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def get_engine_async_finish(self, res: Gio.AsyncResult) -> EngineDesc: ...
    @staticmethod
    def get_input_context(
        path: str, connection: Gio.DBusConnection
    ) -> InputContext: ...
    @staticmethod
    def get_input_context_async(
        path: str,
        connection: Gio.DBusConnection,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @staticmethod
    def get_input_context_async_finish(res: Gio.AsyncResult) -> InputContext: ...
    def needs_surrounding_text(self) -> bool: ...
    @classmethod
    def new(
        cls,
        path: str,
        connection: Gio.DBusConnection,
        cancellable: Gio.Cancellable | None = None,
    ) -> InputContext: ...
    @staticmethod
    def new_async(
        path: str,
        connection: Gio.DBusConnection,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    @classmethod
    def new_async_finish(cls, res: Gio.AsyncResult) -> InputContext: ...
    def post_process_key_event(self) -> None: ...
    def process_hand_writing_event(
        self, coordinates: float, coordinates_len: int
    ) -> None: ...
    def process_key_event(self, keyval: int, keycode: int, state: int) -> bool: ...
    def process_key_event_async(
        self,
        keyval: int,
        keycode: int,
        state: int,
        timeout_msec: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def process_key_event_async_finish(self, res: Gio.AsyncResult) -> bool: ...
    def property_activate(self, prop_name: str, state: int) -> None: ...
    def reset(self) -> None: ...
    def set_capabilities(self, capabilities: int) -> None: ...
    def set_client_commit_preedit(self, client_commit: bool) -> None: ...
    def set_content_type(self, purpose: int, hints: int) -> None: ...
    def set_cursor_location(self, x: int, y: int, w: int, h: int) -> None: ...
    def set_cursor_location_relative(self, x: int, y: int, w: int, h: int) -> None: ...
    def set_engine(self, name: str) -> None: ...
    def set_post_process_key_event(self, enable: bool) -> None: ...
    def set_surrounding_text(
        self, text: Text, cursor_pos: int, anchor_pos: int
    ) -> None: ...

class InputContextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        InputContextClass()
    """

    parent: ProxyClass
    pdummy: list[None]

class Keymap(Object):
    """
    :Constructors:

    ::

        Keymap(**properties)
        new(name:str) -> IBus.Keymap

    Object IBusKeymap

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Object
    name: str
    keymap: list[int]
    @staticmethod
    def get(name: str) -> Keymap: ...
    def lookup_keysym(self, keycode: int, state: int) -> int: ...
    @classmethod
    def new(cls, name: str) -> Keymap: ...

class KeymapClass(GObject.GPointer):
    """
    :Constructors:

    ::

        KeymapClass()
    """

    parent: ObjectClass

class LookupTable(Serializable):
    """
    :Constructors:

    ::

        LookupTable(**properties)
        new(page_size:int, cursor_pos:int, cursor_visible:bool, round:bool) -> IBus.LookupTable

    Object IBusLookupTable

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Serializable
    page_size: int
    cursor_pos: int
    cursor_visible: bool
    round: bool
    orientation: int
    candidates: list[None]
    labels: list[None]
    def append_candidate(self, text: Text) -> None: ...
    def append_label(self, text: Text) -> None: ...
    def clean(self): ...  # FIXME Function
    def clear(self) -> None: ...
    def cursor_down(self) -> bool: ...
    def cursor_up(self) -> bool: ...
    def get_candidate(self, index: int) -> Text: ...
    def get_cursor_in_page(self) -> int: ...
    def get_cursor_pos(self) -> int: ...
    def get_label(self, index: int) -> Text: ...
    def get_number_of_candidates(self) -> int: ...
    def get_orientation(self) -> int: ...
    def get_page_size(self) -> int: ...
    def is_cursor_visible(self) -> bool: ...
    def is_round(self) -> bool: ...
    @classmethod
    def new(
        cls, page_size: int, cursor_pos: int, cursor_visible: bool, round: bool
    ) -> LookupTable: ...
    def page_down(self) -> bool: ...
    def page_up(self) -> bool: ...
    def set_cursor_pos(self, cursor_pos: int) -> None: ...
    def set_cursor_visible(self, visible: bool) -> None: ...
    def set_label(self, index: int, text: Text) -> None: ...
    def set_orientation(self, orientation: int) -> None: ...
    def set_page_size(self, page_size: int) -> None: ...
    def set_round(self, round: bool) -> None: ...
    def show_cursor(self, visible): ...  # FIXME Function

class LookupTableClass(GObject.GPointer):
    """
    :Constructors:

    ::

        LookupTableClass()
    """

    parent: SerializableClass

class Object(GObject.InitiallyUnowned):
    """
    :Constructors:

    ::

        Object(**properties)
        new() -> IBus.Object

    Object IBusObject

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: GObject.InitiallyUnowned
    flags: int
    @property
    def priv(self) -> ObjectPrivate: ...
    def destroy(self) -> None: ...
    def do_destroy(self) -> None: ...
    @classmethod
    def new(cls) -> Object: ...

class ObjectClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObjectClass()
    """

    parent: GObject.InitiallyUnownedClass
    destroy: Callable[[Object], None]
    pdummy: list[None]

class ObjectPrivate(GObject.GPointer): ...

class ObservedPath(Serializable):
    """
    :Constructors:

    ::

        ObservedPath(**properties)
        new(path:str, fill_stat:bool) -> IBus.ObservedPath
        new_from_xml_node(node:IBus.XML, fill_stat:bool) -> IBus.ObservedPath

    Object IBusObservedPath

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Serializable
    path: str
    mtime: int
    is_dir: bool
    is_exist: bool
    def check_modification(self) -> bool: ...
    @classmethod
    def new(cls, path: str, fill_stat: bool) -> ObservedPath: ...
    @classmethod
    def new_from_xml_node(cls, node: XML, fill_stat: bool) -> ObservedPath: ...
    def output(self, output: GLib.String, indent: int) -> None: ...
    def traverse(self, dir_only: bool) -> list[ObservedPath]: ...

class ObservedPathClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ObservedPathClass()
    """

    parent: SerializableClass

class PanelService(Service):
    """
    :Constructors:

    ::

        PanelService(**properties)
        new(connection:Gio.DBusConnection) -> IBus.PanelService

    Object IBusPanelService

    Signals from IBusPanelService:
      process-key-event (guint, guint, guint) -> gboolean
      focus-in (gchararray)
      focus-out (gchararray)
      reset ()
      set-cursor-location (gint, gint, gint, gint)
      set-content-type (guint, guint)
      update-preedit-text (IBusText, guint, gboolean)
      show-preedit-text ()
      hide-preedit-text ()
      update-auxiliary-text (IBusText, gboolean)
      show-auxiliary-text ()
      hide-auxiliary-text ()
      update-lookup-table (IBusLookupTable, gboolean)
      show-lookup-table ()
      hide-lookup-table ()
      page-up-lookup-table ()
      page-down-lookup-table ()
      cursor-up-lookup-table ()
      cursor-down-lookup-table ()
      register-properties (IBusPropList)
      update-property (IBusProperty)
      set-cursor-location-relative (gint, gint, gint, gint)
      hide-language-bar ()
      show-language-bar ()
      start-setup ()
      state-changed ()
      destroy-context (gchararray)
      panel-extension-received (IBusExtensionEvent)
      commit-text-received (IBusText)
      candidate-clicked-lookup-table (guint, guint, guint)

    Properties from IBusService:
      object-path -> gchararray: object path
        The path of service object
      connection -> GDBusConnection: connection
        The connection of service object

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props(Service.Props):
        connection: Gio.DBusConnection
        object_path: str

    @property
    def props(self) -> Props: ...
    parent: Service
    def __init__(
        self, connection: Gio.DBusConnection = ..., object_path: str = ...
    ) -> None: ...
    def candidate_clicked(self, index: int, button: int, state: int) -> None: ...
    def commit_text(self, text: Text) -> None: ...
    def cursor_down(self) -> None: ...
    def cursor_up(self) -> None: ...
    def do_candidate_clicked_lookup_table(
        self, index: int, button: int, state: int
    ) -> None: ...
    def do_commit_text_received(self, text: Text) -> None: ...
    def do_cursor_down_lookup_table(self) -> None: ...
    def do_cursor_up_lookup_table(self) -> None: ...
    def do_destroy_context(self, input_context_path: str) -> None: ...
    def do_focus_in(self, input_context_path: str) -> None: ...
    def do_focus_out(self, input_context_path: str) -> None: ...
    def do_hide_auxiliary_text(self) -> None: ...
    def do_hide_language_bar(self) -> None: ...
    def do_hide_lookup_table(self) -> None: ...
    def do_hide_preedit_text(self) -> None: ...
    def do_page_down_lookup_table(self) -> None: ...
    def do_page_up_lookup_table(self) -> None: ...
    def do_panel_extension_received(self, event: ExtensionEvent) -> None: ...
    def do_process_key_event(self, keyval: int, keycode: int, state: int) -> bool: ...
    def do_register_properties(self, prop_list: PropList) -> None: ...
    def do_reset(self) -> None: ...
    def do_set_content_type(self, purpose: int, hints: int) -> None: ...
    def do_set_cursor_location(self, x: int, y: int, w: int, h: int) -> None: ...
    def do_set_cursor_location_relative(
        self, x: int, y: int, w: int, h: int
    ) -> None: ...
    def do_show_auxiliary_text(self) -> None: ...
    def do_show_language_bar(self) -> None: ...
    def do_show_lookup_table(self) -> None: ...
    def do_show_preedit_text(self) -> None: ...
    def do_start_setup(self) -> None: ...
    def do_state_changed(self) -> None: ...
    def do_update_auxiliary_text(self, text: Text, visible: bool) -> None: ...
    def do_update_lookup_table(
        self, lookup_table: LookupTable, visible: bool
    ) -> None: ...
    def do_update_preedit_text(
        self, text: Text, cursor_pos: int, visible: bool
    ) -> None: ...
    def do_update_property(self, prop: Property) -> None: ...
    def hide_preedit_text_received(self) -> None: ...
    @classmethod
    def new(cls, connection: Gio.DBusConnection) -> PanelService: ...
    def page_down(self) -> None: ...
    def page_up(self) -> None: ...
    def panel_extension(self, event: ExtensionEvent) -> None: ...
    def property_activate(self, prop_name: str, prop_state: int) -> None: ...
    def property_hide(self, prop_name: str) -> None: ...
    def property_show(self, prop_name: str) -> None: ...
    def show_preedit_text_received(self) -> None: ...
    def update_auxiliary_text_received(self, text: Text, visible: bool) -> None: ...
    def update_lookup_table_received(
        self, table: LookupTable, visible: bool
    ) -> None: ...
    def update_preedit_text_received(
        self, text: Text, cursor_pos: int, visible: bool
    ) -> None: ...

class PanelServiceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PanelServiceClass()
    """

    parent: ServiceClass
    focus_in: Callable[[PanelService, str], None]
    focus_out: Callable[[PanelService, str], None]
    register_properties: Callable[[PanelService, PropList], None]
    set_cursor_location: Callable[[PanelService, int, int, int, int], None]
    update_auxiliary_text: Callable[[PanelService, Text, bool], None]
    update_lookup_table: Callable[[PanelService, LookupTable, bool], None]
    update_preedit_text: Callable[[PanelService, Text, int, bool], None]
    update_property: Callable[[PanelService, Property], None]
    cursor_down_lookup_table: Callable[[PanelService], None]
    cursor_up_lookup_table: Callable[[PanelService], None]
    hide_auxiliary_text: Callable[[PanelService], None]
    hide_language_bar: Callable[[PanelService], None]
    hide_lookup_table: Callable[[PanelService], None]
    hide_preedit_text: Callable[[PanelService], None]
    page_down_lookup_table: Callable[[PanelService], None]
    page_up_lookup_table: Callable[[PanelService], None]
    reset: Callable[[PanelService], None]
    show_auxiliary_text: Callable[[PanelService], None]
    show_language_bar: Callable[[PanelService], None]
    show_lookup_table: Callable[[PanelService], None]
    show_preedit_text: Callable[[PanelService], None]
    start_setup: Callable[[PanelService], None]
    state_changed: Callable[[PanelService], None]
    destroy_context: Callable[[PanelService, str], None]
    set_content_type: Callable[[PanelService, int, int], None]
    set_cursor_location_relative: Callable[[PanelService, int, int, int, int], None]
    panel_extension_received: Callable[[PanelService, ExtensionEvent], None]
    process_key_event: Callable[[PanelService, int, int, int], bool]
    commit_text_received: Callable[[PanelService, Text], None]
    candidate_clicked_lookup_table: Callable[[PanelService, int, int, int], None]
    pdummy: list[None]

class ProcessKeyEventData(GObject.GPointer):
    """
    :Constructors:

    ::

        ProcessKeyEventData()
    """

    keyval: int
    keycode: int
    state: int

class PropList(Serializable):
    """
    :Constructors:

    ::

        PropList(**properties)
        new() -> IBus.PropList

    Object IBusPropList

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Serializable
    properties: list[None]
    def append(self, prop: Property) -> None: ...
    def get(self, index: int) -> Property: ...
    @classmethod
    def new(cls) -> PropList: ...
    def update_property(self, prop: Property) -> bool: ...

class PropListClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PropListClass()
    """

    parent: SerializableClass

class Property(Serializable):
    """
    :Constructors:

    ::

        Property(**properties)
        new(key:str, type:IBus.PropType, label:IBus.Text, icon:str=None, tooltip:IBus.Text, sensitive:bool, visible:bool, state:IBus.PropState, prop_list:IBus.PropList=None) -> IBus.Property

    Object IBusProperty

    Properties from IBusProperty:
      key -> gchararray: key
        The key of property
      icon -> gchararray: icon
        The icon of property
      label -> IBusText: label
        The label of property
      symbol -> IBusText: symbol
        The symbol of property
      tooltip -> IBusText: tooltip
        The tooltip of property
      sensitive -> gboolean: sensitive
        The sensitive of property
      visible -> gboolean: visible
        The visible of property
      prop-type -> IBusPropType: prop-type
        The type of property
      state -> IBusPropState: state
        The state of property
      sub-props -> IBusPropList: sub properties
        The sub properties of property

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props(Serializable.Props):
        icon: str
        key: str
        label: Text
        prop_type: PropType
        sensitive: bool
        state: PropState
        sub_props: PropList
        symbol: Text
        tooltip: Text
        visible: bool

    @property
    def props(self) -> Props: ...
    parent: Serializable
    @property
    def priv(self) -> PropertyPrivate: ...
    pdummy: list[None]
    def __init__(
        self,
        icon: str = ...,
        key: str = ...,
        label: Text = ...,
        prop_type: PropType = ...,
        sensitive: bool = ...,
        state: PropState = ...,
        sub_props: PropList = ...,
        symbol: Text = ...,
        tooltip: Text = ...,
        visible: bool = ...,
    ) -> None: ...
    def get_icon(self) -> str: ...
    def get_key(self) -> str: ...
    def get_label(self) -> Text: ...
    def get_prop_type(self) -> PropType: ...
    def get_sensitive(self) -> bool: ...
    def get_state(self) -> PropState: ...
    def get_sub_props(self) -> PropList: ...
    def get_symbol(self) -> Text: ...
    def get_tooltip(self) -> Text: ...
    def get_visible(self) -> bool: ...
    @classmethod
    def new(
        cls,
        key: str,
        type: PropType,
        label: Text,
        icon: str | None,
        tooltip: Text,
        sensitive: bool,
        visible: bool,
        state: PropState,
        prop_list: PropList | None = None,
    ) -> Property: ...
    def set_icon(self, icon: str) -> None: ...
    def set_label(self, label: Text) -> None: ...
    def set_sensitive(self, sensitive: bool) -> None: ...
    def set_state(self, state: PropState) -> None: ...
    def set_sub_props(self, prop_list: PropList) -> None: ...
    def set_symbol(self, symbol: Text) -> None: ...
    def set_tooltip(self, tooltip: Text) -> None: ...
    def set_visible(self, visible: bool) -> None: ...
    def update(self, prop_update: Property) -> bool: ...

class PropertyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        PropertyClass()
    """

    parent: SerializableClass

class PropertyPrivate(GObject.GPointer): ...

class Proxy(Gio.DBusProxy, Gio.AsyncInitable, Gio.DBusInterface, Gio.Initable):
    """
    :Constructors:

    ::

        Proxy(**properties)

    Object IBusProxy

    Signals from IBusProxy:
      destroy ()

    Signals from GDBusProxy:
      g-properties-changed (GVariant, GStrv)
      g-signal (gchararray, gchararray, GVariant)

    Properties from GDBusProxy:
      g-connection -> GDBusConnection: g-connection
      g-bus-type -> GBusType: g-bus-type
      g-name -> gchararray: g-name
      g-name-owner -> gchararray: g-name-owner
      g-flags -> GDBusProxyFlags: g-flags
      g-object-path -> gchararray: g-object-path
      g-interface-name -> gchararray: g-interface-name
      g-default-timeout -> gint: g-default-timeout
      g-interface-info -> GDBusInterfaceInfo: g-interface-info

    Signals from GObject:
      notify (GParam)
    """

    class Props(Gio.DBusProxy.Props):
        g_connection: Gio.DBusConnection
        g_default_timeout: int
        g_flags: Gio.DBusProxyFlags
        g_interface_info: Gio.DBusInterfaceInfo
        g_interface_name: str
        g_name: str
        g_name_owner: str
        g_object_path: str
        g_bus_type: Gio.BusType

    @property
    def props(self) -> Props: ...
    parent: Gio.DBusProxy
    flags: int
    own: bool
    def __init__(
        self,
        g_bus_type: Gio.BusType = ...,
        g_connection: Gio.DBusConnection = ...,
        g_default_timeout: int = ...,
        g_flags: Gio.DBusProxyFlags = ...,
        g_interface_info: Gio.DBusInterfaceInfo = ...,
        g_interface_name: str = ...,
        g_name: str = ...,
        g_object_path: str = ...,
    ) -> None: ...
    def destroy(self) -> None: ...
    def do_destroy(self) -> None: ...

class ProxyClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ProxyClass()
    """

    parent: Gio.DBusProxyClass
    destroy: Callable[[Proxy], None]
    pdummy: list[None]

class Rectangle(GObject.GPointer):
    """
    :Constructors:

    ::

        Rectangle()
    """

    x: int
    y: int
    width: int
    height: int

class Registry(Serializable):
    """
    :Constructors:

    ::

        Registry(**properties)
        new() -> IBus.Registry

    Object IBusRegistry

    Signals from IBusRegistry:
      changed ()

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Serializable
    @property
    def priv(self) -> RegistryPrivate: ...
    def check_modification(self) -> bool: ...
    def get_components(self) -> list[Component]: ...
    def get_observed_paths(self) -> list[ObservedPath]: ...
    def load(self) -> None: ...
    def load_cache(self, is_user: bool) -> bool: ...
    def load_cache_file(self, filename: str) -> bool: ...
    def load_in_dir(self, dirname: str) -> None: ...
    @classmethod
    def new(cls) -> Registry: ...
    def output(self, output: GLib.String, indent: int) -> None: ...
    def save_cache(self, is_user: bool) -> bool: ...
    def save_cache_file(self, filename: str) -> bool: ...
    def start_monitor_changes(self) -> None: ...

class RegistryClass(GObject.GPointer):
    """
    :Constructors:

    ::

        RegistryClass()
    """

    parent: SerializableClass

class RegistryPrivate(GObject.GPointer): ...

class Serializable(Object):
    """
    :Constructors:

    ::

        Serializable(**properties)
        new() -> IBus.Serializable

    Object IBusSerializable

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Object
    @property
    def priv(self) -> SerializablePrivate: ...
    def copy(self) -> Serializable: ...
    @staticmethod
    def deserialize_object(variant: GLib.Variant) -> Serializable: ...
    def do_copy(self, src: Serializable) -> bool: ...
    def do_deserialize(self, variant: GLib.Variant) -> int: ...
    def do_serialize(self, builder: GLib.VariantBuilder) -> bool: ...
    def get_qattachment(self, key: int) -> GLib.Variant: ...
    @classmethod
    def new(cls) -> Serializable: ...
    def remove_qattachment(self, key: int) -> None: ...
    def serialize_object(self) -> GLib.Variant: ...
    def set_qattachment(self, key: int, value: GLib.Variant) -> None: ...

class SerializableClass(GObject.GPointer):
    """
    :Constructors:

    ::

        SerializableClass()
    """

    parent: ObjectClass
    serialize: Callable[[Serializable, GLib.VariantBuilder], bool]
    deserialize: Callable[[Serializable, GLib.Variant], int]
    copy: Callable[[Serializable, Serializable], bool]
    pdummy: list[None]

class SerializablePrivate(GObject.GPointer): ...

class Service(Object):
    """
    :Constructors:

    ::

        Service(**properties)
        new(connection:Gio.DBusConnection, path:str) -> IBus.Service

    Object IBusService

    Properties from IBusService:
      object-path -> gchararray: object path
        The path of service object
      connection -> GDBusConnection: connection
        The connection of service object

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props(Object.Props):
        connection: Gio.DBusConnection
        object_path: str

    @property
    def props(self) -> Props: ...
    parent: Object
    @property
    def priv(self) -> ServicePrivate: ...
    def __init__(
        self, connection: Gio.DBusConnection = ..., object_path: str = ...
    ) -> None: ...
    def add_interfaces(self, xml_data: str) -> bool: ...
    def do_service_get_property(
        self,
        connection: Gio.DBusConnection,
        sender: str,
        object_path: str,
        interface_name: str,
        property_name: str,
    ) -> GLib.Variant | None: ...
    def do_service_method_call(
        self,
        connection: Gio.DBusConnection,
        sender: str,
        object_path: str,
        interface_name: str,
        method_name: str,
        parameters: GLib.Variant,
        invocation: Gio.DBusMethodInvocation,
    ) -> None: ...
    def do_service_set_property(
        self,
        connection: Gio.DBusConnection,
        sender: str,
        object_path: str,
        interface_name: str,
        property_name: str,
        value: GLib.Variant,
    ) -> bool: ...
    def emit_signal(
        self,
        dest_bus_name: str,
        interface_name: str,
        signal_name: str,
        parameters: GLib.Variant,
    ) -> bool: ...
    def free_interfaces(self, depth: int) -> int: ...
    def get_connection(self) -> Gio.DBusConnection: ...
    def get_object_path(self) -> str: ...
    @classmethod
    def new(cls, connection: Gio.DBusConnection, path: str) -> Service: ...
    def register(self, connection: Gio.DBusConnection) -> bool: ...
    def unregister(self, connection: Gio.DBusConnection) -> None: ...

class ServiceClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ServiceClass()
    """

    parent: ObjectClass
    service_method_call: Callable[
        [
            Service,
            Gio.DBusConnection,
            str,
            str,
            str,
            str,
            GLib.Variant,
            Gio.DBusMethodInvocation,
        ],
        None,
    ]
    service_get_property: Callable[
        [Service, Gio.DBusConnection, str, str, str, str], GLib.Variant | None
    ]
    service_set_property: Callable[
        [Service, Gio.DBusConnection, str, str, str, str, GLib.Variant], bool
    ]
    interfaces: list[None]
    pdummy: list[None]
    def add_interfaces(self, xml_data: str) -> bool: ...
    def free_interfaces(self, depth: int) -> int: ...

class ServicePrivate(GObject.GPointer): ...

class Text(Serializable):
    """
    :Constructors:

    ::

        Text(**properties)
        new_from_string(str:str) -> IBus.Text
        new_from_ucs4(str:str) -> IBus.Text
        new_from_unichar(c:str) -> IBus.Text

    Object IBusText

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    parent: Serializable
    is_static: bool
    text: str
    attrs: AttrList
    def append_attribute(
        self, type: int, value: int, start_index: int, end_index: int
    ) -> None: ...
    def get_attributes(self) -> AttrList: ...
    def get_length(self) -> int: ...
    def get_text(self) -> str: ...
    @classmethod
    def new_from_string(cls, str: str) -> Text: ...
    @classmethod
    def new_from_ucs4(cls, str: str) -> Text: ...
    @classmethod
    def new_from_unichar(cls, c: str) -> Text: ...
    def set_attributes(self, attrs: AttrList) -> None: ...

class TextClass(GObject.GPointer):
    """
    :Constructors:

    ::

        TextClass()
    """

    parent: SerializableClass

class UnicodeBlock(Serializable):
    """
    :Constructors:

    ::

        UnicodeBlock(**properties)

    Object IBusUnicodeBlock

    Properties from IBusUnicodeBlock:
      name -> gchararray: name
        The Unicode name
      start -> guint: start code point
        The Unicode start code point
      end -> guint: end code point
        The Unicode end code point

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props(Serializable.Props):
        end: int
        name: str
        start: int

    @property
    def props(self) -> Props: ...
    parent: Serializable
    @property
    def priv(self) -> UnicodeBlockPrivate: ...
    def __init__(self, end: int = ..., name: str = ..., start: int = ...) -> None: ...
    def get_end(self) -> str: ...
    def get_name(self) -> str: ...
    def get_start(self) -> str: ...
    @staticmethod
    def load(path: str) -> list[UnicodeBlock]: ...
    @staticmethod
    def save(path: str, list: list[UnicodeBlock]) -> None: ...

class UnicodeBlockClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UnicodeBlockClass()
    """

    parent: SerializableClass

class UnicodeBlockPrivate(GObject.GPointer): ...

class UnicodeData(Serializable):
    """
    :Constructors:

    ::

        UnicodeData(**properties)

    Object IBusUnicodeData

    Properties from IBusUnicodeData:
      code -> guint: code point
        The Unicode code point
      name -> gchararray: name
        The Unicode name
      alias -> gchararray: alias name
        The Unicode alias name
      block-name -> gchararray: block name
        The Unicode block name

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props(Serializable.Props):
        alias: str
        block_name: str
        code: int
        name: str

    @property
    def props(self) -> Props: ...
    parent: Serializable
    @property
    def priv(self) -> UnicodeDataPrivate: ...
    def __init__(
        self, alias: str = ..., block_name: str = ..., code: int = ..., name: str = ...
    ) -> None: ...
    def get_alias(self) -> str: ...
    def get_block_name(self) -> str: ...
    def get_code(self) -> str: ...
    def get_name(self) -> str: ...
    @staticmethod
    def load(path: str, object: GObject.Object | None = None) -> list[UnicodeData]: ...
    @staticmethod
    def load_async(
        path: str,
        object: GObject.Object | None,
        cancellable: Gio.Cancellable | None,
        callback: Callable[..., None],
        *user_data: Any,
    ) -> None: ...
    @staticmethod
    def save(path: str, list: list[UnicodeData]) -> None: ...
    def set_block_name(self, block_name: str) -> None: ...

class UnicodeDataClass(GObject.GPointer):
    """
    :Constructors:

    ::

        UnicodeDataClass()
    """

    parent: SerializableClass

class UnicodeDataPrivate(GObject.GPointer): ...

class XEvent(Serializable):
    """
    :Constructors:

    ::

        XEvent(**properties)

    Object IBusXEvent

    Properties from IBusXEvent:
      version -> guint: version
        version
      event-type -> gint: event type
        event type
      window -> guint: window
        window
      send-event -> gint: send event
        send event
      serial -> gulong: serial
        serial
      time -> guint: time
        time
      state -> guint: state
        state
      keyval -> guint: keyval
        keyval
      length -> gint: length
        length
      string -> gchararray: string
        string
      hardware-keycode -> guint: hardware keycode
        hardware keycode
      group -> guint: group
        group
      is-modifier -> gboolean: is modifier
        is modifier
      root -> guint: root
        root
      subwindow -> guint: subwindow
        subwindow
      x -> gint: x
        x
      y -> gint: y
        y
      x-root -> gint: x root
        x root
      y-root -> gint: y root
        y root
      same-screen -> gboolean: same screen
        same screen
      purpose -> gchararray: purpose
        purpose

    Signals from IBusObject:
      destroy ()

    Signals from GObject:
      notify (GParam)
    """

    class Props(Serializable.Props):
        event_type: int
        group: int
        hardware_keycode: int
        is_modifier: bool
        keyval: int
        length: int
        purpose: str
        root: int
        same_screen: bool
        send_event: int
        serial: int
        state: int
        string: str
        subwindow: int
        time: int
        version: int
        window: int
        x: int
        x_root: int
        y: int
        y_root: int

    @property
    def props(self) -> Props: ...
    parent: Serializable
    @property
    def priv(self) -> XEventPrivate: ...
    event_type: XEventType
    window: int
    send_event: int
    serial: int
    def __init__(
        self,
        event_type: int = ...,
        group: int = ...,
        hardware_keycode: int = ...,
        is_modifier: bool = ...,
        keyval: int = ...,
        length: int = ...,
        purpose: str = ...,
        root: int = ...,
        same_screen: bool = ...,
        send_event: int = ...,
        serial: int = ...,
        state: int = ...,
        string: str = ...,
        subwindow: int = ...,
        time: int = ...,
        window: int = ...,
        x: int = ...,
        x_root: int = ...,
        y: int = ...,
        y_root: int = ...,
    ) -> None: ...
    def get_event_type(self) -> XEventType: ...
    def get_group(self) -> int: ...
    def get_hardware_keycode(self) -> int: ...
    def get_is_modifier(self) -> bool: ...
    def get_keyval(self) -> int: ...
    def get_length(self) -> int: ...
    def get_purpose(self) -> str: ...
    def get_root(self) -> int: ...
    def get_same_screen(self) -> bool: ...
    def get_send_event(self) -> int: ...
    def get_serial(self) -> int: ...
    def get_state(self) -> int: ...
    def get_string(self) -> str: ...
    def get_subwindow(self) -> int: ...
    def get_time(self) -> int: ...
    def get_version(self) -> int: ...
    def get_window(self) -> int: ...
    def get_x(self) -> int: ...
    def get_x_root(self) -> int: ...
    def get_y(self) -> int: ...
    def get_y_root(self) -> int: ...

class XEventClass(GObject.GPointer):
    """
    :Constructors:

    ::

        XEventClass()
    """

    parent: SerializableClass
    pdummy: list[None]

class XEventPrivate(GObject.GPointer): ...

class XML(GObject.GBoxed):
    """
    :Constructors:

    ::

        XML()
    """

    name: str
    text: str
    attributes: str
    sub_nodes: list[None]
    def copy(self) -> XML: ...
    def free(self) -> None: ...
    def output(self, output: GLib.String) -> None: ...
    @staticmethod
    def parse_buffer(buffer: str) -> XML: ...
    @staticmethod
    def parse_file(name: str) -> XML: ...

class BusNameFlag(GObject.GFlags):
    ALLOW_REPLACEMENT = 1
    DO_NOT_QUEUE = 4
    REPLACE_EXISTING = 2

class Capabilite(GObject.GFlags):
    AUXILIARY_TEXT = 2
    FOCUS = 8
    LOOKUP_TABLE = 4
    OSK = 64
    PREEDIT_TEXT = 1
    PROPERTY = 16
    SURROUNDING_TEXT = 32
    SYNC_PROCESS_KEY = 128
    SYNC_PROCESS_KEY_V2 = 128

class InputHints(GObject.GFlags):
    EMOJI = 512
    INHIBIT_OSK = 128
    LOWERCASE = 8
    NONE = 0
    NO_EMOJI = 1024
    NO_SPELLCHECK = 2
    PRIVATE = 2048
    SPELLCHECK = 1
    UPPERCASE_CHARS = 16
    UPPERCASE_SENTENCES = 64
    UPPERCASE_WORDS = 32
    VERTICAL_WRITING = 256
    WORD_COMPLETION = 4

class ModifierType(GObject.GFlags):
    BUTTON1_MASK = 256
    BUTTON2_MASK = 512
    BUTTON3_MASK = 1024
    BUTTON4_MASK = 2048
    BUTTON5_MASK = 4096
    CONTROL_MASK = 4
    FORWARD_MASK = 33554432
    HANDLED_MASK = 16777216
    HYPER_MASK = 134217728
    IGNORED_MASK = 33554432
    LOCK_MASK = 2
    META_MASK = 268435456
    MOD1_MASK = 8
    MOD2_MASK = 16
    MOD3_MASK = 32
    MOD4_MASK = 64
    MOD5_MASK = 128
    MODIFIER_MASK = 1593843711
    RELEASE_MASK = 1073741824
    SHIFT_MASK = 1
    SUPER_MASK = 67108864

class ObjectFlags(GObject.GFlags):
    DESTROYED = 2
    IN_DESTRUCTION = 1
    RESERVED_1 = 4
    RESERVED_2 = 8

class AttrPreedit(GObject.GEnum):
    DEFAULT = 0
    ERROR_COMPOSE = 8
    ERROR_SPELLING = 7
    NONE = 1
    PREDICTION = 4
    PREFIX = 5
    SELECTION = 3
    SUFFIX = 6
    WHOLE = 2

class AttrType(GObject.GEnum):
    BACKGROUND = 3
    FOREGROUND = 2
    UNDERLINE = 1

class AttrUnderline(GObject.GEnum):
    DOUBLE = 2
    ERROR = 4
    LOW = 3
    NONE = 0
    SINGLE = 1
    @staticmethod
    def new(underline_type: int, start_index: int, end_index: int) -> Attribute: ...

class BusGlobalBindingType(GObject.GEnum):
    ANY = 0
    EMOJI_TYPING = 2
    IME_SWITCHER = 1

class BusRequestNameReply(GObject.GEnum):
    ALREADY_OWNER = 4
    EXISTS = 3
    IN_QUEUE = 2
    PRIMARY_OWNER = 1

class BusStartServiceByNameReply(GObject.GEnum):
    ALREADY_RUNNING = 2
    SUCCESS = 1

class Error(GObject.GEnum):
    FAILED = 2
    NO_CONFIG = 1
    NO_ENGINE = 0
    @staticmethod
    def quark() -> int: ...

class InputPurpose(GObject.GEnum):
    ALPHA = 1
    DIGITS = 2
    EMAIL = 6
    FREE_FORM = 0
    NAME = 7
    NUMBER = 3
    PASSWORD = 8
    PHONE = 4
    PIN = 9
    TERMINAL = 10
    URL = 5

class Orientation(GObject.GEnum):
    HORIZONTAL = 0
    SYSTEM = 2
    VERTICAL = 1

class PreeditFocusMode(GObject.GEnum):
    CLEAR = 0
    COMMIT = 1

class PropState(GObject.GEnum):
    CHECKED = 1
    INCONSISTENT = 2
    UNCHECKED = 0

class PropType(GObject.GEnum):
    MENU = 3
    NORMAL = 0
    RADIO = 2
    SEPARATOR = 4
    TOGGLE = 1

class XEventType(GObject.GEnum):
    EVENT_LAST = 3
    KEY_PRESS = 0
    KEY_RELEASE = 1
    NOTHING = -1
    OTHER = 2
