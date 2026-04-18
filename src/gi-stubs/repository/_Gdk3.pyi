from typing import Any
from typing import Final
from typing import Protocol
from typing import type_check_only
from typing import TypeVar

from collections.abc import Callable
from collections.abc import Iterator
from collections.abc import Sequence

import cairo
from gi import _gi
from gi.repository import GdkPixbuf
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Pango

T = TypeVar("T")
_SomeSurface = TypeVar("_SomeSurface", bound=cairo.Surface)

BUTTON_MIDDLE: Final[int]
BUTTON_PRIMARY: Final[int]
BUTTON_SECONDARY: Final[int]
CURRENT_TIME: Final[int]
EVENT_PROPAGATE: Final = False
EVENT_STOP: Final = True
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
MAJOR_VERSION: Final[int]
MAX_TIMECOORD_AXES: Final[int]
MICRO_VERSION: Final[int]
MINOR_VERSION: Final[int]
PARENT_RELATIVE: Final[int]
PRIORITY_REDRAW: Final[int]
SELECTION_CLIPBOARD: Final[Atom]
SELECTION_PRIMARY: Final[Atom]
SELECTION_SECONDARY: Final[Atom]
SELECTION_TYPE_ATOM: Final[Atom]
SELECTION_TYPE_BITMAP: Final[Atom]
SELECTION_TYPE_COLORMAP: Final[Atom]
SELECTION_TYPE_DRAWABLE: Final[Atom]
SELECTION_TYPE_INTEGER: Final[Atom]
SELECTION_TYPE_PIXMAP: Final[Atom]
SELECTION_TYPE_STRING: Final[Atom]
SELECTION_TYPE_WINDOW: Final[Atom]
TARGET_BITMAP: Final[Atom]
TARGET_COLORMAP: Final[Atom]
TARGET_DRAWABLE: Final[Atom]
TARGET_PIXMAP: Final[Atom]
TARGET_STRING: Final[Atom]

def add_option_entries_libgtk_only(group: GLib.OptionGroup) -> None: ...
def atom_intern(atom_name: str, only_if_exists: bool) -> Atom: ...
def atom_intern_static_string(atom_name: str) -> Atom: ...
def beep() -> None: ...

# override
def cairo_create(window: Window) -> cairo.Context[cairo.ImageSurface]: ...
def cairo_draw_from_gl(
    cr: cairo.Context[_SomeSurface],
    window: Window,
    source: int,
    source_type: int,
    buffer_scale: int,
    x: int,
    y: int,
    width: int,
    height: int,
) -> None: ...
def cairo_get_clip_rectangle(
    cr: cairo.Context[_SomeSurface],
) -> tuple[bool, Rectangle]: ...
def cairo_get_drawing_context(
    cr: cairo.Context[_SomeSurface],
) -> DrawingContext | None: ...
def cairo_rectangle(cr: cairo.Context[_SomeSurface], rectangle: Rectangle) -> None: ...
def cairo_region(cr: cairo.Context[_SomeSurface], region: cairo.Region) -> None: ...
def cairo_region_create_from_surface(surface: cairo.Surface) -> cairo.Region: ...
def cairo_set_source_color(cr: cairo.Context[_SomeSurface], color: Color) -> None: ...
def cairo_set_source_pixbuf(
    cr: cairo.Context[_SomeSurface],
    pixbuf: GdkPixbuf.Pixbuf,
    pixbuf_x: float,
    pixbuf_y: float,
) -> None: ...
def cairo_set_source_rgba(cr: cairo.Context[_SomeSurface], rgba: RGBA) -> None: ...
def cairo_set_source_window(
    cr: cairo.Context[_SomeSurface], window: Window, x: float, y: float
) -> None: ...

# override
def cairo_surface_create_from_pixbuf(
    pixbuf: GdkPixbuf.Pixbuf, scale: int, for_window: Window | None = None
) -> cairo.ImageSurface: ...
def color_parse(spec: str) -> Color | None: ...  # CHECK Wrapped function
def disable_multidevice() -> None: ...
def drag_abort(context: DragContext, time_: int) -> None: ...
def drag_begin(window: Window, targets: list[Atom]) -> DragContext: ...
def drag_begin_for_device(
    window: Window, device: Device, targets: list[Atom]
) -> DragContext: ...
def drag_begin_from_point(
    window: Window, device: Device, targets: list[Atom], x_root: int, y_root: int
) -> DragContext: ...
def drag_drop(context: DragContext, time_: int) -> None: ...
def drag_drop_done(context: DragContext, success: bool) -> None: ...
def drag_drop_succeeded(context: DragContext) -> bool: ...
def drag_find_window_for_screen(
    context: DragContext, drag_window: Window, screen: Screen, x_root: int, y_root: int
) -> tuple[Window, DragProtocol]: ...
def drag_get_selection(context: DragContext) -> Atom: ...
def drag_motion(
    context: DragContext,
    dest_window: Window,
    protocol: DragProtocol,
    x_root: int,
    y_root: int,
    suggested_action: DragAction,
    possible_actions: DragAction,
    time_: int,
) -> bool: ...
def drag_status(context: DragContext, action: DragAction, time_: int) -> None: ...
def drop_finish(context: DragContext, success: bool, time_: int) -> None: ...
def drop_reply(context: DragContext, accepted: bool, time_: int) -> None: ...
def error_trap_pop() -> int: ...
def error_trap_pop_ignored() -> None: ...
def error_trap_push() -> None: ...
def event_get() -> Event | None: ...
def event_handler_set(func: Callable[..., None], *data: Any) -> None: ...
def event_peek() -> Event | None: ...
def event_request_motions(event: EventMotion) -> None: ...
def events_get_angle(event1: Event, event2: Event) -> tuple[bool, float]: ...
def events_get_center(event1: Event, event2: Event) -> tuple[bool, float, float]: ...
def events_get_distance(event1: Event, event2: Event) -> tuple[bool, float]: ...
def events_pending() -> bool: ...
def flush() -> None: ...
def get_default_root_window() -> Window: ...
def get_display() -> str: ...
def get_display_arg_name() -> str | None: ...
def get_program_class() -> str: ...
def get_show_events() -> bool: ...
def gl_error_quark() -> int: ...
def init() -> list[str]: ...
def init_check() -> tuple[bool, list[str]]: ...
def keyboard_grab(window: Window, owner_events: bool, time_: int) -> GrabStatus: ...
def keyboard_ungrab(time_: int) -> None: ...
def keyval_convert_case(symbol: int) -> tuple[int, int]: ...
def keyval_from_name(keyval_name: str) -> int: ...
def keyval_is_lower(keyval: int) -> bool: ...
def keyval_is_upper(keyval: int) -> bool: ...
def keyval_name(keyval: int) -> str | None: ...
def keyval_to_lower(keyval: int) -> int: ...
def keyval_to_unicode(keyval: int) -> int: ...
def keyval_to_upper(keyval: int) -> int: ...
def list_visuals() -> list[Visual]: ...
def notify_startup_complete() -> None: ...
def notify_startup_complete_with_id(startup_id: str) -> None: ...
def offscreen_window_get_embedder(window: Window) -> Window | None: ...
def offscreen_window_get_surface(window: Window) -> cairo.Surface | None: ...
def offscreen_window_set_embedder(window: Window, embedder: Window) -> None: ...
def pango_context_get() -> Pango.Context: ...
def pango_context_get_for_display(display: Display) -> Pango.Context: ...
def pango_context_get_for_screen(screen: Screen) -> Pango.Context: ...
def parse_args() -> list[str]: ...
def pixbuf_get_from_surface(
    surface: cairo.Surface, src_x: int, src_y: int, width: int, height: int
) -> GdkPixbuf.Pixbuf | None: ...
def pixbuf_get_from_window(
    window: Window, src_x: int, src_y: int, width: int, height: int
) -> GdkPixbuf.Pixbuf | None: ...
def pointer_grab(
    window: Window,
    owner_events: bool,
    event_mask: EventMask,
    confine_to: Window | None,
    cursor: Cursor | None,
    time_: int,
) -> GrabStatus: ...
def pointer_is_grabbed() -> bool: ...
def pointer_ungrab(time_: int) -> None: ...
def pre_parse_libgtk_only() -> None: ...
def property_delete(window: Window, property: Atom) -> None: ...
def property_get(
    window: Window, property: Atom, type: Atom, offset: int, length: int, pdelete: int
) -> tuple[bool, Atom, int, bytes]: ...
def query_depths() -> list[int]: ...
def query_visual_types() -> list[VisualType]: ...
def rectangle_intersect(self, src2: Rectangle) -> tuple[bool, Rectangle]: ...
def rectangle_union(self, src2: Rectangle) -> Rectangle: ...
def selection_convert(
    requestor: Window, selection: Atom, target: Atom, time_: int
) -> None: ...
def selection_owner_get(selection: Atom) -> Window | None: ...
def selection_owner_get_for_display(
    display: Display, selection: Atom
) -> Window | None: ...
def selection_owner_set(
    owner: Window | None, selection: Atom, time_: int, send_event: bool
) -> bool: ...
def selection_owner_set_for_display(
    display: Display,
    owner: Window | None,
    selection: Atom,
    time_: int,
    send_event: bool,
) -> bool: ...
def selection_send_notify(
    requestor: Window, selection: Atom, target: Atom, property: Atom, time_: int
) -> None: ...
def selection_send_notify_for_display(
    display: Display,
    requestor: Window,
    selection: Atom,
    target: Atom,
    property: Atom,
    time_: int,
) -> None: ...
def set_allowed_backends(backends: str) -> None: ...
def set_double_click_time(msec: int) -> None: ...
def set_program_class(program_class: str) -> None: ...
def set_show_events(show_events: bool) -> None: ...
def setting_get(name: str, value: Any) -> bool: ...
def synthesize_window_state(
    window: Window, unset_flags: WindowState, set_flags: WindowState
) -> None: ...
def test_render_sync(window: Window) -> None: ...
def test_simulate_button(
    window: Window,
    x: int,
    y: int,
    button: int,
    modifiers: ModifierType,
    button_pressrelease: EventType,
) -> bool: ...
def test_simulate_key(
    window: Window,
    x: int,
    y: int,
    keyval: int,
    modifiers: ModifierType,
    key_pressrelease: EventType,
) -> bool: ...
def text_property_to_utf8_list_for_display(
    display: Display, encoding: Atom, format: int, text: Sequence[int]
) -> tuple[int, list[str]]: ...
def threads_add_idle(
    priority: int, function: Callable[..., bool], *data: Any
) -> int: ...
def threads_add_timeout(
    priority: int, interval: int, function: Callable[..., bool], *data: Any
) -> int: ...
def threads_add_timeout_seconds(
    priority: int, interval: int, function: Callable[..., bool], *data: Any
) -> int: ...
def threads_enter() -> None: ...
def threads_init() -> None: ...
def threads_leave() -> None: ...
def unicode_to_keyval(wc: int) -> int: ...
def utf8_to_string_target(str: str) -> str | None: ...

class AppLaunchContext(Gio.AppLaunchContext):
    """
    :Constructors:

    ::

        AppLaunchContext(**properties)
        new() -> Gdk.AppLaunchContext

    Object GdkAppLaunchContext

    Properties from GdkAppLaunchContext:
      display -> GdkDisplay: Display
        Display

    Signals from GAppLaunchContext:
      launch-failed (gchararray)
      launch-started (GAppInfo, GVariant)
      launched (GAppInfo, GVariant)

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(Gio.AppLaunchContext.Props):
        @property
        def display(self) -> Display: ...

    @property
    def props(self) -> Props: ...
    def __init__(self, *, display: Display = ...) -> None: ...
    @classmethod
    def new(cls) -> AppLaunchContext: ...
    def set_desktop(self, desktop: int) -> None: ...
    def set_display(self, display: Display) -> None: ...
    def set_icon(self, icon: Gio.Icon | None = None) -> None: ...
    def set_icon_name(self, icon_name: str | None = None) -> None: ...
    def set_screen(self, screen: Screen) -> None: ...
    def set_timestamp(self, timestamp: int) -> None: ...

class Atom(_gi.Struct):
    @staticmethod
    def intern(atom_name: str, only_if_exists: bool) -> Atom: ...
    @staticmethod
    def intern_static_string(atom_name: str) -> Atom: ...
    def name(self) -> str: ...

class Color(GObject.GBoxed):
    """
    :Constructors:

    ::

        Color()
    """

    pixel: int
    red: int
    green: int
    blue: int
    def __init__(
        self, red, green, blue
    ) -> None: ...  # FIXME: Override is missing typing annotation
    MAX_VALUE: Final[int]
    blue_float = ...  # FIXME: Constant is missing typing annotation
    green_float = ...  # FIXME: Constant is missing typing annotation
    red_float = ...  # FIXME: Constant is missing typing annotation

    def copy(self) -> Color: ...
    def equal(self, colorb: Color) -> bool: ...
    def free(self) -> None: ...
    @staticmethod
    def from_floats(red, green, blue):
        """
        Return a new Color object from red/green/blue values from 0.0 to 1.0.
        """  # FIXME: Override is missing typing annotation
    def hash(self) -> int: ...
    @staticmethod
    def parse(spec: str) -> tuple[bool, Color]: ...
    def to_floats(self):
        """
        Return (red_float, green_float, blue_float) triple.
        """  # FIXME: Override is missing typing annotation
    def to_string(self) -> str: ...

class Cursor(GObject.Object):
    """
    :Constructors:

    ::

        Cursor(**properties)
        new(cursor_type:Gdk.CursorType) -> Gdk.Cursor
        new_for_display(display:Gdk.Display, cursor_type:Gdk.CursorType) -> Gdk.Cursor or None
        new_from_name(display:Gdk.Display, name:str) -> Gdk.Cursor or None
        new_from_pixbuf(display:Gdk.Display, pixbuf:GdkPixbuf.Pixbuf, x:int, y:int) -> Gdk.Cursor
        new_from_surface(display:Gdk.Display, surface:cairo.Surface, x:float, y:float) -> Gdk.Cursor

    Object GdkCursor

    Properties from GdkCursor:
      cursor-type -> GdkCursorType: Cursor type
        Standard cursor type
      display -> GdkDisplay: Display
        Display of this cursor

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def cursor_type(self) -> CursorType: ...
        @property
        def display(self) -> Display: ...

    @property
    def props(self) -> Props: ...
    def __init__(
        self, *, cursor_type: CursorType = ..., display: Display = ...
    ) -> None: ...
    def get_cursor_type(self) -> CursorType: ...
    def get_display(self) -> Display: ...
    def get_image(self) -> GdkPixbuf.Pixbuf | None: ...
    def get_surface(self) -> tuple[cairo.Surface | None, float, float]: ...
    @classmethod
    def new(cls, cursor_type: CursorType) -> Cursor: ...
    @classmethod
    def new_for_display(
        cls, display: Display, cursor_type: CursorType
    ) -> Cursor | None: ...
    @classmethod
    def new_from_name(cls, display: Display, name: str) -> Cursor | None: ...
    @classmethod
    def new_from_pixbuf(
        cls, display: Display, pixbuf: GdkPixbuf.Pixbuf, x: int, y: int
    ) -> Cursor: ...
    @classmethod
    def new_from_surface(
        cls, display: Display, surface: cairo.Surface, x: float, y: float
    ) -> Cursor: ...
    def ref(self) -> Cursor: ...
    def unref(self) -> None: ...

class Device(GObject.Object):
    """
    :Constructors:

    ::

        Device(**properties)

    Object GdkDevice

    Signals from GdkDevice:
      changed ()
      tool-changed (GdkDeviceTool)

    Properties from GdkDevice:
      display -> GdkDisplay: Device Display
        Display which the device belongs to
      device-manager -> GdkDeviceManager: Device manager
        Device manager which the device belongs to
      name -> gchararray: Device name
        Device name
      associated-device -> GdkDevice: Associated device
        Associated pointer or keyboard with this device
      type -> GdkDeviceType: Device type
        Device role in the device manager
      input-source -> GdkInputSource: Input source
        Source type for the device
      input-mode -> GdkInputMode: Input mode for the device
        Input mode for the device
      has-cursor -> gboolean: Whether the device has a cursor
        Whether there is a visible cursor following device motion
      n-axes -> guint: Number of axes in the device
        Number of axes in the device
      vendor-id -> gchararray: Vendor ID
        Vendor ID
      product-id -> gchararray: Product ID
        Product ID
      seat -> GdkSeat: Seat
        Seat
      num-touches -> guint: Number of concurrent touches
        Number of concurrent touches
      axes -> GdkAxisFlags: Axes
        Axes
      tool -> GdkDeviceTool: Tool
        The tool that is currently used with this device

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def associated_device(self) -> Device | None: ...
        @property
        def axes(self) -> AxisFlags: ...
        @property
        def device_manager(self) -> DeviceManager: ...
        @property
        def display(self) -> Display: ...
        @property
        def has_cursor(self) -> bool: ...
        input_mode: InputMode
        @property
        def input_source(self) -> InputSource: ...
        @property
        def n_axes(self) -> int: ...
        @property
        def name(self) -> str: ...
        @property
        def num_touches(self) -> int: ...
        @property
        def product_id(self) -> str | None: ...
        seat: Seat
        @property
        def tool(self) -> DeviceTool: ...
        @property
        def type(self) -> DeviceType: ...
        @property
        def vendor_id(self) -> str | None: ...

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        device_manager: DeviceManager = ...,
        display: Display = ...,
        has_cursor: bool = ...,
        input_mode: InputMode = ...,
        input_source: InputSource = ...,
        name: str = ...,
        num_touches: int = ...,
        product_id: str = ...,
        seat: Seat = ...,
        type: DeviceType = ...,
        vendor_id: str = ...,
    ) -> None: ...
    def get_associated_device(self) -> Device | None: ...
    def get_axes(self) -> AxisFlags: ...
    def get_axis_use(self, index_: int) -> AxisUse: ...
    def get_device_type(self) -> DeviceType: ...
    def get_display(self) -> Display: ...
    def get_has_cursor(self) -> bool: ...
    def get_key(self, index_: int) -> tuple[bool, int, ModifierType]: ...
    def get_last_event_window(self) -> Window | None: ...
    def get_mode(self) -> InputMode: ...
    def get_n_axes(self) -> int: ...
    def get_n_keys(self) -> int: ...
    def get_name(self) -> str: ...
    def get_position(self) -> tuple[Screen, int, int]: ...
    def get_position_double(self) -> tuple[Screen, float, float]: ...
    def get_product_id(self) -> str | None: ...
    def get_seat(self) -> Seat: ...
    def get_source(self) -> InputSource: ...
    def get_vendor_id(self) -> str | None: ...
    def get_window_at_position(self) -> tuple[Window | None, int, int]: ...
    def get_window_at_position_double(self) -> tuple[Window | None, float, float]: ...
    def grab(
        self,
        window: Window,
        grab_ownership: GrabOwnership,
        owner_events: bool,
        event_mask: EventMask,
        cursor: Cursor | None,
        time_: int,
    ) -> GrabStatus: ...
    @staticmethod
    def grab_info_libgtk_only(
        display: Display, device: Device
    ) -> tuple[bool, Window, bool]: ...
    def list_axes(self) -> list[Atom]: ...
    def list_slave_devices(self) -> list[Device] | None: ...
    def set_axis_use(self, index_: int, use: AxisUse) -> None: ...
    def set_key(self, index_: int, keyval: int, modifiers: ModifierType) -> None: ...
    def set_mode(self, mode: InputMode) -> bool: ...
    def ungrab(self, time_: int) -> None: ...
    def warp(self, screen: Screen, x: int, y: int) -> None: ...

class DeviceManager(GObject.Object):
    """
    :Constructors:

    ::

        DeviceManager(**properties)

    Object GdkDeviceManager

    Signals from GdkDeviceManager:
      device-added (GdkDevice)
      device-removed (GdkDevice)
      device-changed (GdkDevice)

    Properties from GdkDeviceManager:
      display -> GdkDisplay: Display
        Display for the device manager

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def display(self) -> Display | None: ...

    @property
    def props(self) -> Props: ...
    def __init__(self, *, display: Display = ...) -> None: ...
    def get_client_pointer(self) -> Device: ...
    def get_display(self) -> Display | None: ...
    def list_devices(self, type: DeviceType) -> list[Device]: ...

class DevicePad(GObject.GInterface, Protocol):
    """
    Interface GdkDevicePad

    Signals from GObject:
      notify (GParam)
    """
    def get_feature_group(self, feature: DevicePadFeature, feature_idx: int) -> int: ...
    def get_group_n_modes(self, group_idx: int) -> int: ...
    def get_n_features(self, feature: DevicePadFeature) -> int: ...
    def get_n_groups(self) -> int: ...

class DevicePadInterface(_gi.Struct): ...

class DeviceTool(GObject.Object):
    """
    :Constructors:

    ::

        DeviceTool(**properties)

    Object GdkDeviceTool

    Properties from GdkDeviceTool:
      serial -> guint64: Serial
        Serial number
      tool-type -> GdkDeviceToolType: Tool type
        Tool type
      axes -> GdkAxisFlags: Axes
        Tool axes
      hardware-id -> guint64: Hardware ID
        Hardware ID

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def axes(self) -> AxisFlags: ...
        @property
        def hardware_id(self) -> int: ...
        @property
        def serial(self) -> int: ...
        @property
        def tool_type(self) -> DeviceToolType: ...

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        axes: AxisFlags = ...,
        hardware_id: int = ...,
        serial: int = ...,
        tool_type: DeviceToolType = ...,
    ) -> None: ...
    def get_hardware_id(self) -> int: ...
    def get_serial(self) -> int: ...
    def get_tool_type(self) -> DeviceToolType: ...

class Display(GObject.Object):
    """
    :Constructors:

    ::

        Display(**properties)

    Object GdkDisplay

    Signals from GdkDisplay:
      opened ()
      closed (gboolean)
      seat-added (GdkSeat)
      seat-removed (GdkSeat)
      monitor-added (GdkMonitor)
      monitor-removed (GdkMonitor)

    Signals from GObject:
      notify (GParam)
    """
    def beep(self) -> None: ...
    def close(self) -> None: ...
    def device_is_grabbed(self, device: Device) -> bool: ...
    def flush(self) -> None: ...
    def get_app_launch_context(self) -> AppLaunchContext: ...
    @staticmethod
    def get_default() -> Display | None: ...
    def get_default_cursor_size(self) -> int: ...
    def get_default_group(self) -> Window: ...
    def get_default_screen(self) -> Screen: ...
    def get_default_seat(self) -> Seat: ...
    def get_device_manager(self) -> DeviceManager | None: ...
    def get_event(self) -> Event | None: ...
    def get_maximal_cursor_size(self) -> tuple[int, int]: ...
    def get_monitor(self, monitor_num: int) -> Monitor | None: ...
    def get_monitor_at_point(self, x: int, y: int) -> Monitor: ...
    def get_monitor_at_window(self, window: Window) -> Monitor: ...
    def get_n_monitors(self) -> int: ...
    def get_n_screens(self) -> int: ...
    def get_name(self) -> str: ...
    def get_pointer(self) -> tuple[Screen, int, int, ModifierType]: ...
    def get_primary_monitor(self) -> Monitor | None: ...
    def get_screen(self, screen_num: int) -> Screen: ...
    def get_window_at_pointer(self) -> tuple[Window | None, int, int]: ...
    def has_pending(self) -> bool: ...
    def is_closed(self) -> bool: ...
    def keyboard_ungrab(self, time_: int) -> None: ...
    def list_devices(self) -> list[Device]: ...
    def list_seats(self) -> list[Seat]: ...
    def notify_startup_complete(self, startup_id: str) -> None: ...
    @staticmethod
    def open(display_name: str) -> Display | None: ...
    @staticmethod
    def open_default_libgtk_only() -> Display | None: ...
    def peek_event(self) -> Event | None: ...
    def pointer_is_grabbed(self) -> bool: ...
    def pointer_ungrab(self, time_: int) -> None: ...
    def put_event(self, event: Event) -> None: ...
    def request_selection_notification(self, selection: Atom) -> bool: ...
    def set_double_click_distance(self, distance: int) -> None: ...
    def set_double_click_time(self, msec: int) -> None: ...
    def store_clipboard(
        self,
        clipboard_window: Window,
        time_: int,
        targets: Sequence[Atom] | None = None,
    ) -> None: ...
    def supports_clipboard_persistence(self) -> bool: ...
    def supports_composite(self) -> bool: ...
    def supports_cursor_alpha(self) -> bool: ...
    def supports_cursor_color(self) -> bool: ...
    def supports_input_shapes(self) -> bool: ...
    def supports_selection_notification(self) -> bool: ...
    def supports_shapes(self) -> bool: ...
    def sync(self) -> None: ...
    def warp_pointer(self, screen: Screen, x: int, y: int) -> None: ...

class DisplayManager(GObject.Object):
    """
    :Constructors:

    ::

        DisplayManager(**properties)

    Object GdkDisplayManager

    Signals from GdkDisplayManager:
      display-opened (GdkDisplay)

    Properties from GdkDisplayManager:
      default-display -> GdkDisplay: Default Display
        The default display for GDK

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        default_display: Display | None

    @property
    def props(self) -> Props: ...
    def __init__(self, *, default_display: Display = ...) -> None: ...
    @staticmethod
    def get() -> DisplayManager: ...
    def get_default_display(self) -> Display | None: ...
    def list_displays(self) -> list[Display]: ...
    def open_display(self, name: str) -> Display | None: ...
    def set_default_display(self, display: Display) -> None: ...

class DragContext(GObject.Object):
    """
    :Constructors:

    ::

        DragContext(**properties)

    Object GdkDragContext

    Signals from GdkDragContext:
      cancel (GdkDragCancelReason)
      drop-performed (gint)
      dnd-finished ()
      action-changed (GdkDragAction)

    Signals from GObject:
      notify (GParam)
    """
    def finish(
        self, success, del_, time
    ): ...  # FIXME: Override is missing typing annotation
    def get_actions(self) -> DragAction: ...
    def get_dest_window(self) -> Window: ...
    def get_device(self) -> Device: ...
    def get_drag_window(self) -> Window | None: ...
    def get_protocol(self) -> DragProtocol: ...
    def get_selected_action(self) -> DragAction: ...
    def get_source_window(self) -> Window: ...
    def get_suggested_action(self) -> DragAction: ...
    def list_targets(self) -> list[Atom]: ...
    def manage_dnd(self, ipc_window: Window, actions: DragAction) -> bool: ...
    def set_device(self, device: Device) -> None: ...
    def set_hotspot(self, hot_x: int, hot_y: int) -> None: ...

class DrawingContext(GObject.Object):
    """
    :Constructors:

    ::

        DrawingContext(**properties)

    Object GdkDrawingContext

    Properties from GdkDrawingContext:
      window -> GdkWindow: Window
        The window that created the context
      clip -> CairoRegion: Clip
        The clip region of the context

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def clip(self) -> cairo.Region | None: ...
        @property
        def window(self) -> Window: ...

    @property
    def props(self) -> Props: ...
    def __init__(self, *, clip: cairo.Region = ..., window: Window = ...) -> None: ...
    # override
    def get_cairo_context(self) -> cairo.Context[cairo.ImageSurface]: ...
    def get_clip(self) -> cairo.Region | None: ...
    def get_window(self) -> Window: ...
    def is_valid(self) -> bool: ...

class DrawingContextClass(_gi.Struct): ...

# override
class Event(GObject.GBoxed):
    _UNION_MEMBERS = ...
    any: EventAny
    button: EventButton
    configure: EventConfigure
    crossing: EventCrossing
    dnd: EventDND
    expose: EventExpose
    focus_change: EventFocus
    grab_broken: EventGrabBroken
    key: EventKey
    motion: EventMotion
    owner_change: EventOwnerChange
    pad_axis: EventPadAxis
    pad_button: EventPadButton
    pad_group_mode: EventPadGroupMode
    property: EventProperty
    proximity: EventProximity
    scroll: EventScroll
    selection: EventSelection
    setting: EventSetting
    touch: EventTouch
    touchpad_pinch: EventTouchpadPinch
    touchpad_swipe: EventTouchpadSwipe
    type: EventType
    visibility: EventVisibility
    window_state: EventWindowState

    def free(self) -> None: ...
    @staticmethod
    def get() -> Event | None: ...
    def get_axis(self, axis_use: AxisUse) -> tuple[bool, float]: ...
    def get_button(self) -> tuple[bool, int]: ...
    def get_click_count(self) -> tuple[bool, int]: ...
    def get_coords(self) -> tuple[bool, float, float]: ...
    def get_device(self) -> Device | None: ...
    def get_device_tool(self) -> DeviceTool: ...
    def get_event_sequence(self) -> EventSequence: ...
    def get_event_type(self) -> EventType: ...
    def get_keycode(self) -> tuple[bool, int]: ...
    def get_keyval(self) -> tuple[bool, int]: ...
    def get_pointer_emulated(self) -> bool: ...
    def get_root_coords(self) -> tuple[bool, float, float]: ...
    def get_scancode(self) -> int: ...
    def get_screen(self) -> Screen: ...
    def get_scroll_deltas(self) -> tuple[bool, float, float]: ...
    def get_scroll_direction(self) -> tuple[bool, ScrollDirection]: ...
    def get_seat(self) -> Seat: ...
    def get_source_device(self) -> Device | None: ...
    def get_state(self) -> ModifierType: ...
    def get_time(self) -> int: ...
    def get_window(self) -> Window: ...
    @staticmethod
    def handler_set(func: Callable[..., None], *data: Any) -> None: ...
    def is_scroll_stop_event(self) -> bool: ...
    @classmethod
    def new(cls, type: EventType) -> Event: ...
    @staticmethod
    def peek() -> Event | None: ...
    def put(self) -> None: ...
    @staticmethod
    def request_motions(event: EventMotion) -> None: ...
    def set_device(self, device: Device) -> None: ...
    def set_device_tool(self, tool: DeviceTool | None = None) -> None: ...
    def set_screen(self, screen: Screen) -> None: ...
    def set_source_device(self, device: Device) -> None: ...
    def triggers_context_menu(self) -> bool: ...

# override
class EventAny(Event):
    type: EventType
    window: Window
    send_event: int

# override
class EventButton(Event):
    type: EventType
    window: Window
    send_event: int
    time: int
    x: float
    y: float
    axes: float
    state: ModifierType
    button: int
    device: Device
    x_root: float
    y_root: float

# override
class EventConfigure(Event):
    type: EventType
    window: Window
    send_event: int
    x: int
    y: int
    width: int
    height: int

# override
class EventCrossing(Event):
    type: EventType
    window: Window
    send_event: int
    subwindow: Window
    time: int
    x: float
    y: float
    x_root: float
    y_root: float
    mode: CrossingMode
    detail: NotifyType
    focus: bool
    state: ModifierType

# override
class EventDND(Event):
    type: EventType
    window: Window
    send_event: int
    context: DragContext
    time: int
    x_root: int
    y_root: int

# override
class EventExpose(Event):
    type: EventType
    window: Window
    send_event: int
    area: Rectangle
    region: cairo.Region
    count: int

# override
class EventFocus(Event):
    type: EventType
    window: Window
    send_event: int
    in_: int

# override
class EventGrabBroken(Event):
    type: EventType
    window: Window
    send_event: int
    keyboard: bool
    implicit: bool
    grab_window: Window

# override
class EventKey(Event):
    type: EventType
    window: Window
    send_event: int
    time: int
    state: ModifierType
    keyval: int
    length: int
    string: str
    hardware_keycode: int
    group: int
    is_modifier: int

# override
class EventMotion(Event):
    type: EventType
    window: Window
    send_event: int
    time: int
    x: float
    y: float
    axes: float
    state: ModifierType
    is_hint: int
    device: Device
    x_root: float
    y_root: float

# override
class EventOwnerChange(Event):
    type: EventType
    window: Window
    send_event: int
    owner: Window
    reason: OwnerChange
    selection: Atom
    time: int
    selection_time: int

# override
class EventPadAxis(Event):
    type: EventType
    window: Window
    send_event: int
    time: int
    group: int
    index: int
    mode: int
    value: float

# override
class EventPadButton(Event):
    type: EventType
    window: Window
    send_event: int
    time: int
    group: int
    button: int
    mode: int

# override
class EventPadGroupMode(Event):
    type: EventType
    window: Window
    send_event: int
    time: int
    group: int
    mode: int

# override
class EventProperty(Event):
    type: EventType
    window: Window
    send_event: int
    atom: Atom
    time: int
    state: PropertyState

# override
class EventProximity(Event):
    type: EventType
    window: Window
    send_event: int
    time: int
    device: Device

# override
class EventScroll(Event):
    type: EventType
    window: Window
    send_event: int
    time: int
    x: float
    y: float
    state: ModifierType
    direction: ScrollDirection
    device: Device
    x_root: float
    y_root: float
    delta_x: float
    delta_y: float
    is_stop: int

# override
class EventSelection(Event):
    type: EventType
    window: Window
    send_event: int
    selection: Atom
    target: Atom
    property: Atom
    time: int
    requestor: Window

class EventSequence(GObject.GBoxed): ...

# override
class EventSetting(Event):
    type: EventType
    window: Window
    send_event: int
    action: SettingAction
    name: str

# override
class EventTouch(Event):
    type: EventType
    window: Window
    send_event: int
    time: int
    x: float
    y: float
    axes: float
    state: ModifierType
    sequence: EventSequence
    emulating_pointer: bool
    device: Device
    x_root: float
    y_root: float

# override
class EventTouchpadPinch(Event):
    type: EventType
    window: Window
    send_event: int
    phase: int
    n_fingers: int
    time: int
    x: float
    y: float
    dx: float
    dy: float
    angle_delta: float
    scale: float
    x_root: float
    y_root: float
    state: ModifierType

# override
class EventTouchpadSwipe(Event):
    type: EventType
    window: Window
    send_event: int
    phase: int
    n_fingers: int
    time: int
    x: float
    y: float
    dx: float
    dy: float
    x_root: float
    y_root: float
    state: ModifierType

# override
class EventVisibility(Event):
    type: EventType
    window: Window
    send_event: int
    state: VisibilityState

# override
class EventWindowState(Event):
    type: EventType
    window: Window
    send_event: int
    changed_mask: WindowState
    new_window_state: WindowState

class FrameClock(GObject.Object):
    """
    :Constructors:

    ::

        FrameClock(**properties)

    Object GdkFrameClock

    Signals from GdkFrameClock:
      flush-events ()
      before-paint ()
      update ()
      layout ()
      paint ()
      after-paint ()
      resume-events ()

    Signals from GObject:
      notify (GParam)
    """
    def begin_updating(self) -> None: ...
    def end_updating(self) -> None: ...
    def get_current_timings(self) -> FrameTimings | None: ...
    def get_frame_counter(self) -> int: ...
    def get_frame_time(self) -> int: ...
    def get_history_start(self) -> int: ...
    def get_refresh_info(self, base_time: int) -> tuple[int, int]: ...
    def get_timings(self, frame_counter: int) -> FrameTimings | None: ...
    def request_phase(self, phase: FrameClockPhase) -> None: ...

class FrameClockClass(_gi.Struct): ...
class FrameClockPrivate(_gi.Struct): ...

class FrameTimings(GObject.GBoxed):
    def get_complete(self) -> bool: ...
    def get_frame_counter(self) -> int: ...
    def get_frame_time(self) -> int: ...
    def get_predicted_presentation_time(self) -> int: ...
    def get_presentation_time(self) -> int: ...
    def get_refresh_interval(self) -> int: ...
    def ref(self) -> FrameTimings: ...
    def unref(self) -> None: ...

class GLContext(GObject.Object):
    """
    :Constructors:

    ::

        GLContext(**properties)

    Object GdkGLContext

    Properties from GdkGLContext:
      display -> GdkDisplay: Display
        The GDK display used to create the GL context
      window -> GdkWindow: Window
        The GDK window bound to the GL context
      shared-context -> GdkGLContext: Shared context
        The GL context this context shares data with

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def display(self) -> Display | None: ...
        @property
        def shared_context(self) -> GLContext | None: ...
        @property
        def window(self) -> Window | None: ...

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        display: Display = ...,
        shared_context: GLContext = ...,
        window: Window = ...,
    ) -> None: ...
    @staticmethod
    def clear_current() -> None: ...
    @staticmethod
    def get_current() -> GLContext | None: ...
    def get_debug_enabled(self) -> bool: ...
    def get_display(self) -> Display | None: ...
    def get_forward_compatible(self) -> bool: ...
    def get_required_version(self) -> tuple[int, int]: ...
    def get_shared_context(self) -> GLContext | None: ...
    def get_use_es(self) -> bool: ...
    def get_version(self) -> tuple[int, int]: ...
    def get_window(self) -> Window | None: ...
    def is_legacy(self) -> bool: ...
    def make_current(self) -> None: ...
    def realize(self) -> bool: ...
    def set_debug_enabled(self, enabled: bool) -> None: ...
    def set_forward_compatible(self, compatible: bool) -> None: ...
    def set_required_version(self, major: int, minor: int) -> None: ...
    def set_use_es(self, use_es: int) -> None: ...

class Geometry(_gi.Struct):
    """
    :Constructors:

    ::

        Geometry()
    """

    min_width: int
    min_height: int
    max_width: int
    max_height: int
    base_width: int
    base_height: int
    width_inc: int
    height_inc: int
    min_aspect: float
    max_aspect: float
    win_gravity: Gravity

class Keymap(GObject.Object):
    """
    :Constructors:

    ::

        Keymap(**properties)

    Object GdkKeymap

    Signals from GdkKeymap:
      direction-changed ()
      keys-changed ()
      state-changed ()

    Signals from GObject:
      notify (GParam)
    """
    def add_virtual_modifiers(self) -> ModifierType: ...
    def get_caps_lock_state(self) -> bool: ...
    @staticmethod
    def get_default() -> Keymap: ...
    def get_direction(self) -> Pango.Direction: ...
    def get_entries_for_keycode(
        self, hardware_keycode: int
    ) -> tuple[bool, list[KeymapKey], list[int]]: ...
    def get_entries_for_keyval(self, keyval: int) -> tuple[bool, list[KeymapKey]]: ...
    @staticmethod
    def get_for_display(display: Display) -> Keymap: ...
    def get_modifier_mask(self, intent: ModifierIntent) -> ModifierType: ...
    def get_modifier_state(self) -> int: ...
    def get_num_lock_state(self) -> bool: ...
    def get_scroll_lock_state(self) -> bool: ...
    def have_bidi_layouts(self) -> bool: ...
    def lookup_key(self, key: KeymapKey) -> int: ...
    def map_virtual_modifiers(self) -> tuple[bool, ModifierType]: ...
    def translate_keyboard_state(
        self, hardware_keycode: int, state: ModifierType, group: int
    ) -> tuple[bool, int, int, int, ModifierType]: ...

class KeymapKey(_gi.Struct):
    """
    :Constructors:

    ::

        KeymapKey()
    """

    keycode: int
    group: int
    level: int

class Monitor(GObject.Object):
    """
    :Constructors:

    ::

        Monitor(**properties)

    Object GdkMonitor

    Signals from GdkMonitor:
      invalidate ()

    Properties from GdkMonitor:
      display -> GdkDisplay: Display
        The display of the monitor
      manufacturer -> gchararray: Manufacturer
        The manufacturer name
      model -> gchararray: Model
        The model name
      scale-factor -> gint: Scale factor
        The scale factor
      geometry -> GdkRectangle: Geometry
        The geometry of the monitor
      workarea -> GdkRectangle: Workarea
        The workarea of the monitor
      width-mm -> gint: Physical width
        The width of the monitor, in millimeters
      height-mm -> gint: Physical height
        The height of the monitor, in millimeters
      refresh-rate -> gint: Refresh rate
        The refresh rate, in millihertz
      subpixel-layout -> GdkSubpixelLayout: Subpixel layout
        The subpixel layout

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def display(self) -> Display: ...
        @property
        def geometry(self) -> Rectangle: ...
        @property
        def height_mm(self) -> int: ...
        @property
        def manufacturer(self) -> str | None: ...
        @property
        def model(self) -> str | None: ...
        @property
        def refresh_rate(self) -> int: ...
        @property
        def scale_factor(self) -> int: ...
        @property
        def subpixel_layout(self) -> SubpixelLayout: ...
        @property
        def width_mm(self) -> int: ...
        @property
        def workarea(self) -> Rectangle: ...

    @property
    def props(self) -> Props: ...
    def __init__(self, *, display: Display = ...) -> None: ...
    def get_display(self) -> Display: ...
    def get_geometry(self) -> Rectangle: ...
    def get_height_mm(self) -> int: ...
    def get_manufacturer(self) -> str | None: ...
    def get_model(self) -> str | None: ...
    def get_refresh_rate(self) -> int: ...
    def get_scale_factor(self) -> int: ...
    def get_subpixel_layout(self) -> SubpixelLayout: ...
    def get_width_mm(self) -> int: ...
    def get_workarea(self) -> Rectangle: ...
    def is_primary(self) -> bool: ...

class MonitorClass(_gi.Struct): ...

class Point(_gi.Struct):
    """
    :Constructors:

    ::

        Point()
    """

    x: int
    y: int

class RGBA(GObject.GBoxed):
    """
    :Constructors:

    ::

        RGBA()
    """

    red: float
    green: float
    blue: float
    alpha: float
    # override
    def __init__(
        self,
        red: float = 1.0,
        green: float = 1.0,
        blue: float = 1.0,
        alpha: float = 1.0,
    ) -> None: ...
    # override
    def __iter__(self) -> Iterator[float]: ...
    def copy(self) -> RGBA: ...
    def equal(self, p2: RGBA) -> bool: ...
    def free(self) -> None: ...
    # override
    @classmethod
    def from_color(cls, color: Color) -> RGBA: ...
    def hash(self) -> int: ...
    def parse(self, spec: str) -> bool: ...
    # override
    def to_color(self) -> Color: ...
    def to_string(self) -> str: ...

class Rectangle(GObject.GBoxed):
    """
    :Constructors:

    ::

        Rectangle()
    """

    x: int
    y: int
    width: int
    height: int
    def equal(self, rect2: Rectangle) -> bool: ...
    def intersect(self, src2: Rectangle) -> tuple[bool, Rectangle]: ...
    def union(self, src2: Rectangle) -> Rectangle: ...

class Screen(GObject.Object):
    """
    :Constructors:

    ::

        Screen(**properties)

    Object GdkScreen

    Signals from GdkScreen:
      size-changed ()
      composited-changed ()
      monitors-changed ()

    Properties from GdkScreen:
      font-options -> gpointer: Font options
        The default font options for the screen
      resolution -> gdouble: Font resolution
        The resolution for fonts on the screen

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        font_options: None | None
        resolution: float

    @property
    def props(self) -> Props: ...
    def __init__(
        self, *, font_options: None | None = ..., resolution: float = ...
    ) -> None: ...
    def get_active_window(self) -> Window | None: ...
    @staticmethod
    def get_default() -> Screen | None: ...
    def get_display(self) -> Display: ...
    def get_font_options(self) -> cairo.FontOptions | None: ...
    def get_height(self) -> int: ...
    def get_height_mm(self) -> int: ...
    def get_monitor_at_point(self, x: int, y: int) -> int: ...
    def get_monitor_at_window(self, window: Window) -> int: ...
    def get_monitor_geometry(self, monitor_num: int) -> Rectangle: ...
    def get_monitor_height_mm(self, monitor_num: int) -> int: ...
    def get_monitor_plug_name(self, monitor_num: int) -> str | None: ...
    def get_monitor_scale_factor(self, monitor_num: int) -> int: ...
    def get_monitor_width_mm(self, monitor_num: int) -> int: ...
    def get_monitor_workarea(self, monitor_num: int) -> Rectangle: ...
    def get_n_monitors(self) -> int: ...
    def get_number(self) -> int: ...
    def get_primary_monitor(self) -> int: ...
    def get_resolution(self) -> float: ...
    def get_rgba_visual(self) -> Visual | None: ...
    def get_root_window(self) -> Window: ...
    def get_setting(self, name: str, value: Any) -> bool: ...
    def get_system_visual(self) -> Visual: ...
    def get_toplevel_windows(self) -> list[Window]: ...
    def get_width(self) -> int: ...
    def get_width_mm(self) -> int: ...
    def get_window_stack(self) -> list[Window] | None: ...
    @staticmethod
    def height() -> int: ...
    @staticmethod
    def height_mm() -> int: ...
    def is_composited(self) -> bool: ...
    def list_visuals(self) -> list[Visual]: ...
    def make_display_name(self) -> str: ...
    def set_font_options(self, options: cairo.FontOptions | None = None) -> None: ...
    def set_resolution(self, dpi: float) -> None: ...
    @staticmethod
    def width() -> int: ...
    @staticmethod
    def width_mm() -> int: ...

class Seat(GObject.Object):
    """
    :Constructors:

    ::

        Seat(**properties)

    Object GdkSeat

    Signals from GdkSeat:
      device-added (GdkDevice)
      device-removed (GdkDevice)
      tool-added (GdkDeviceTool)
      tool-removed (GdkDeviceTool)

    Properties from GdkSeat:
      display -> GdkDisplay: Display
        Display

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        @property
        def display(self) -> Display: ...

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    def __init__(self, *, display: Display = ...) -> None: ...
    def get_capabilities(self) -> SeatCapabilities: ...
    def get_display(self) -> Display: ...
    def get_keyboard(self) -> Device | None: ...
    def get_pointer(self) -> Device | None: ...
    def get_slaves(self, capabilities: SeatCapabilities) -> list[Device]: ...
    def grab(
        self,
        window: Window,
        capabilities: SeatCapabilities,
        owner_events: bool,
        cursor: Cursor | None = None,
        event: Event | None = None,
        prepare_func: Callable[..., None] | None = None,
        *prepare_func_data: Any,
    ) -> GrabStatus: ...
    def ungrab(self) -> None: ...

class TimeCoord(_gi.Struct):
    """
    :Constructors:

    ::

        TimeCoord()
    """

    time: int
    axes: list[float]

class Visual(GObject.Object):
    """
    :Constructors:

    ::

        Visual(**properties)

    Object GdkVisual

    Signals from GObject:
      notify (GParam)
    """
    @staticmethod
    def get_best() -> Visual: ...
    @staticmethod
    def get_best_depth() -> int: ...
    @staticmethod
    def get_best_type() -> VisualType: ...
    @staticmethod
    def get_best_with_both(depth: int, visual_type: VisualType) -> Visual | None: ...
    @staticmethod
    def get_best_with_depth(depth: int) -> Visual: ...
    @staticmethod
    def get_best_with_type(visual_type: VisualType) -> Visual: ...
    def get_bits_per_rgb(self) -> int: ...
    def get_blue_pixel_details(self) -> tuple[int, int, int]: ...
    def get_byte_order(self) -> ByteOrder: ...
    def get_colormap_size(self) -> int: ...
    def get_depth(self) -> int: ...
    def get_green_pixel_details(self) -> tuple[int, int, int]: ...
    def get_red_pixel_details(self) -> tuple[int, int, int]: ...
    def get_screen(self) -> Screen: ...
    @staticmethod
    def get_system() -> Visual: ...
    def get_visual_type(self) -> VisualType: ...

class Window(GObject.Object):
    """
    :Constructors:

    ::

        Window(**properties)
        new(parent:Gdk.Window=None, attributes:Gdk.WindowAttr, attributes_mask:Gdk.WindowAttributesType) -> Gdk.Window

    Object GdkWindow

    Signals from GdkWindow:
      pick-embedded-child (gdouble, gdouble) -> GdkWindow
      to-embedder (gdouble, gdouble, gpointer, gpointer)
      from-embedder (gdouble, gdouble, gpointer, gpointer)
      create-surface (gint, gint) -> CairoSurface
      moved-to-rect (gpointer, gpointer, gboolean, gboolean)

    Properties from GdkWindow:
      cursor -> GdkCursor: Cursor
        Cursor

    Signals from GObject:
      notify (GParam)
    """
    @type_check_only
    class Props(GObject.Object.Props):
        cursor: Cursor | None

    @property
    def props(self) -> Props: ...
    # override
    def __init__(
        self,
        parent: Window | None,
        attributes: WindowAttr,
        attributes_mask: WindowAttributesType,
    ) -> None: ...
    @staticmethod
    def at_pointer() -> tuple[Window, int, int]: ...
    def beep(self) -> None: ...
    def begin_draw_frame(self, region: cairo.Region) -> DrawingContext: ...
    def begin_move_drag(
        self, button: int, root_x: int, root_y: int, timestamp: int
    ) -> None: ...
    def begin_move_drag_for_device(
        self, device: Device, button: int, root_x: int, root_y: int, timestamp: int
    ) -> None: ...
    def begin_paint_rect(self, rectangle: Rectangle) -> None: ...
    def begin_paint_region(self, region: cairo.Region) -> None: ...
    def begin_resize_drag(
        self, edge: WindowEdge, button: int, root_x: int, root_y: int, timestamp: int
    ) -> None: ...
    def begin_resize_drag_for_device(
        self,
        edge: WindowEdge,
        device: Device,
        button: int,
        root_x: int,
        root_y: int,
        timestamp: int,
    ) -> None: ...
    def cairo_create(self): ...  # FIXME: Override is missing typing annotation
    def configure_finished(self) -> None: ...
    @staticmethod
    def constrain_size(
        geometry: Geometry, flags: WindowHints, width: int, height: int
    ) -> tuple[int, int]: ...
    def coords_from_parent(
        self, parent_x: float, parent_y: float
    ) -> tuple[float, float]: ...
    def coords_to_parent(self, x: float, y: float) -> tuple[float, float]: ...
    def create_gl_context(self) -> GLContext: ...
    def create_similar_image_surface(
        self, format: cairo.Format, width: int, height: int, scale: int
    ) -> cairo.Surface: ...
    def create_similar_surface(
        self, content: cairo.Content, width: int, height: int
    ) -> cairo.Surface: ...
    def deiconify(self) -> None: ...
    def destroy(self) -> None: ...
    def destroy_notify(self) -> None: ...
    def do_create_surface(self, width: int, height: int) -> cairo.Surface: ...
    def do_from_embedder(
        self,
        embedder_x: float,
        embedder_y: float,
        offscreen_x: float,
        offscreen_y: float,
    ) -> None: ...
    def do_to_embedder(
        self,
        offscreen_x: float,
        offscreen_y: float,
        embedder_x: float,
        embedder_y: float,
    ) -> None: ...
    def enable_synchronized_configure(self) -> None: ...
    def end_draw_frame(self, context: DrawingContext) -> None: ...
    def end_paint(self) -> None: ...
    def ensure_native(self) -> bool: ...
    def flush(self) -> None: ...
    def focus(self, timestamp: int) -> None: ...
    def freeze_toplevel_updates_libgtk_only(self) -> None: ...
    def freeze_updates(self) -> None: ...
    def fullscreen(self) -> None: ...
    def fullscreen_on_monitor(self, monitor: int) -> None: ...
    def geometry_changed(self) -> None: ...
    def get_accept_focus(self) -> bool: ...
    def get_background_pattern(self) -> cairo.Pattern | None: ...
    def get_children(self) -> list[Window]: ...
    def get_children_with_user_data(self, user_data: None) -> list[Window]: ...
    def get_clip_region(self) -> cairo.Region: ...
    def get_composited(self) -> bool: ...
    def get_cursor(self) -> Cursor | None: ...
    def get_decorations(self) -> tuple[bool, WMDecoration]: ...
    def get_device_cursor(self, device: Device) -> Cursor | None: ...
    def get_device_events(self, device: Device) -> EventMask: ...
    def get_device_position(
        self, device: Device
    ) -> tuple[Window | None, int, int, ModifierType]: ...
    def get_device_position_double(
        self, device: Device
    ) -> tuple[Window | None, float, float, ModifierType]: ...
    def get_display(self) -> Display: ...
    def get_drag_protocol(self) -> tuple[DragProtocol, Window]: ...
    def get_effective_parent(self) -> Window: ...
    def get_effective_toplevel(self) -> Window: ...
    def get_event_compression(self) -> bool: ...
    def get_events(self) -> EventMask: ...
    def get_focus_on_map(self) -> bool: ...
    def get_frame_clock(self) -> FrameClock: ...
    def get_frame_extents(self) -> Rectangle: ...
    def get_fullscreen_mode(self) -> FullscreenMode: ...
    def get_geometry(self) -> tuple[int, int, int, int]: ...
    def get_group(self) -> Window: ...
    def get_height(self) -> int: ...
    def get_modal_hint(self) -> bool: ...
    def get_origin(self) -> tuple[int, int, int]: ...
    def get_parent(self) -> Window: ...
    def get_pass_through(self) -> bool: ...
    def get_pointer(self) -> tuple[Window | None, int, int, ModifierType]: ...
    def get_position(self) -> tuple[int, int]: ...
    def get_root_coords(self, x: int, y: int) -> tuple[int, int]: ...
    def get_root_origin(self) -> tuple[int, int]: ...
    def get_scale_factor(self) -> int: ...
    def get_screen(self) -> Screen: ...
    def get_source_events(self, source: InputSource) -> EventMask: ...
    def get_state(self) -> WindowState: ...
    def get_support_multidevice(self) -> bool: ...
    def get_toplevel(self) -> Window: ...
    def get_type_hint(self) -> WindowTypeHint: ...
    def get_update_area(self) -> cairo.Region: ...
    def get_user_data(self) -> None: ...
    def get_visible_region(self) -> cairo.Region: ...
    def get_visual(self) -> Visual: ...
    def get_width(self) -> int: ...
    def get_window_type(self) -> WindowType: ...
    def has_native(self) -> bool: ...
    def hide(self) -> None: ...
    def iconify(self) -> None: ...
    def input_shape_combine_region(
        self, shape_region: cairo.Region, offset_x: int, offset_y: int
    ) -> None: ...
    def invalidate_maybe_recurse(
        self,
        region: cairo.Region,
        child_func: Callable[..., bool] | None = None,
        *user_data: Any,
    ) -> None: ...
    def invalidate_rect(
        self, rect: Rectangle | None, invalidate_children: bool
    ) -> None: ...
    def invalidate_region(
        self, region: cairo.Region, invalidate_children: bool
    ) -> None: ...
    def is_destroyed(self) -> bool: ...
    def is_input_only(self) -> bool: ...
    def is_shaped(self) -> bool: ...
    def is_viewable(self) -> bool: ...
    def is_visible(self) -> bool: ...
    def lower(self) -> None: ...
    def mark_paint_from_clip(self, cr: cairo.Context[_SomeSurface]) -> None: ...
    def maximize(self) -> None: ...
    def merge_child_input_shapes(self) -> None: ...
    def merge_child_shapes(self) -> None: ...
    def move(self, x: int, y: int) -> None: ...
    def move_region(self, region: cairo.Region, dx: int, dy: int) -> None: ...
    def move_resize(self, x: int, y: int, width: int, height: int) -> None: ...
    def move_to_rect(
        self,
        rect: Rectangle,
        rect_anchor: Gravity,
        window_anchor: Gravity,
        anchor_hints: AnchorHints,
        rect_anchor_dx: int,
        rect_anchor_dy: int,
    ) -> None: ...
    @classmethod
    def new(
        cls,
        parent: Window | None,
        attributes: WindowAttr,
        attributes_mask: WindowAttributesType,
    ) -> Window: ...
    def peek_children(self) -> list[Window]: ...
    @staticmethod
    def process_all_updates() -> None: ...
    def process_updates(self, update_children: bool) -> None: ...
    def raise_(self) -> None: ...
    def register_dnd(self) -> None: ...
    def reparent(self, new_parent: Window, x: int, y: int) -> None: ...
    def resize(self, width: int, height: int) -> None: ...
    def restack(self, sibling: Window | None, above: bool) -> None: ...
    def scroll(self, dx: int, dy: int) -> None: ...
    def set_accept_focus(self, accept_focus: bool) -> None: ...
    def set_background(self, color: Color) -> None: ...
    def set_background_pattern(self, pattern: cairo.Pattern | None = None) -> None: ...
    def set_background_rgba(self, rgba: RGBA) -> None: ...
    def set_child_input_shapes(self) -> None: ...
    def set_child_shapes(self) -> None: ...
    def set_composited(self, composited: bool) -> None: ...
    def set_cursor(self, cursor: Cursor | None = None) -> None: ...
    @staticmethod
    def set_debug_updates(setting: bool) -> None: ...
    def set_decorations(self, decorations: WMDecoration) -> None: ...
    def set_device_cursor(self, device: Device, cursor: Cursor) -> None: ...
    def set_device_events(self, device: Device, event_mask: EventMask) -> None: ...
    def set_event_compression(self, event_compression: bool) -> None: ...
    def set_events(self, event_mask: EventMask) -> None: ...
    def set_focus_on_map(self, focus_on_map: bool) -> None: ...
    def set_fullscreen_mode(self, mode: FullscreenMode) -> None: ...
    def set_functions(self, functions: WMFunction) -> None: ...
    def set_geometry_hints(
        self, geometry: Geometry, geom_mask: WindowHints
    ) -> None: ...
    def set_group(self, leader: Window | None = None) -> None: ...
    def set_icon_list(self, pixbufs: list[GdkPixbuf.Pixbuf]) -> None: ...
    def set_icon_name(self, name: str | None = None) -> None: ...
    def set_keep_above(self, setting: bool) -> None: ...
    def set_keep_below(self, setting: bool) -> None: ...
    def set_modal_hint(self, modal: bool) -> None: ...
    def set_opacity(self, opacity: float) -> None: ...
    def set_opaque_region(self, region: cairo.Region | None = None) -> None: ...
    def set_override_redirect(self, override_redirect: bool) -> None: ...
    def set_pass_through(self, pass_through: bool) -> None: ...
    def set_role(self, role: str) -> None: ...
    def set_shadow_width(
        self, left: int, right: int, top: int, bottom: int
    ) -> None: ...
    def set_skip_pager_hint(self, skips_pager: bool) -> None: ...
    def set_skip_taskbar_hint(self, skips_taskbar: bool) -> None: ...
    def set_source_events(self, source: InputSource, event_mask: EventMask) -> None: ...
    def set_startup_id(self, startup_id: str) -> None: ...
    def set_static_gravities(self, use_static: bool) -> bool: ...
    def set_support_multidevice(self, support_multidevice: bool) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_transient_for(self, parent: Window) -> None: ...
    def set_type_hint(self, hint: WindowTypeHint) -> None: ...
    def set_urgency_hint(self, urgent: bool) -> None: ...
    def set_user_data(self, user_data: GObject.Object | None = None) -> None: ...
    def shape_combine_region(
        self, shape_region: cairo.Region | None, offset_x: int, offset_y: int
    ) -> None: ...
    def show(self) -> None: ...
    def show_unraised(self) -> None: ...
    def show_window_menu(self, event: Event) -> bool: ...
    def stick(self) -> None: ...
    def thaw_toplevel_updates_libgtk_only(self) -> None: ...
    def thaw_updates(self) -> None: ...
    def unfullscreen(self) -> None: ...
    def unmaximize(self) -> None: ...
    def unstick(self) -> None: ...
    def withdraw(self) -> None: ...

class WindowAttr(_gi.Struct):
    """
    :Constructors:

    ::

        WindowAttr()
    """

    title: str
    event_mask: int
    x: int
    y: int
    width: int
    height: int
    wclass: WindowWindowClass
    visual: Visual
    window_type: WindowType
    cursor: Cursor
    wmclass_name: str
    wmclass_class: str
    override_redirect: bool
    type_hint: WindowTypeHint

class WindowClass(_gi.Struct):
    """
    :Constructors:

    ::

        WindowClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def pick_embedded_child(self) -> None: ...
    @property
    def to_embedder(self) -> Callable[[Window, float, float, float, float], None]: ...
    @property
    def from_embedder(self) -> Callable[[Window, float, float, float, float], None]: ...
    @property
    def create_surface(self) -> Callable[[Window, int, int], cairo.Surface]: ...

class WindowRedirect(_gi.Struct): ...

class AnchorHints(GObject.GFlags):
    FLIP = 3
    FLIP_X = 1
    FLIP_Y = 2
    RESIZE = 48
    RESIZE_X = 16
    RESIZE_Y = 32
    SLIDE = 12
    SLIDE_X = 4
    SLIDE_Y = 8

class AxisFlags(GObject.GFlags):
    DISTANCE = 128
    PRESSURE = 8
    ROTATION = 256
    SLIDER = 512
    WHEEL = 64
    X = 2
    XTILT = 16
    Y = 4
    YTILT = 32

class DragAction(GObject.GFlags):
    ASK = 32
    COPY = 2
    DEFAULT = 1
    LINK = 8
    MOVE = 4
    PRIVATE = 16

class EventMask(GObject.GFlags):
    ALL_EVENTS_MASK = 67108862
    BUTTON1_MOTION_MASK = 32
    BUTTON2_MOTION_MASK = 64
    BUTTON3_MOTION_MASK = 128
    BUTTON_MOTION_MASK = 16
    BUTTON_PRESS_MASK = 256
    BUTTON_RELEASE_MASK = 512
    ENTER_NOTIFY_MASK = 4096
    EXPOSURE_MASK = 2
    FOCUS_CHANGE_MASK = 16384
    KEY_PRESS_MASK = 1024
    KEY_RELEASE_MASK = 2048
    LEAVE_NOTIFY_MASK = 8192
    POINTER_MOTION_HINT_MASK = 8
    POINTER_MOTION_MASK = 4
    PROPERTY_CHANGE_MASK = 65536
    PROXIMITY_IN_MASK = 262144
    PROXIMITY_OUT_MASK = 524288
    SCROLL_MASK = 2097152
    SMOOTH_SCROLL_MASK = 8388608
    STRUCTURE_MASK = 32768
    SUBSTRUCTURE_MASK = 1048576
    TABLET_PAD_MASK = 33554432
    TOUCHPAD_GESTURE_MASK = 16777216
    TOUCH_MASK = 4194304
    VISIBILITY_NOTIFY_MASK = 131072

class FrameClockPhase(GObject.GFlags):
    AFTER_PAINT = 64
    BEFORE_PAINT = 2
    FLUSH_EVENTS = 1
    LAYOUT = 8
    NONE = 0
    PAINT = 16
    RESUME_EVENTS = 32
    UPDATE = 4

class ModifierType(GObject.GFlags):
    BUTTON1_MASK = 256
    BUTTON2_MASK = 512
    BUTTON3_MASK = 1024
    BUTTON4_MASK = 2048
    BUTTON5_MASK = 4096
    CONTROL_MASK = 4
    HYPER_MASK = 134217728
    LOCK_MASK = 2
    META_MASK = 268435456
    MOD1_MASK = 8
    MOD2_MASK = 16
    MOD3_MASK = 32
    MOD4_MASK = 64
    MOD5_MASK = 128
    MODIFIER_MASK = 1543512063
    MODIFIER_RESERVED_13_MASK = 8192
    MODIFIER_RESERVED_14_MASK = 16384
    MODIFIER_RESERVED_15_MASK = 32768
    MODIFIER_RESERVED_16_MASK = 65536
    MODIFIER_RESERVED_17_MASK = 131072
    MODIFIER_RESERVED_18_MASK = 262144
    MODIFIER_RESERVED_19_MASK = 524288
    MODIFIER_RESERVED_20_MASK = 1048576
    MODIFIER_RESERVED_21_MASK = 2097152
    MODIFIER_RESERVED_22_MASK = 4194304
    MODIFIER_RESERVED_23_MASK = 8388608
    MODIFIER_RESERVED_24_MASK = 16777216
    MODIFIER_RESERVED_25_MASK = 33554432
    MODIFIER_RESERVED_29_MASK = 536870912
    RELEASE_MASK = 1073741824
    SHIFT_MASK = 1
    SUPER_MASK = 67108864

class SeatCapabilities(GObject.GFlags):
    ALL = 15
    ALL_POINTING = 7
    KEYBOARD = 8
    NONE = 0
    POINTER = 1
    TABLET_STYLUS = 4
    TOUCH = 2

class WMDecoration(GObject.GFlags):
    ALL = 1
    BORDER = 2
    MAXIMIZE = 64
    MENU = 16
    MINIMIZE = 32
    RESIZEH = 4
    TITLE = 8

class WMFunction(GObject.GFlags):
    ALL = 1
    CLOSE = 32
    MAXIMIZE = 16
    MINIMIZE = 8
    MOVE = 4
    RESIZE = 2

class WindowAttributesType(GObject.GFlags):
    CURSOR = 16
    NOREDIR = 128
    TITLE = 2
    TYPE_HINT = 256
    VISUAL = 32
    WMCLASS = 64
    X = 4
    Y = 8

class WindowHints(GObject.GFlags):
    ASPECT = 16
    BASE_SIZE = 8
    MAX_SIZE = 4
    MIN_SIZE = 2
    POS = 1
    RESIZE_INC = 32
    USER_POS = 128
    USER_SIZE = 256
    WIN_GRAVITY = 64

class WindowState(GObject.GFlags):
    ABOVE = 32
    BELOW = 64
    BOTTOM_RESIZABLE = 16384
    BOTTOM_TILED = 8192
    FOCUSED = 128
    FULLSCREEN = 16
    ICONIFIED = 2
    LEFT_RESIZABLE = 65536
    LEFT_TILED = 32768
    MAXIMIZED = 4
    RIGHT_RESIZABLE = 4096
    RIGHT_TILED = 2048
    STICKY = 8
    TILED = 256
    TOP_RESIZABLE = 1024
    TOP_TILED = 512
    WITHDRAWN = 1

class AxisUse(GObject.GEnum):
    DISTANCE = 7
    IGNORE = 0
    LAST = 10
    PRESSURE = 3
    ROTATION = 8
    SLIDER = 9
    WHEEL = 6
    X = 1
    XTILT = 4
    Y = 2
    YTILT = 5

class ByteOrder(GObject.GEnum):
    LSB_FIRST = 0
    MSB_FIRST = 1

class CrossingMode(GObject.GEnum):
    DEVICE_SWITCH = 8
    GRAB = 1
    GTK_GRAB = 3
    GTK_UNGRAB = 4
    NORMAL = 0
    STATE_CHANGED = 5
    TOUCH_BEGIN = 6
    TOUCH_END = 7
    UNGRAB = 2

class CursorType(GObject.GEnum):
    ARROW = 2
    BASED_ARROW_DOWN = 4
    BASED_ARROW_UP = 6
    BLANK_CURSOR = -2
    BOAT = 8
    BOGOSITY = 10
    BOTTOM_LEFT_CORNER = 12
    BOTTOM_RIGHT_CORNER = 14
    BOTTOM_SIDE = 16
    BOTTOM_TEE = 18
    BOX_SPIRAL = 20
    CENTER_PTR = 22
    CIRCLE = 24
    CLOCK = 26
    COFFEE_MUG = 28
    CROSS = 30
    CROSSHAIR = 34
    CROSS_REVERSE = 32
    CURSOR_IS_PIXMAP = -1
    DIAMOND_CROSS = 36
    DOT = 38
    DOTBOX = 40
    DOUBLE_ARROW = 42
    DRAFT_LARGE = 44
    DRAFT_SMALL = 46
    DRAPED_BOX = 48
    EXCHANGE = 50
    FLEUR = 52
    GOBBLER = 54
    GUMBY = 56
    HAND1 = 58
    HAND2 = 60
    HEART = 62
    ICON = 64
    IRON_CROSS = 66
    LAST_CURSOR = 153
    LEFTBUTTON = 74
    LEFT_PTR = 68
    LEFT_SIDE = 70
    LEFT_TEE = 72
    LL_ANGLE = 76
    LR_ANGLE = 78
    MAN = 80
    MIDDLEBUTTON = 82
    MOUSE = 84
    PENCIL = 86
    PIRATE = 88
    PLUS = 90
    QUESTION_ARROW = 92
    RIGHTBUTTON = 100
    RIGHT_PTR = 94
    RIGHT_SIDE = 96
    RIGHT_TEE = 98
    RTL_LOGO = 102
    SAILBOAT = 104
    SB_DOWN_ARROW = 106
    SB_H_DOUBLE_ARROW = 108
    SB_LEFT_ARROW = 110
    SB_RIGHT_ARROW = 112
    SB_UP_ARROW = 114
    SB_V_DOUBLE_ARROW = 116
    SHUTTLE = 118
    SIZING = 120
    SPIDER = 122
    SPRAYCAN = 124
    STAR = 126
    TARGET = 128
    TCROSS = 130
    TOP_LEFT_ARROW = 132
    TOP_LEFT_CORNER = 134
    TOP_RIGHT_CORNER = 136
    TOP_SIDE = 138
    TOP_TEE = 140
    TREK = 142
    UL_ANGLE = 144
    UMBRELLA = 146
    UR_ANGLE = 148
    WATCH = 150
    XTERM = 152
    X_CURSOR = 0

class DevicePadFeature(GObject.GEnum):
    BUTTON = 0
    RING = 1
    STRIP = 2

class DeviceToolType(GObject.GEnum):
    AIRBRUSH = 5
    BRUSH = 3
    ERASER = 2
    LENS = 7
    MOUSE = 6
    PEN = 1
    PENCIL = 4
    UNKNOWN = 0

class DeviceType(GObject.GEnum):
    FLOATING = 2
    MASTER = 0
    SLAVE = 1

class DragCancelReason(GObject.GEnum):
    ERROR = 2
    NO_TARGET = 0
    USER_CANCELLED = 1

class DragProtocol(GObject.GEnum):
    LOCAL = 6
    MOTIF = 1
    NONE = 0
    OLE2 = 5
    ROOTWIN = 3
    WAYLAND = 7
    WIN32_DROPFILES = 4
    XDND = 2

class EventType(GObject.GEnum):
    BUTTON_PRESS = 4
    BUTTON_RELEASE = 7
    CLIENT_EVENT = 28
    CONFIGURE = 13
    DAMAGE = 36
    DELETE = 0
    DESTROY = 1
    DOUBLE_BUTTON_PRESS = 5
    DRAG_ENTER = 22
    DRAG_LEAVE = 23
    DRAG_MOTION = 24
    DRAG_STATUS = 25
    DROP_FINISHED = 27
    DROP_START = 26
    ENTER_NOTIFY = 10
    EVENT_LAST = 48
    EXPOSE = 2
    FOCUS_CHANGE = 12
    GRAB_BROKEN = 35
    KEY_PRESS = 8
    KEY_RELEASE = 9
    LEAVE_NOTIFY = 11
    MAP = 14
    MOTION_NOTIFY = 3
    NOTHING = -1
    OWNER_CHANGE = 34
    PAD_BUTTON_PRESS = 43
    PAD_BUTTON_RELEASE = 44
    PAD_GROUP_MODE = 47
    PAD_RING = 45
    PAD_STRIP = 46
    PROPERTY_NOTIFY = 16
    PROXIMITY_IN = 20
    PROXIMITY_OUT = 21
    SCROLL = 31
    SELECTION_CLEAR = 17
    SELECTION_NOTIFY = 19
    SELECTION_REQUEST = 18
    SETTING = 33
    TOUCHPAD_PINCH = 42
    TOUCHPAD_SWIPE = 41
    TOUCH_BEGIN = 37
    TOUCH_CANCEL = 40
    TOUCH_END = 39
    TOUCH_UPDATE = 38
    TRIPLE_BUTTON_PRESS = 6
    UNMAP = 15
    VISIBILITY_NOTIFY = 29
    WINDOW_STATE = 32

class FilterReturn(GObject.GEnum):
    CONTINUE = 0
    REMOVE = 2
    TRANSLATE = 1

class FullscreenMode(GObject.GEnum):
    ALL_MONITORS = 1
    CURRENT_MONITOR = 0

class GLError(GObject.GEnum):
    NOT_AVAILABLE = 0
    UNSUPPORTED_FORMAT = 1
    UNSUPPORTED_PROFILE = 2
    @staticmethod
    def quark() -> int: ...

class GrabOwnership(GObject.GEnum):
    APPLICATION = 2
    NONE = 0
    WINDOW = 1

class GrabStatus(GObject.GEnum):
    ALREADY_GRABBED = 1
    FAILED = 5
    FROZEN = 4
    INVALID_TIME = 2
    NOT_VIEWABLE = 3
    SUCCESS = 0

class Gravity(GObject.GEnum):
    CENTER = 5
    EAST = 6
    NORTH = 2
    NORTH_EAST = 3
    NORTH_WEST = 1
    SOUTH = 8
    SOUTH_EAST = 9
    SOUTH_WEST = 7
    STATIC = 10
    WEST = 4

class InputMode(GObject.GEnum):
    DISABLED = 0
    SCREEN = 1
    WINDOW = 2

class InputSource(GObject.GEnum):
    CURSOR = 3
    ERASER = 2
    KEYBOARD = 4
    MOUSE = 0
    PEN = 1
    TABLET_PAD = 8
    TOUCHPAD = 6
    TOUCHSCREEN = 5
    TRACKPOINT = 7

class ModifierIntent(GObject.GEnum):
    CONTEXT_MENU = 1
    DEFAULT_MOD_MASK = 6
    EXTEND_SELECTION = 2
    MODIFY_SELECTION = 3
    NO_TEXT_INPUT = 4
    PRIMARY_ACCELERATOR = 0
    SHIFT_GROUP = 5

class NotifyType(GObject.GEnum):
    ANCESTOR = 0
    INFERIOR = 2
    NONLINEAR = 3
    NONLINEAR_VIRTUAL = 4
    UNKNOWN = 5
    VIRTUAL = 1

class OwnerChange(GObject.GEnum):
    CLOSE = 2
    DESTROY = 1
    NEW_OWNER = 0

class PropMode(GObject.GEnum):
    APPEND = 2
    PREPEND = 1
    REPLACE = 0

class PropertyState(GObject.GEnum):
    DELETE = 1
    NEW_VALUE = 0

class ScrollDirection(GObject.GEnum):
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    SMOOTH = 4
    UP = 0

class SettingAction(GObject.GEnum):
    CHANGED = 1
    DELETED = 2
    NEW = 0

class Status(GObject.GEnum):
    ERROR = -1
    ERROR_FILE = -3
    ERROR_MEM = -4
    ERROR_PARAM = -2
    OK = 0

class SubpixelLayout(GObject.GEnum):
    HORIZONTAL_BGR = 3
    HORIZONTAL_RGB = 2
    NONE = 1
    UNKNOWN = 0
    VERTICAL_BGR = 5
    VERTICAL_RGB = 4

class TouchpadGesturePhase(GObject.GEnum):
    BEGIN = 0
    CANCEL = 3
    END = 2
    UPDATE = 1

class VisibilityState(GObject.GEnum):
    FULLY_OBSCURED = 2
    PARTIAL = 1
    UNOBSCURED = 0

class VisualType(GObject.GEnum):
    DIRECT_COLOR = 5
    GRAYSCALE = 1
    PSEUDO_COLOR = 3
    STATIC_COLOR = 2
    STATIC_GRAY = 0
    TRUE_COLOR = 4

class WindowEdge(GObject.GEnum):
    EAST = 4
    NORTH = 1
    NORTH_EAST = 2
    NORTH_WEST = 0
    SOUTH = 6
    SOUTH_EAST = 7
    SOUTH_WEST = 5
    WEST = 3

class WindowType(GObject.GEnum):
    CHILD = 2
    FOREIGN = 4
    OFFSCREEN = 5
    ROOT = 0
    SUBSURFACE = 6
    TEMP = 3
    TOPLEVEL = 1

class WindowTypeHint(GObject.GEnum):
    COMBO = 12
    DESKTOP = 7
    DIALOG = 1
    DND = 13
    DOCK = 6
    DROPDOWN_MENU = 8
    MENU = 2
    NORMAL = 0
    NOTIFICATION = 11
    POPUP_MENU = 9
    SPLASHSCREEN = 4
    TOOLBAR = 3
    TOOLTIP = 10
    UTILITY = 5

class WindowWindowClass(GObject.GEnum):
    INPUT_ONLY = 1
    INPUT_OUTPUT = 0
