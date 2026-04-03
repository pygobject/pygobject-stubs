from typing import Any
from typing import Final
from typing import TypeVar
from typing_extensions import Self

from collections.abc import Callable
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

ACTION_ALL: Final[int]
BUTTON_MIDDLE: Final[int]
BUTTON_PRIMARY: Final[int]
BUTTON_SECONDARY: Final[int]
CURRENT_TIME: Final[int]
EVENT_PROPAGATE: Final = False
EVENT_STOP: Final = True
KEY_0: Final[int]
KEY_1: Final[int]
KEY_10ChannelsDown: Final[int]
KEY_10ChannelsUp: Final[int]
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
KEY_3DMode: Final[int]
KEY_4: Final[int]
KEY_5: Final[int]
KEY_6: Final[int]
KEY_7: Final[int]
KEY_8: Final[int]
KEY_9: Final[int]
KEY_A: Final[int]
KEY_AE: Final[int]
KEY_ALSToggle: Final[int]
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
KEY_Accessibility: Final[int]
KEY_Acircumflex: Final[int]
KEY_Acircumflexacute: Final[int]
KEY_Acircumflexbelowdot: Final[int]
KEY_Acircumflexgrave: Final[int]
KEY_Acircumflexhook: Final[int]
KEY_Acircumflextilde: Final[int]
KEY_AddFavorite: Final[int]
KEY_Addressbook: Final[int]
KEY_Adiaeresis: Final[int]
KEY_Agrave: Final[int]
KEY_Ahook: Final[int]
KEY_Alt_L: Final[int]
KEY_Alt_R: Final[int]
KEY_Amacron: Final[int]
KEY_Aogonek: Final[int]
KEY_AppSelect: Final[int]
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
KEY_AspectRatio: Final[int]
KEY_Assistant: Final[int]
KEY_Atilde: Final[int]
KEY_AttendantOff: Final[int]
KEY_AttendantOn: Final[int]
KEY_AttendantToggle: Final[int]
KEY_AudibleBell_Enable: Final[int]
KEY_Audio: Final[int]
KEY_AudioCycleTrack: Final[int]
KEY_AudioDesc: Final[int]
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
KEY_AutopilotEngageToggle: Final[int]
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
KEY_BrightnessAuto: Final[int]
KEY_BrightnessMax: Final[int]
KEY_BrightnessMin: Final[int]
KEY_Buttonconfig: Final[int]
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
KEY_CameraAccessDisable: Final[int]
KEY_CameraAccessEnable: Final[int]
KEY_CameraAccessToggle: Final[int]
KEY_CameraDown: Final[int]
KEY_CameraFocus: Final[int]
KEY_CameraLeft: Final[int]
KEY_CameraRight: Final[int]
KEY_CameraUp: Final[int]
KEY_CameraZoomIn: Final[int]
KEY_CameraZoomOut: Final[int]
KEY_Cancel: Final[int]
KEY_Caps_Lock: Final[int]
KEY_Ccaron: Final[int]
KEY_Ccedilla: Final[int]
KEY_Ccircumflex: Final[int]
KEY_Ch: Final[int]
KEY_ChannelDown: Final[int]
KEY_ChannelUp: Final[int]
KEY_Clear: Final[int]
KEY_ClearGrab: Final[int]
KEY_ClearvuSonar: Final[int]
KEY_Close: Final[int]
KEY_Codeinput: Final[int]
KEY_ColonSign: Final[int]
KEY_Community: Final[int]
KEY_ContextMenu: Final[int]
KEY_ContrastAdjust: Final[int]
KEY_ControlPanel: Final[int]
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
KEY_DVD: Final[int]
KEY_Dabovedot: Final[int]
KEY_Data: Final[int]
KEY_Database: Final[int]
KEY_Dcaron: Final[int]
KEY_Delete: Final[int]
KEY_Dictate: Final[int]
KEY_Display: Final[int]
KEY_DisplayOff: Final[int]
KEY_DisplayToggle: Final[int]
KEY_DoNotDisturb: Final[int]
KEY_Documents: Final[int]
KEY_DongSign: Final[int]
KEY_Down: Final[int]
KEY_Dstroke: Final[int]
KEY_DualRangeRadar: Final[int]
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
KEY_Editor: Final[int]
KEY_Egrave: Final[int]
KEY_Ehook: Final[int]
KEY_Eisu_Shift: Final[int]
KEY_Eisu_toggle: Final[int]
KEY_Eject: Final[int]
KEY_Emacron: Final[int]
KEY_EmojiPicker: Final[int]
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
KEY_FastReverse: Final[int]
KEY_Favorites: Final[int]
KEY_Finance: Final[int]
KEY_Find: Final[int]
KEY_First_Virtual_Screen: Final[int]
KEY_FishingChart: Final[int]
KEY_Fn: Final[int]
KEY_FnRightShift: Final[int]
KEY_Fn_Esc: Final[int]
KEY_Forward: Final[int]
KEY_FrameBack: Final[int]
KEY_FrameForward: Final[int]
KEY_FullScreen: Final[int]
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
KEY_GraphicsEditor: Final[int]
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
KEY_HangupPhone: Final[int]
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
KEY_Images: Final[int]
KEY_Info: Final[int]
KEY_Insert: Final[int]
KEY_Iogonek: Final[int]
KEY_Itilde: Final[int]
KEY_J: Final[int]
KEY_Jcircumflex: Final[int]
KEY_Journal: Final[int]
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
KEY_KbdInputAssistAccept: Final[int]
KEY_KbdInputAssistCancel: Final[int]
KEY_KbdInputAssistNext: Final[int]
KEY_KbdInputAssistNextgroup: Final[int]
KEY_KbdInputAssistPrev: Final[int]
KEY_KbdInputAssistPrevgroup: Final[int]
KEY_KbdLcdMenu1: Final[int]
KEY_KbdLcdMenu2: Final[int]
KEY_KbdLcdMenu3: Final[int]
KEY_KbdLcdMenu4: Final[int]
KEY_KbdLcdMenu5: Final[int]
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
KEY_LeftDown: Final[int]
KEY_LeftUp: Final[int]
KEY_LightBulb: Final[int]
KEY_LightsToggle: Final[int]
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
KEY_Macro1: Final[int]
KEY_Macro10: Final[int]
KEY_Macro11: Final[int]
KEY_Macro12: Final[int]
KEY_Macro13: Final[int]
KEY_Macro14: Final[int]
KEY_Macro15: Final[int]
KEY_Macro16: Final[int]
KEY_Macro17: Final[int]
KEY_Macro18: Final[int]
KEY_Macro19: Final[int]
KEY_Macro2: Final[int]
KEY_Macro20: Final[int]
KEY_Macro21: Final[int]
KEY_Macro22: Final[int]
KEY_Macro23: Final[int]
KEY_Macro24: Final[int]
KEY_Macro25: Final[int]
KEY_Macro26: Final[int]
KEY_Macro27: Final[int]
KEY_Macro28: Final[int]
KEY_Macro29: Final[int]
KEY_Macro3: Final[int]
KEY_Macro30: Final[int]
KEY_Macro4: Final[int]
KEY_Macro5: Final[int]
KEY_Macro6: Final[int]
KEY_Macro7: Final[int]
KEY_Macro8: Final[int]
KEY_Macro9: Final[int]
KEY_MacroPreset1: Final[int]
KEY_MacroPreset2: Final[int]
KEY_MacroPreset3: Final[int]
KEY_MacroPresetCycle: Final[int]
KEY_MacroRecordStart: Final[int]
KEY_MacroRecordStop: Final[int]
KEY_Mae_Koho: Final[int]
KEY_Mail: Final[int]
KEY_MailForward: Final[int]
KEY_MarkWaypoint: Final[int]
KEY_Market: Final[int]
KEY_Massyo: Final[int]
KEY_MediaRepeat: Final[int]
KEY_MediaTopMenu: Final[int]
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
KEY_MonBrightnessCycle: Final[int]
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
KEY_NavChart: Final[int]
KEY_NavInfo: Final[int]
KEY_Ncaron: Final[int]
KEY_Ncedilla: Final[int]
KEY_New: Final[int]
KEY_NewSheqelSign: Final[int]
KEY_News: Final[int]
KEY_Next: Final[int]
KEY_NextElement: Final[int]
KEY_NextFavorite: Final[int]
KEY_Next_VMode: Final[int]
KEY_Next_Virtual_Screen: Final[int]
KEY_NotificationCenter: Final[int]
KEY_Ntilde: Final[int]
KEY_Num_Lock: Final[int]
KEY_Numeric0: Final[int]
KEY_Numeric1: Final[int]
KEY_Numeric11: Final[int]
KEY_Numeric12: Final[int]
KEY_Numeric2: Final[int]
KEY_Numeric3: Final[int]
KEY_Numeric4: Final[int]
KEY_Numeric5: Final[int]
KEY_Numeric6: Final[int]
KEY_Numeric7: Final[int]
KEY_Numeric8: Final[int]
KEY_Numeric9: Final[int]
KEY_NumericA: Final[int]
KEY_NumericB: Final[int]
KEY_NumericC: Final[int]
KEY_NumericD: Final[int]
KEY_NumericPound: Final[int]
KEY_NumericStar: Final[int]
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
KEY_OnScreenKeyboard: Final[int]
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
KEY_PauseRecord: Final[int]
KEY_PesetaSign: Final[int]
KEY_Phone: Final[int]
KEY_PickupPhone: Final[int]
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
KEY_Presentation: Final[int]
KEY_Prev_VMode: Final[int]
KEY_Prev_Virtual_Screen: Final[int]
KEY_PreviousCandidate: Final[int]
KEY_PreviousElement: Final[int]
KEY_Print: Final[int]
KEY_Prior: Final[int]
KEY_PrivacyScreenToggle: Final[int]
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
KEY_RadarOverlay: Final[int]
KEY_Rcaron: Final[int]
KEY_Rcedilla: Final[int]
KEY_Red: Final[int]
KEY_Redo: Final[int]
KEY_Refresh: Final[int]
KEY_RefreshRateToggle: Final[int]
KEY_Reload: Final[int]
KEY_RepeatKeys_Enable: Final[int]
KEY_Reply: Final[int]
KEY_Return: Final[int]
KEY_Right: Final[int]
KEY_RightDown: Final[int]
KEY_RightUp: Final[int]
KEY_RockerDown: Final[int]
KEY_RockerEnter: Final[int]
KEY_RockerUp: Final[int]
KEY_Romaji: Final[int]
KEY_RootMenu: Final[int]
KEY_RotateWindows: Final[int]
KEY_RotationKB: Final[int]
KEY_RotationLockToggle: Final[int]
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
KEY_Screensaver: Final[int]
KEY_ScrollClick: Final[int]
KEY_ScrollDown: Final[int]
KEY_ScrollUp: Final[int]
KEY_Scroll_Lock: Final[int]
KEY_Search: Final[int]
KEY_Select: Final[int]
KEY_SelectButton: Final[int]
KEY_SelectiveScreenshot: Final[int]
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
KEY_SidevuSonar: Final[int]
KEY_SingleCandidate: Final[int]
KEY_SingleRangeRadar: Final[int]
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
KEY_SlowReverse: Final[int]
KEY_Sos: Final[int]
KEY_Spell: Final[int]
KEY_SpellCheck: Final[int]
KEY_SplitScreen: Final[int]
KEY_Standby: Final[int]
KEY_Start: Final[int]
KEY_StickyKeys_Enable: Final[int]
KEY_Stop: Final[int]
KEY_StopRecord: Final[int]
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
KEY_Taskmanager: Final[int]
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
KEY_TraditionalSonar: Final[int]
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
KEY_Unmute: Final[int]
KEY_Uogonek: Final[int]
KEY_Up: Final[int]
KEY_Uring: Final[int]
KEY_User1KB: Final[int]
KEY_User2KB: Final[int]
KEY_UserPB: Final[int]
KEY_Utilde: Final[int]
KEY_V: Final[int]
KEY_VOD: Final[int]
KEY_VendorHome: Final[int]
KEY_Video: Final[int]
KEY_VideoPhone: Final[int]
KEY_View: Final[int]
KEY_VoiceCommand: Final[int]
KEY_Voicemail: Final[int]
KEY_VoidSymbol: Final[int]
KEY_W: Final[int]
KEY_WLAN: Final[int]
KEY_WPSButton: Final[int]
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
KEY_ZoomReset: Final[int]
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
KEY_combining_acute: Final[int]
KEY_combining_belowdot: Final[int]
KEY_combining_grave: Final[int]
KEY_combining_hook: Final[int]
KEY_combining_tilde: Final[int]
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
KEY_dead_SCHWA: Final[int]
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
KEY_dead_hamza: Final[int]
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
KEY_dead_schwa: Final[int]
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
KEY_guillemetleft: Final[int]
KEY_guillemetright: Final[int]
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
KEY_ordmasculine: Final[int]
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
MODIFIER_MASK: Final[int]
PRIORITY_REDRAW: Final[int]

def cairo_draw_from_gl(
    cr: cairo.Context[_SomeSurface],
    surface: Surface,
    source: int,
    source_type: int,
    buffer_scale: int,
    x: int,
    y: int,
    width: int,
    height: int,
) -> None: ...
def cairo_rectangle(cr: cairo.Context[_SomeSurface], rectangle: Rectangle) -> None: ...
def cairo_region(cr: cairo.Context[_SomeSurface], region: cairo.Region) -> None: ...
def cairo_region_create_from_surface(surface: cairo.Surface) -> cairo.Region: ...
def cairo_set_source_pixbuf(
    cr: cairo.Context[_SomeSurface],
    pixbuf: GdkPixbuf.Pixbuf,
    pixbuf_x: float,
    pixbuf_y: float,
) -> None: ...
def cairo_set_source_rgba(cr: cairo.Context[_SomeSurface], rgba: RGBA) -> None: ...
def color_state_get_oklab() -> ColorState: ...
def color_state_get_oklch() -> ColorState: ...
def color_state_get_rec2100_linear() -> ColorState: ...
def color_state_get_rec2100_pq() -> ColorState: ...
def color_state_get_srgb() -> ColorState: ...
def color_state_get_srgb_linear() -> ColorState: ...
def content_deserialize_async(
    stream: Gio.InputStream,
    mime_type: str,
    type: type[Any],
    io_priority: int,
    cancellable: Gio.Cancellable | None = None,
    callback: Callable[..., None] | None = None,
    *user_data: Any,
) -> None: ...
def content_deserialize_finish(result: Gio.AsyncResult) -> tuple[bool, Any]: ...
def content_formats_parse(string: str) -> ContentFormats | None: ...
def content_register_deserializer(
    mime_type: str, type: type[Any], deserialize: Callable[..., None], *data: Any
) -> None: ...
def content_register_serializer(
    type: type[Any], mime_type: str, serialize: Callable[..., None], *data: Any
) -> None: ...
def content_serialize_async(
    stream: Gio.OutputStream,
    mime_type: str,
    value: Any,
    io_priority: int,
    cancellable: Gio.Cancellable | None = None,
    callback: Callable[..., None] | None = None,
    *user_data: Any,
) -> None: ...
def content_serialize_finish(result: Gio.AsyncResult) -> bool: ...
def dmabuf_error_quark() -> int: ...
def drag_action_is_unique(action: DragAction) -> bool: ...
def events_get_angle(event1: Event, event2: Event) -> tuple[bool, float]: ...
def events_get_center(event1: Event, event2: Event) -> tuple[bool, float, float]: ...
def events_get_distance(event1: Event, event2: Event) -> tuple[bool, float]: ...
def gl_error_quark() -> int: ...
def intern_mime_type(string: str) -> str | None: ...
def keyval_convert_case(symbol: int) -> tuple[int, int]: ...
def keyval_from_name(keyval_name: str) -> int: ...
def keyval_is_lower(keyval: int) -> bool: ...
def keyval_is_upper(keyval: int) -> bool: ...
def keyval_name(keyval: int) -> str | None: ...
def keyval_to_lower(keyval: int) -> int: ...
def keyval_to_unicode(keyval: int) -> int: ...
def keyval_to_upper(keyval: int) -> int: ...
def paintable_new_empty(intrinsic_width: int, intrinsic_height: int) -> Paintable: ...
def pixbuf_get_from_surface(
    surface: cairo.Surface, src_x: int, src_y: int, width: int, height: int
) -> GdkPixbuf.Pixbuf | None: ...
def pixbuf_get_from_texture(texture: Texture) -> GdkPixbuf.Pixbuf | None: ...
def set_allowed_backends(backends: str) -> None: ...
def texture_error_quark() -> int: ...
def unicode_to_keyval(wc: int) -> int: ...
def vulkan_error_quark() -> int: ...

class AppLaunchContext(Gio.AppLaunchContext):
    """
    :Constructors:

    ::

        AppLaunchContext(**properties)

    Object GdkAppLaunchContext

    Properties from GdkAppLaunchContext:
      display -> GdkDisplay: display

    Signals from GAppLaunchContext:
      launch-failed (gchararray)
      launch-started (GAppInfo, GVariant)
      launched (GAppInfo, GVariant)

    Signals from GObject:
      notify (GParam)
    """
    class Props(Gio.AppLaunchContext.Props):
        display: Display

    @property
    def props(self) -> Props: ...
    def __init__(self, *, display: Display = ...) -> None: ...
    def get_display(self) -> Display: ...
    def set_desktop(self, desktop: int) -> None: ...
    def set_icon(self, icon: Gio.Icon | None = None) -> None: ...
    def set_icon_name(self, icon_name: str | None = None) -> None: ...
    def set_timestamp(self, timestamp: int) -> None: ...

class ButtonEvent(Event):
    """
    :Constructors:

    ::

        ButtonEvent(**properties)
    """
    def get_button(self) -> int: ...

class CairoContext(DrawContext):
    """
    :Constructors:

    ::

        CairoContext(**properties)

    Object GdkCairoContext

    Properties from GdkDrawContext:
      display -> GdkDisplay: display
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """
    class Props(DrawContext.Props):
        display: Display | None
        surface: Surface | None

    @property
    def props(self) -> Props: ...
    def __init__(self, *, display: Display = ..., surface: Surface = ...) -> None: ...
    def cairo_create(self) -> cairo.Context | None: ...

class CicpParams(GObject.Object):
    """
    :Constructors:

    ::

        CicpParams(**properties)
        new() -> Gdk.CicpParams

    Object GdkCicpParams

    Properties from GdkCicpParams:
      color-primaries -> guint: color-primaries
      transfer-function -> guint: transfer-function
      matrix-coefficients -> guint: matrix-coefficients
      range -> GdkCicpRange: range

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        color_primaries: int
        matrix_coefficients: int
        range: CicpRange
        transfer_function: int

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        color_primaries: int = ...,
        matrix_coefficients: int = ...,
        range: CicpRange = ...,
        transfer_function: int = ...,
    ) -> None: ...
    def build_color_state(self) -> ColorState: ...
    def get_color_primaries(self) -> int: ...
    def get_matrix_coefficients(self) -> int: ...
    def get_range(self) -> CicpRange: ...
    def get_transfer_function(self) -> int: ...
    @classmethod
    def new(cls) -> CicpParams: ...
    def set_color_primaries(self, color_primaries: int) -> None: ...
    def set_matrix_coefficients(self, matrix_coefficients: int) -> None: ...
    def set_range(self, range: CicpRange) -> None: ...
    def set_transfer_function(self, transfer_function: int) -> None: ...

class CicpParamsClass(GObject.GPointer): ...

class Clipboard(GObject.Object):
    """
    :Constructors:

    ::

        Clipboard(**properties)

    Object GdkClipboard

    Signals from GdkClipboard:
      changed ()

    Properties from GdkClipboard:
      display -> GdkDisplay: display
      formats -> GdkContentFormats: formats
      local -> gboolean: local
      content -> GdkContentProvider: content

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        content: ContentProvider | None
        display: Display
        formats: ContentFormats
        local: bool

    @property
    def props(self) -> Props: ...
    def __init__(self, *, display: Display = ...) -> None: ...
    def get_content(self) -> ContentProvider | None: ...
    def get_display(self) -> Display: ...
    def get_formats(self) -> ContentFormats: ...
    def is_local(self) -> bool: ...
    def read_async(
        self,
        mime_types: Sequence[str],
        io_priority: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def read_finish(self, result: Gio.AsyncResult) -> tuple[Gio.InputStream, str]: ...
    def read_text_async(
        self,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    # override
    def read_text_finish(self, result: Gio.AsyncResult) -> str | None: ...
    def read_texture_async(
        self,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    # override
    def read_texture_finish(self, result: Gio.AsyncResult) -> Texture | None: ...
    def read_value_async(
        self,
        type: type[Any],
        io_priority: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def read_value_finish(self, result: Gio.AsyncResult) -> Any: ...
    def set(self, value: Any) -> None: ...
    def set_content(self, provider: ContentProvider | None = None) -> bool: ...
    def store_async(
        self,
        io_priority: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def store_finish(self, result: Gio.AsyncResult) -> bool: ...

class ColorState(GObject.GBoxed):
    def create_cicp_params(self) -> CicpParams | None: ...
    def equal(self, other: ColorState) -> bool: ...
    def equivalent(self, other: ColorState) -> bool: ...
    @staticmethod
    def get_oklab() -> ColorState: ...
    @staticmethod
    def get_oklch() -> ColorState: ...
    @staticmethod
    def get_rec2100_linear() -> ColorState: ...
    @staticmethod
    def get_rec2100_pq() -> ColorState: ...
    @staticmethod
    def get_srgb() -> ColorState: ...
    @staticmethod
    def get_srgb_linear() -> ColorState: ...
    def ref(self) -> ColorState: ...
    def unref(self) -> None: ...

class ContentDeserializer(GObject.Object, Gio.AsyncResult):
    """
    :Constructors:

    ::

        ContentDeserializer(**properties)

    Object GdkContentDeserializer

    Signals from GObject:
      notify (GParam)
    """
    def get_cancellable(self) -> Gio.Cancellable | None: ...
    def get_gtype(self) -> type[Any]: ...
    def get_input_stream(self) -> Gio.InputStream: ...
    def get_mime_type(self) -> str: ...
    def get_priority(self) -> int: ...
    def get_task_data(self) -> None: ...
    def get_user_data(self) -> None: ...
    def get_value(self) -> Any: ...
    def return_error(self, error: GLib.Error) -> None: ...
    def return_success(self) -> None: ...
    def set_task_data(self, data: None, notify: Callable[[None], None]) -> None: ...

class ContentFormats(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(mime_types:list=None) -> Gdk.ContentFormats
        new_for_gtype(type:GType) -> Gdk.ContentFormats
    """
    @staticmethod
    def __new__(cls: type[Self], mime_types: Sequence[str] | None = None) -> Self: ...
    # override
    def contain_gtype(self, type: Any) -> bool: ...
    def contain_mime_type(self, mime_type: str) -> bool: ...
    def get_gtypes(self) -> list[type[Any]] | None: ...
    def get_mime_types(self) -> list[str] | None: ...
    def is_empty(self) -> bool: ...
    def match(self, second: ContentFormats) -> bool: ...
    def match_gtype(self, second: ContentFormats) -> type[Any]: ...
    def match_mime_type(self, second: ContentFormats) -> str | None: ...
    @classmethod
    def new(cls, mime_types: Sequence[str] | None = None) -> ContentFormats: ...
    # override
    @classmethod
    def new_for_gtype(cls, type: Any) -> ContentFormats: ...
    @staticmethod
    def parse(string: str) -> ContentFormats | None: ...
    def print_(self, string: GLib.String) -> None: ...
    def ref(self) -> ContentFormats: ...
    def to_string(self) -> str: ...
    def union(self, second: ContentFormats) -> ContentFormats: ...
    def union_deserialize_gtypes(self) -> ContentFormats: ...
    def union_deserialize_mime_types(self) -> ContentFormats: ...
    def union_serialize_gtypes(self) -> ContentFormats: ...
    def union_serialize_mime_types(self) -> ContentFormats: ...
    def unref(self) -> None: ...

class ContentFormatsBuilder(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Gdk.ContentFormatsBuilder
    """
    @staticmethod
    def __new__(cls: type[Self]) -> Self: ...
    def add_formats(self, formats: ContentFormats) -> None: ...
    def add_gtype(self, type: type[Any]) -> None: ...
    def add_mime_type(self, mime_type: str) -> None: ...
    @classmethod
    def new(cls) -> ContentFormatsBuilder: ...
    def ref(self) -> ContentFormatsBuilder: ...
    def to_formats(self) -> ContentFormats: ...
    def unref(self) -> None: ...

class ContentProvider(GObject.Object):
    """
    :Constructors:

    ::

        ContentProvider(**properties)
        new_for_bytes(mime_type:str, bytes:GLib.Bytes) -> Gdk.ContentProvider
        new_for_value(value:GObject.Value) -> Gdk.ContentProvider
        new_union(providers:list=None) -> Gdk.ContentProvider

    Object GdkContentProvider

    Signals from GdkContentProvider:
      content-changed ()

    Properties from GdkContentProvider:
      formats -> GdkContentFormats: formats
      storable-formats -> GdkContentFormats: storable-formats

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        formats: ContentFormats
        storable_formats: ContentFormats

    @property
    def props(self) -> Props: ...
    @property
    def parent(self) -> GObject.Object: ...
    def content_changed(self) -> None: ...
    def do_attach_clipboard(self, clipboard: Clipboard) -> None: ...
    def do_content_changed(self) -> None: ...
    def do_detach_clipboard(self, clipboard: Clipboard) -> None: ...
    def do_get_value(self) -> tuple[bool, Any]: ...
    def do_ref_formats(self) -> ContentFormats: ...
    def do_ref_storable_formats(self) -> ContentFormats: ...
    def do_write_mime_type_async(
        self,
        mime_type: str,
        stream: Gio.OutputStream,
        io_priority: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def do_write_mime_type_finish(self, result: Gio.AsyncResult) -> bool: ...
    def get_value(self) -> tuple[bool, Any]: ...
    @classmethod
    def new_for_bytes(cls, mime_type: str, bytes: GLib.Bytes) -> ContentProvider: ...
    @classmethod
    def new_for_value(cls, value: Any) -> ContentProvider: ...
    @classmethod
    def new_union(
        cls, providers: Sequence[ContentProvider] | None = None
    ) -> ContentProvider: ...
    def ref_formats(self) -> ContentFormats: ...
    def ref_storable_formats(self) -> ContentFormats: ...
    def write_mime_type_async(
        self,
        mime_type: str,
        stream: Gio.OutputStream,
        io_priority: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def write_mime_type_finish(self, result: Gio.AsyncResult) -> bool: ...

class ContentProviderClass(GObject.GPointer):
    """
    :Constructors:

    ::

        ContentProviderClass()
    """
    @property
    def parent_class(self) -> GObject.ObjectClass: ...
    @property
    def content_changed(self) -> Callable[[ContentProvider], None]: ...
    @property
    def attach_clipboard(self) -> Callable[[ContentProvider, Clipboard], None]: ...
    @property
    def detach_clipboard(self) -> Callable[[ContentProvider, Clipboard], None]: ...
    @property
    def ref_formats(self) -> Callable[[ContentProvider], ContentFormats]: ...
    @property
    def ref_storable_formats(self) -> Callable[[ContentProvider], ContentFormats]: ...
    @property
    def write_mime_type_async(self) -> Callable[..., None]: ...
    @property
    def write_mime_type_finish(
        self,
    ) -> Callable[[ContentProvider, Gio.AsyncResult], bool]: ...
    @property
    def get_value(self) -> Callable[[ContentProvider], tuple[bool, Any]]: ...
    @property
    def padding(self) -> list[None]: ...

class ContentSerializer(GObject.Object, Gio.AsyncResult):
    """
    :Constructors:

    ::

        ContentSerializer(**properties)

    Object GdkContentSerializer

    Signals from GObject:
      notify (GParam)
    """
    def get_cancellable(self) -> Gio.Cancellable | None: ...
    def get_gtype(self) -> type[Any]: ...
    def get_mime_type(self) -> str: ...
    def get_output_stream(self) -> Gio.OutputStream: ...
    def get_priority(self) -> int: ...
    def get_task_data(self) -> None: ...
    def get_user_data(self) -> None: ...
    def get_value(self) -> Any: ...
    def return_error(self, error: GLib.Error) -> None: ...
    def return_success(self) -> None: ...
    def set_task_data(self, data: None, notify: Callable[[None], None]) -> None: ...

class CrossingEvent(Event):
    """
    :Constructors:

    ::

        CrossingEvent(**properties)
    """
    def get_detail(self) -> NotifyType: ...
    def get_focus(self) -> bool: ...
    def get_mode(self) -> CrossingMode: ...

class Cursor(GObject.Object):
    """
    :Constructors:

    ::

        Cursor(**properties)
        new_from_callback(callback:Gdk.CursorGetTextureCallback, data=None, fallback:Gdk.Cursor=None) -> Gdk.Cursor or None
        new_from_name(name:str, fallback:Gdk.Cursor=None) -> Gdk.Cursor or None
        new_from_texture(texture:Gdk.Texture, hotspot_x:int, hotspot_y:int, fallback:Gdk.Cursor=None) -> Gdk.Cursor

    Object GdkCursor

    Properties from GdkCursor:
      fallback -> GdkCursor: fallback
      hotspot-x -> gint: hotspot-x
      hotspot-y -> gint: hotspot-y
      name -> gchararray: name
      texture -> GdkTexture: texture

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        fallback: Cursor | None
        hotspot_x: int
        hotspot_y: int
        name: str | None
        texture: Texture | None

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        fallback: Cursor = ...,
        hotspot_x: int = ...,
        hotspot_y: int = ...,
        name: str = ...,
        texture: Texture = ...,
    ) -> None: ...
    def get_fallback(self) -> Cursor | None: ...
    def get_hotspot_x(self) -> int: ...
    def get_hotspot_y(self) -> int: ...
    def get_name(self) -> str | None: ...
    def get_texture(self) -> Texture | None: ...
    @classmethod
    def new_from_callback(
        cls,
        callback: Callable[..., tuple[Texture | None, int, int, int, int]],
        fallback: Cursor | None = None,
        *data: Any,
    ) -> Cursor | None: ...
    @classmethod
    def new_from_name(
        cls, name: str, fallback: Cursor | None = None
    ) -> Cursor | None: ...
    @classmethod
    def new_from_texture(
        cls,
        texture: Texture,
        hotspot_x: int,
        hotspot_y: int,
        fallback: Cursor | None = None,
    ) -> Cursor: ...

class DNDEvent(Event):
    """
    :Constructors:

    ::

        DNDEvent(**properties)
    """
    def get_drop(self) -> Drop | None: ...

class DeleteEvent(Event): ...

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
      display -> GdkDisplay: display
      name -> gchararray: name
      source -> GdkInputSource: source
      has-cursor -> gboolean: has-cursor
      n-axes -> guint: n-axes
      vendor-id -> gchararray: vendor-id
      product-id -> gchararray: product-id
      seat -> GdkSeat: seat
      num-touches -> guint: num-touches
      tool -> GdkDeviceTool: tool
      direction -> PangoDirection: direction
      has-bidi-layouts -> gboolean: has-bidi-layouts
      caps-lock-state -> gboolean: caps-lock-state
      num-lock-state -> gboolean: num-lock-state
      scroll-lock-state -> gboolean: scroll-lock-state
      modifier-state -> GdkModifierType: modifier-state
      layout-names -> GStrv: layout-names
      active-layout-index -> gint: active-layout-index

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        active_layout_index: int
        caps_lock_state: bool
        direction: Pango.Direction
        display: Display
        has_bidi_layouts: bool
        has_cursor: bool
        layout_names: list[str] | None
        modifier_state: ModifierType
        n_axes: int
        name: str
        num_lock_state: bool
        num_touches: int
        product_id: str | None
        scroll_lock_state: bool
        seat: Seat
        source: InputSource
        tool: DeviceTool | None
        vendor_id: str | None

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        display: Display = ...,
        has_cursor: bool = ...,
        name: str = ...,
        num_touches: int = ...,
        product_id: str = ...,
        seat: Seat = ...,
        source: InputSource = ...,
        vendor_id: str = ...,
    ) -> None: ...
    def get_active_layout_index(self) -> int: ...
    def get_caps_lock_state(self) -> bool: ...
    def get_device_tool(self) -> DeviceTool | None: ...
    def get_direction(self) -> Pango.Direction: ...
    def get_display(self) -> Display: ...
    def get_has_cursor(self) -> bool: ...
    def get_layout_names(self) -> list[str] | None: ...
    def get_modifier_state(self) -> ModifierType: ...
    def get_name(self) -> str: ...
    def get_num_lock_state(self) -> bool: ...
    def get_num_touches(self) -> int: ...
    def get_product_id(self) -> str | None: ...
    def get_scroll_lock_state(self) -> bool: ...
    def get_seat(self) -> Seat: ...
    def get_source(self) -> InputSource: ...
    def get_surface_at_position(self) -> tuple[Surface | None, float, float]: ...
    def get_timestamp(self) -> int: ...
    def get_vendor_id(self) -> str | None: ...
    def has_bidi_layouts(self) -> bool: ...

class DevicePad(GObject.GInterface):
    """
    Interface GdkDevicePad

    Signals from GObject:
      notify (GParam)
    """
    def get_feature_group(self, feature: DevicePadFeature, feature_idx: int) -> int: ...
    def get_group_n_modes(self, group_idx: int) -> int: ...
    def get_n_features(self, feature: DevicePadFeature) -> int: ...
    def get_n_groups(self) -> int: ...

class DevicePadInterface(GObject.GPointer): ...

class DeviceTool(GObject.Object):
    """
    :Constructors:

    ::

        DeviceTool(**properties)

    Object GdkDeviceTool

    Properties from GdkDeviceTool:
      serial -> guint64: serial
      tool-type -> GdkDeviceToolType: tool-type
      axes -> GdkAxisFlags: axes
      hardware-id -> guint64: hardware-id

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        axes: AxisFlags
        hardware_id: int
        serial: int
        tool_type: DeviceToolType

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
    def get_axes(self) -> AxisFlags: ...
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
      setting-changed (gchararray)

    Properties from GdkDisplay:
      composited -> gboolean: composited
      rgba -> gboolean: rgba
      shadow-width -> gboolean: shadow-width
      input-shapes -> gboolean: input-shapes
      dmabuf-formats -> GdkDmabufFormats: dmabuf-formats

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        composited: bool
        dmabuf_formats: DmabufFormats
        input_shapes: bool
        rgba: bool
        shadow_width: bool

    @property
    def props(self) -> Props: ...
    def beep(self) -> None: ...
    def close(self) -> None: ...
    def create_gl_context(self) -> GLContext: ...
    def device_is_grabbed(self, device: Device) -> bool: ...
    def flush(self) -> None: ...
    def get_app_launch_context(self) -> AppLaunchContext: ...
    def get_clipboard(self) -> Clipboard: ...
    @staticmethod
    def get_default() -> Display | None: ...
    def get_default_seat(self) -> Seat | None: ...
    def get_dmabuf_formats(self) -> DmabufFormats: ...
    def get_monitor_at_surface(self, surface: Surface) -> Monitor | None: ...
    # override
    def get_monitors(self) -> Gio.ListModel[Monitor]: ...
    def get_name(self) -> str: ...
    def get_primary_clipboard(self) -> Clipboard: ...
    def get_setting(self, name: str, value: Any) -> bool: ...
    def get_startup_notification_id(self) -> str | None: ...
    def is_closed(self) -> bool: ...
    def is_composited(self) -> bool: ...
    def is_rgba(self) -> bool: ...
    def list_seats(self) -> list[Seat]: ...
    def map_keycode(self, keycode: int) -> tuple[bool, list[KeymapKey], list[int]]: ...
    def map_keyval(self, keyval: int) -> tuple[bool, list[KeymapKey]]: ...
    def notify_startup_complete(self, startup_id: str) -> None: ...
    @staticmethod
    def open(display_name: str | None = None) -> Display | None: ...
    def prepare_gl(self) -> bool: ...
    def put_event(self, event: Event) -> None: ...
    def supports_input_shapes(self) -> bool: ...
    def supports_shadow_width(self) -> bool: ...
    def sync(self) -> None: ...
    def translate_key(
        self, keycode: int, state: ModifierType, group: int
    ) -> tuple[bool, int, int, int, ModifierType]: ...

class DisplayManager(GObject.Object):
    """
    :Constructors:

    ::

        DisplayManager(**properties)

    Object GdkDisplayManager

    Signals from GdkDisplayManager:
      display-opened (GdkDisplay)

    Properties from GdkDisplayManager:
      default-display -> GdkDisplay: default-display

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        default_display: Display | None

    @property
    def props(self) -> Props: ...
    def __init__(self, *, default_display: Display = ...) -> None: ...
    @staticmethod
    def get() -> DisplayManager: ...
    def get_default_display(self) -> Display | None: ...
    def list_displays(self) -> list[Display]: ...
    def open_display(self, name: str | None = None) -> Display | None: ...
    def set_default_display(self, display: Display) -> None: ...

class DmabufFormats(GObject.GBoxed):
    def contains(self, fourcc: int, modifier: int) -> bool: ...
    def equal(self, formats2: DmabufFormats | None = None) -> bool: ...
    def get_format(self, idx: int) -> tuple[int, int]: ...
    def get_n_formats(self) -> int: ...
    def ref(self) -> DmabufFormats: ...
    def unref(self) -> None: ...

class DmabufTexture(Texture, Paintable, Gio.Icon, Gio.LoadableIcon):
    """
    :Constructors:

    ::

        DmabufTexture(**properties)

    Object GdkDmabufTexture

    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()

    Properties from GdkTexture:
      width -> gint: width
      height -> gint: height
      color-state -> GdkColorState: color-state

    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()

    Signals from GObject:
      notify (GParam)
    """
    class Props(Texture.Props):
        color_state: ColorState
        height: int
        width: int

    @property
    def props(self) -> Props: ...
    def __init__(
        self, *, color_state: ColorState = ..., height: int = ..., width: int = ...
    ) -> None: ...

class DmabufTextureBuilder(GObject.Object):
    """
    :Constructors:

    ::

        DmabufTextureBuilder(**properties)
        new() -> Gdk.DmabufTextureBuilder

    Object GdkDmabufTextureBuilder

    Properties from GdkDmabufTextureBuilder:
      display -> GdkDisplay: display
      width -> guint: width
      height -> guint: height
      fourcc -> guint: fourcc
      modifier -> guint64: modifier
      premultiplied -> gboolean: premultiplied
      n-planes -> guint: n-planes
      color-state -> GdkColorState: color-state
      update-region -> CairoRegion: update-region
      update-texture -> GdkTexture: update-texture

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        color_state: ColorState | None
        display: Display
        fourcc: int
        height: int
        modifier: int
        n_planes: int
        premultiplied: bool
        update_region: cairo.Region | None
        update_texture: Texture | None
        width: int

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        color_state: ColorState | None = ...,
        display: Display = ...,
        fourcc: int = ...,
        height: int = ...,
        modifier: int = ...,
        n_planes: int = ...,
        premultiplied: bool = ...,
        update_region: cairo.Region | None = ...,
        update_texture: Texture | None = ...,
        width: int = ...,
    ) -> None: ...
    def build(
        self, destroy: Callable[[None], None] | None, data: None
    ) -> Texture | None: ...
    def get_color_state(self) -> ColorState | None: ...
    def get_display(self) -> Display: ...
    def get_fd(self, plane: int) -> int: ...
    def get_fourcc(self) -> int: ...
    def get_height(self) -> int: ...
    def get_modifier(self) -> int: ...
    def get_n_planes(self) -> int: ...
    def get_offset(self, plane: int) -> int: ...
    def get_premultiplied(self) -> bool: ...
    def get_stride(self, plane: int) -> int: ...
    def get_update_region(self) -> cairo.Region | None: ...
    def get_update_texture(self) -> Texture | None: ...
    def get_width(self) -> int: ...
    @classmethod
    def new(cls) -> DmabufTextureBuilder: ...
    def set_color_state(self, color_state: ColorState | None = None) -> None: ...
    def set_display(self, display: Display) -> None: ...
    def set_fd(self, plane: int, fd: int) -> None: ...
    def set_fourcc(self, fourcc: int) -> None: ...
    def set_height(self, height: int) -> None: ...
    def set_modifier(self, modifier: int) -> None: ...
    def set_n_planes(self, n_planes: int) -> None: ...
    def set_offset(self, plane: int, offset: int) -> None: ...
    def set_premultiplied(self, premultiplied: bool) -> None: ...
    def set_stride(self, plane: int, stride: int) -> None: ...
    def set_update_region(self, region: cairo.Region | None = None) -> None: ...
    def set_update_texture(self, texture: Texture | None = None) -> None: ...
    def set_width(self, width: int) -> None: ...

class DmabufTextureBuilderClass(GObject.GPointer): ...
class DmabufTextureClass(GObject.GPointer): ...

class Drag(GObject.Object):
    """
    :Constructors:

    ::

        Drag(**properties)

    Object GdkDrag

    Signals from GdkDrag:
      cancel (GdkDragCancelReason)
      drop-performed ()
      dnd-finished ()

    Properties from GdkDrag:
      content -> GdkContentProvider: content
      device -> GdkDevice: device
      display -> GdkDisplay: display
      formats -> GdkContentFormats: formats
      selected-action -> GdkDragAction: selected-action
      actions -> GdkDragAction: actions
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        actions: DragAction
        content: ContentProvider
        device: Device
        display: Display
        formats: ContentFormats
        selected_action: DragAction
        surface: Surface

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        actions: DragAction = ...,
        content: ContentProvider = ...,
        device: Device = ...,
        formats: ContentFormats = ...,
        selected_action: DragAction = ...,
        surface: Surface = ...,
    ) -> None: ...
    @staticmethod
    def begin(
        surface: Surface,
        device: Device,
        content: ContentProvider,
        actions: DragAction,
        dx: float,
        dy: float,
    ) -> Drag | None: ...
    def drop_done(self, success: bool) -> None: ...
    def get_actions(self) -> DragAction: ...
    def get_content(self) -> ContentProvider: ...
    def get_device(self) -> Device: ...
    def get_display(self) -> Display: ...
    def get_drag_surface(self) -> Surface | None: ...
    def get_formats(self) -> ContentFormats: ...
    def get_selected_action(self) -> DragAction: ...
    def get_surface(self) -> Surface: ...
    def set_hotspot(self, hot_x: int, hot_y: int) -> None: ...

class DragSurface(GObject.GInterface):
    """
    Interface GdkDragSurface

    Signals from GObject:
      notify (GParam)
    """
    def present(self, width: int, height: int) -> bool: ...

class DragSurfaceInterface(GObject.GPointer): ...

class DragSurfaceSize(GObject.GPointer):
    def set_size(self, width: int, height: int) -> None: ...

class DrawContext(GObject.Object):
    """
    :Constructors:

    ::

        DrawContext(**properties)

    Object GdkDrawContext

    Properties from GdkDrawContext:
      display -> GdkDisplay: display
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        display: Display | None
        surface: Surface | None

    @property
    def props(self) -> Props: ...
    def __init__(self, *, display: Display = ..., surface: Surface = ...) -> None: ...
    def begin_frame(self, region: cairo.Region) -> None: ...
    def end_frame(self) -> None: ...
    def get_display(self) -> Display | None: ...
    def get_frame_region(self) -> cairo.Region | None: ...
    def get_surface(self) -> Surface | None: ...
    def is_in_frame(self) -> bool: ...

class Drop(GObject.Object):
    """
    :Constructors:

    ::

        Drop(**properties)

    Object GdkDrop

    Properties from GdkDrop:
      actions -> GdkDragAction: actions
      device -> GdkDevice: device
      display -> GdkDisplay: display
      drag -> GdkDrag: drag
      formats -> GdkContentFormats: formats
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        actions: DragAction
        device: Device
        display: Display
        drag: Drag | None
        formats: ContentFormats
        surface: Surface

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        actions: DragAction = ...,
        device: Device = ...,
        drag: Drag = ...,
        formats: ContentFormats = ...,
        surface: Surface = ...,
    ) -> None: ...
    def finish(self, action: DragAction) -> None: ...
    def get_actions(self) -> DragAction: ...
    def get_device(self) -> Device: ...
    def get_display(self) -> Display: ...
    def get_drag(self) -> Drag | None: ...
    def get_formats(self) -> ContentFormats: ...
    def get_surface(self) -> Surface: ...
    def read_async(
        self,
        mime_types: Sequence[str],
        io_priority: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def read_finish(self, result: Gio.AsyncResult) -> tuple[Gio.InputStream, str]: ...
    def read_value_async(
        self,
        type: type[Any],
        io_priority: int,
        cancellable: Gio.Cancellable | None = None,
        callback: Callable[..., None] | None = None,
        *user_data: Any,
    ) -> None: ...
    def read_value_finish(self, result: Gio.AsyncResult) -> Any: ...
    def status(self, actions: DragAction, preferred: DragAction) -> None: ...

class Event(_gi.Fundamental):
    """
    :Constructors:

    ::

        Event(**properties)
    """
    def get_axes(self) -> tuple[bool, list[float]]: ...
    def get_axis(self, axis_use: AxisUse) -> tuple[bool, float]: ...
    def get_device(self) -> Device | None: ...
    def get_device_tool(self) -> DeviceTool | None: ...
    def get_display(self) -> Display | None: ...
    def get_event_sequence(self) -> EventSequence: ...
    def get_event_type(self) -> EventType: ...
    def get_history(self) -> list[TimeCoord] | None: ...
    def get_modifier_state(self) -> ModifierType: ...
    def get_pointer_emulated(self) -> bool: ...
    def get_position(self) -> tuple[bool, float, float]: ...
    def get_seat(self) -> Seat | None: ...
    def get_surface(self) -> Surface | None: ...
    def get_time(self) -> int: ...
    def ref(self) -> Event: ...
    def triggers_context_menu(self) -> bool: ...
    def unref(self) -> None: ...

class EventSequence(GObject.GBoxed): ...

class FileList(GObject.GBoxed):
    """
    :Constructors:

    ::

        new_from_array(files:list) -> Gdk.FileList
        new_from_list(files:list) -> Gdk.FileList
    """
    def __getitem__(self, index): ...  # FIXME: Override is missing typing annotation
    def __iter__(self): ...  # FIXME: Override is missing typing annotation
    def __len__(self): ...  # FIXME: Override is missing typing annotation
    @staticmethod
    def __new__(cls, files): ...  # FIXME: Override is missing typing annotation
    def get_files(self) -> list[Gio.File]: ...
    @classmethod
    def new_from_array(cls, files: Sequence[Gio.File]) -> FileList: ...
    @classmethod
    def new_from_list(cls, files: list[Gio.File]) -> FileList: ...

class FocusEvent(Event):
    """
    :Constructors:

    ::

        FocusEvent(**properties)
    """
    def get_in(self) -> bool: ...

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
    def get_fps(self) -> float: ...
    def get_frame_counter(self) -> int: ...
    def get_frame_time(self) -> int: ...
    def get_history_start(self) -> int: ...
    def get_refresh_info(self, base_time: int) -> tuple[int, int]: ...
    def get_timings(self, frame_counter: int) -> FrameTimings | None: ...
    def request_phase(self, phase: FrameClockPhase) -> None: ...

class FrameClockClass(GObject.GPointer): ...
class FrameClockPrivate(GObject.GPointer): ...

class FrameTimings(GObject.GBoxed):
    def get_complete(self) -> bool: ...
    def get_frame_counter(self) -> int: ...
    def get_frame_time(self) -> int: ...
    def get_predicted_presentation_time(self) -> int: ...
    def get_presentation_time(self) -> int: ...
    def get_refresh_interval(self) -> int: ...
    def ref(self) -> FrameTimings: ...
    def unref(self) -> None: ...

class GLContext(DrawContext):
    """
    :Constructors:

    ::

        GLContext(**properties)

    Object GdkGLContext

    Properties from GdkGLContext:
      allowed-apis -> GdkGLAPI: allowed-apis
      api -> GdkGLAPI: api
      shared-context -> GdkGLContext: shared-context

    Properties from GdkDrawContext:
      display -> GdkDisplay: display
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """
    class Props(DrawContext.Props):
        allowed_apis: GLAPI
        api: GLAPI
        shared_context: GLContext | None
        display: Display | None
        surface: Surface | None

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        allowed_apis: GLAPI = ...,
        shared_context: GLContext = ...,
        display: Display = ...,
        surface: Surface = ...,
    ) -> None: ...
    @staticmethod
    def clear_current() -> None: ...
    def get_allowed_apis(self) -> GLAPI: ...
    def get_api(self) -> GLAPI: ...
    @staticmethod
    def get_current() -> GLContext | None: ...
    def get_debug_enabled(self) -> bool: ...
    def get_display(self) -> Display | None: ...
    def get_forward_compatible(self) -> bool: ...
    def get_required_version(self) -> tuple[int, int]: ...
    def get_shared_context(self) -> GLContext | None: ...
    def get_surface(self) -> Surface | None: ...
    def get_use_es(self) -> bool: ...
    def get_version(self) -> tuple[int, int]: ...
    def is_legacy(self) -> bool: ...
    def is_shared(self, other: GLContext) -> bool: ...
    def make_current(self) -> None: ...
    def realize(self) -> bool: ...
    def set_allowed_apis(self, apis: GLAPI) -> None: ...
    def set_debug_enabled(self, enabled: bool) -> None: ...
    def set_forward_compatible(self, compatible: bool) -> None: ...
    def set_required_version(self, major: int, minor: int) -> None: ...
    def set_use_es(self, use_es: int) -> None: ...

class GLTexture(Texture, Paintable, Gio.Icon, Gio.LoadableIcon):
    """
    :Constructors:

    ::

        GLTexture(**properties)
        new(context:Gdk.GLContext, id:int, width:int, height:int, destroy:GLib.DestroyNotify, data=None) -> Gdk.GLTexture

    Object GdkGLTexture

    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()

    Properties from GdkTexture:
      width -> gint: width
      height -> gint: height
      color-state -> GdkColorState: color-state

    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()

    Signals from GObject:
      notify (GParam)
    """
    class Props(Texture.Props):
        color_state: ColorState
        height: int
        width: int

    @property
    def props(self) -> Props: ...
    def __init__(
        self, *, color_state: ColorState = ..., height: int = ..., width: int = ...
    ) -> None: ...
    @classmethod
    def new(
        cls,
        context: GLContext,
        id: int,
        width: int,
        height: int,
        destroy: Callable[[None], None],
        data: None,
    ) -> GLTexture: ...
    def release(self) -> None: ...

class GLTextureBuilder(GObject.Object):
    """
    :Constructors:

    ::

        GLTextureBuilder(**properties)
        new() -> Gdk.GLTextureBuilder

    Object GdkGLTextureBuilder

    Properties from GdkGLTextureBuilder:
      context -> GdkGLContext: context
      format -> GdkMemoryFormat: format
      has-mipmap -> gboolean: has-mipmap
      height -> gint: height
      id -> guint: id
      sync -> gpointer: sync
      color-state -> GdkColorState: color-state
      update-region -> CairoRegion: update-region
      update-texture -> GdkTexture: update-texture
      width -> gint: width

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        color_state: ColorState
        context: GLContext | None
        format: MemoryFormat
        has_mipmap: bool
        height: int
        id: int
        sync: None | None
        update_region: cairo.Region | None
        update_texture: Texture | None
        width: int

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        color_state: ColorState = ...,
        context: GLContext | None = ...,
        format: MemoryFormat = ...,
        has_mipmap: bool = ...,
        height: int = ...,
        id: int = ...,
        sync: None | None = ...,
        update_region: cairo.Region | None = ...,
        update_texture: Texture | None = ...,
        width: int = ...,
    ) -> None: ...
    def build(self, destroy: Callable[[None], None] | None, data: None) -> Texture: ...
    def get_color_state(self) -> ColorState: ...
    def get_context(self) -> GLContext | None: ...
    def get_format(self) -> MemoryFormat: ...
    def get_has_mipmap(self) -> bool: ...
    def get_height(self) -> int: ...
    def get_id(self) -> int: ...
    def get_sync(self) -> None: ...
    def get_update_region(self) -> cairo.Region | None: ...
    def get_update_texture(self) -> Texture | None: ...
    def get_width(self) -> int: ...
    @classmethod
    def new(cls) -> GLTextureBuilder: ...
    def set_color_state(self, color_state: ColorState) -> None: ...
    def set_context(self, context: GLContext | None = None) -> None: ...
    def set_format(self, format: MemoryFormat) -> None: ...
    def set_has_mipmap(self, has_mipmap: bool) -> None: ...
    def set_height(self, height: int) -> None: ...
    def set_id(self, id: int) -> None: ...
    def set_sync(self, sync: None) -> None: ...
    def set_update_region(self, region: cairo.Region | None = None) -> None: ...
    def set_update_texture(self, texture: Texture | None = None) -> None: ...
    def set_width(self, width: int) -> None: ...

class GLTextureBuilderClass(GObject.GPointer): ...
class GLTextureClass(GObject.GPointer): ...

class GrabBrokenEvent(Event):
    """
    :Constructors:

    ::

        GrabBrokenEvent(**properties)
    """
    def get_grab_surface(self) -> Surface: ...
    def get_implicit(self) -> bool: ...

class KeyEvent(Event):
    """
    :Constructors:

    ::

        KeyEvent(**properties)
    """
    def get_consumed_modifiers(self) -> ModifierType: ...
    def get_keycode(self) -> int: ...
    def get_keyval(self) -> int: ...
    def get_layout(self) -> int: ...
    def get_level(self) -> int: ...
    def get_match(self) -> tuple[bool, int, ModifierType]: ...
    def is_modifier(self) -> bool: ...
    def matches(self, keyval: int, modifiers: ModifierType) -> KeyMatch: ...

class KeymapKey(GObject.GPointer):
    """
    :Constructors:

    ::

        KeymapKey()
    """

    keycode: int
    group: int
    level: int

class MemoryTexture(Texture, Paintable, Gio.Icon, Gio.LoadableIcon):
    """
    :Constructors:

    ::

        MemoryTexture(**properties)
        new(width:int, height:int, format:Gdk.MemoryFormat, bytes:GLib.Bytes, stride:int) -> Gdk.MemoryTexture

    Object GdkMemoryTexture

    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()

    Properties from GdkTexture:
      width -> gint: width
      height -> gint: height
      color-state -> GdkColorState: color-state

    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()

    Signals from GObject:
      notify (GParam)
    """
    class Props(Texture.Props):
        color_state: ColorState
        height: int
        width: int

    @property
    def props(self) -> Props: ...
    def __init__(
        self, *, color_state: ColorState = ..., height: int = ..., width: int = ...
    ) -> None: ...
    @classmethod
    def new(
        cls,
        width: int,
        height: int,
        format: MemoryFormat,
        bytes: GLib.Bytes,
        stride: int,
    ) -> MemoryTexture: ...

class MemoryTextureBuilder(GObject.Object):
    """
    :Constructors:

    ::

        MemoryTextureBuilder(**properties)
        new() -> Gdk.MemoryTextureBuilder

    Object GdkMemoryTextureBuilder

    Properties from GdkMemoryTextureBuilder:
      bytes -> GBytes: bytes
      color-state -> GdkColorState: color-state
      format -> GdkMemoryFormat: format
      height -> gint: height
      stride -> guint64: stride
      update-region -> CairoRegion: update-region
      update-texture -> GdkTexture: update-texture
      width -> gint: width

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        bytes: GLib.Bytes | None
        color_state: ColorState
        format: MemoryFormat
        height: int
        stride: int
        update_region: cairo.Region | None
        update_texture: Texture | None
        width: int

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        bytes: GLib.Bytes | None = ...,
        color_state: ColorState = ...,
        format: MemoryFormat = ...,
        height: int = ...,
        stride: int = ...,
        update_region: cairo.Region | None = ...,
        update_texture: Texture | None = ...,
        width: int = ...,
    ) -> None: ...
    def build(self) -> Texture: ...
    def get_bytes(self) -> GLib.Bytes | None: ...
    def get_color_state(self) -> ColorState: ...
    def get_format(self) -> MemoryFormat: ...
    def get_height(self) -> int: ...
    def get_offset(self, plane: int) -> int: ...
    def get_stride(self) -> int: ...
    def get_stride_for_plane(self, plane: int) -> int: ...
    def get_update_region(self) -> cairo.Region | None: ...
    def get_update_texture(self) -> Texture | None: ...
    def get_width(self) -> int: ...
    @classmethod
    def new(cls) -> MemoryTextureBuilder: ...
    def set_bytes(self, bytes: GLib.Bytes | None = None) -> None: ...
    def set_color_state(self, color_state: ColorState) -> None: ...
    def set_format(self, format: MemoryFormat) -> None: ...
    def set_height(self, height: int) -> None: ...
    def set_offset(self, plane: int, offset: int) -> None: ...
    def set_stride(self, stride: int) -> None: ...
    def set_stride_for_plane(self, plane: int, stride: int) -> None: ...
    def set_update_region(self, region: cairo.Region | None = None) -> None: ...
    def set_update_texture(self, texture: Texture | None = None) -> None: ...
    def set_width(self, width: int) -> None: ...

class MemoryTextureBuilderClass(GObject.GPointer): ...
class MemoryTextureClass(GObject.GPointer): ...

class Monitor(GObject.Object):
    """
    :Constructors:

    ::

        Monitor(**properties)

    Object GdkMonitor

    Signals from GdkMonitor:
      invalidate ()

    Properties from GdkMonitor:
      description -> gchararray: description
      display -> GdkDisplay: display
      manufacturer -> gchararray: manufacturer
      model -> gchararray: model
      connector -> gchararray: connector
      scale-factor -> gint: scale-factor
      scale -> gdouble: scale
      geometry -> GdkRectangle: geometry
      width-mm -> gint: width-mm
      height-mm -> gint: height-mm
      refresh-rate -> gint: refresh-rate
      subpixel-layout -> GdkSubpixelLayout: subpixel-layout
      valid -> gboolean: valid

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        connector: str | None
        description: str | None
        display: Display
        geometry: Rectangle
        height_mm: int
        manufacturer: str | None
        model: str | None
        refresh_rate: int
        scale: float
        scale_factor: int
        subpixel_layout: SubpixelLayout
        valid: bool
        width_mm: int

    @property
    def props(self) -> Props: ...
    def __init__(self, *, display: Display = ...) -> None: ...
    def get_connector(self) -> str | None: ...
    def get_description(self) -> str | None: ...
    def get_display(self) -> Display: ...
    def get_geometry(self) -> Rectangle: ...
    def get_height_mm(self) -> int: ...
    def get_manufacturer(self) -> str | None: ...
    def get_model(self) -> str | None: ...
    def get_refresh_rate(self) -> int: ...
    def get_scale(self) -> float: ...
    def get_scale_factor(self) -> int: ...
    def get_subpixel_layout(self) -> SubpixelLayout: ...
    def get_width_mm(self) -> int: ...
    def is_valid(self) -> bool: ...

class MonitorClass(GObject.GPointer): ...
class MotionEvent(Event): ...

class PadEvent(Event):
    """
    :Constructors:

    ::

        PadEvent(**properties)
    """
    def get_axis_value(self) -> tuple[int, float]: ...
    def get_button(self) -> int: ...
    def get_group_mode(self) -> tuple[int, int]: ...

class Paintable(GObject.GInterface):
    """
    Interface GdkPaintable

    Signals from GObject:
      notify (GParam)
    """
    def compute_concrete_size(
        self,
        specified_width: float,
        specified_height: float,
        default_width: float,
        default_height: float,
    ) -> tuple[float, float]: ...
    def get_current_image(self) -> Paintable: ...
    def get_flags(self) -> PaintableFlags: ...
    def get_intrinsic_aspect_ratio(self) -> float: ...
    def get_intrinsic_height(self) -> int: ...
    def get_intrinsic_width(self) -> int: ...
    def invalidate_contents(self) -> None: ...
    def invalidate_size(self) -> None: ...
    @staticmethod
    def new_empty(intrinsic_width: int, intrinsic_height: int) -> Paintable: ...
    def snapshot(self, snapshot: Snapshot, width: float, height: float) -> None: ...

class PaintableInterface(GObject.GPointer):
    """
    :Constructors:

    ::

        PaintableInterface()
    """
    @property
    def g_iface(self) -> GObject.TypeInterface: ...
    @property
    def snapshot(self) -> Callable[[Paintable, Snapshot, float, float], None]: ...
    @property
    def get_current_image(self) -> Callable[[Paintable], Paintable]: ...
    @property
    def get_flags(self) -> Callable[[Paintable], PaintableFlags]: ...
    @property
    def get_intrinsic_width(self) -> Callable[[Paintable], int]: ...
    @property
    def get_intrinsic_height(self) -> Callable[[Paintable], int]: ...
    @property
    def get_intrinsic_aspect_ratio(self) -> Callable[[Paintable], float]: ...

class Popup(GObject.GInterface):
    """
    Interface GdkPopup

    Signals from GObject:
      notify (GParam)
    """
    def get_autohide(self) -> bool: ...
    def get_parent(self) -> Surface | None: ...
    def get_position_x(self) -> int: ...
    def get_position_y(self) -> int: ...
    def get_rect_anchor(self) -> Gravity: ...
    def get_surface_anchor(self) -> Gravity: ...
    def present(self, width: int, height: int, layout: PopupLayout) -> bool: ...

class PopupInterface(GObject.GPointer): ...

class PopupLayout(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(anchor_rect:Gdk.Rectangle, rect_anchor:Gdk.Gravity, surface_anchor:Gdk.Gravity) -> Gdk.PopupLayout
    """
    @staticmethod
    def __new__(
        cls: type[Self],
        anchor_rect: Rectangle,
        rect_anchor: Gravity,
        surface_anchor: Gravity,
    ) -> Self: ...
    def copy(self) -> PopupLayout: ...
    def equal(self, other: PopupLayout) -> bool: ...
    def get_anchor_hints(self) -> AnchorHints: ...
    def get_anchor_rect(self) -> Rectangle: ...
    def get_offset(self) -> tuple[int, int]: ...
    def get_rect_anchor(self) -> Gravity: ...
    def get_shadow_width(self) -> tuple[int, int, int, int]: ...
    def get_surface_anchor(self) -> Gravity: ...
    @classmethod
    def new(
        cls, anchor_rect: Rectangle, rect_anchor: Gravity, surface_anchor: Gravity
    ) -> PopupLayout: ...
    def ref(self) -> PopupLayout: ...
    def set_anchor_hints(self, anchor_hints: AnchorHints) -> None: ...
    def set_anchor_rect(self, anchor_rect: Rectangle) -> None: ...
    def set_offset(self, dx: int, dy: int) -> None: ...
    def set_rect_anchor(self, anchor: Gravity) -> None: ...
    def set_shadow_width(
        self, left: int, right: int, top: int, bottom: int
    ) -> None: ...
    def set_surface_anchor(self, anchor: Gravity) -> None: ...
    def unref(self) -> None: ...

class ProximityEvent(Event): ...

# override
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

    def __init__(
        self,
        red: float = 1.0,
        green: float = 1.0,
        blue: float = 1.0,
        alpha: float = 1.0,
    ) -> None: ...
    def copy(self) -> RGBA: ...
    def equal(self, p2: RGBA) -> bool: ...
    def free(self) -> None: ...
    def hash(self) -> int: ...
    def is_clear(self) -> bool: ...
    def is_opaque(self) -> bool: ...
    def parse(self, spec: str) -> bool: ...
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
    def contains_point(self, x: int, y: int) -> bool: ...
    def equal(self, rect2: Rectangle) -> bool: ...
    def intersect(self, src2: Rectangle) -> tuple[bool, Rectangle]: ...
    def union(self, src2: Rectangle) -> Rectangle: ...

class ScrollEvent(Event):
    """
    :Constructors:

    ::

        ScrollEvent(**properties)
    """
    def get_deltas(self) -> tuple[float, float]: ...
    def get_direction(self) -> ScrollDirection: ...
    def get_relative_direction(self) -> ScrollRelativeDirection: ...
    def get_unit(self) -> ScrollUnit: ...
    def is_stop(self) -> bool: ...

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
      display -> GdkDisplay: display

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        display: Display

    @property
    def props(self) -> Props: ...
    @property
    def parent_instance(self) -> GObject.Object: ...
    def __init__(self, *, display: Display = ...) -> None: ...
    def get_capabilities(self) -> SeatCapabilities: ...
    def get_devices(self, capabilities: SeatCapabilities) -> list[Device]: ...
    def get_display(self) -> Display: ...
    def get_keyboard(self) -> Device | None: ...
    def get_pointer(self) -> Device | None: ...
    def get_tools(self) -> list[DeviceTool]: ...

class Snapshot(GObject.Object): ...
class SnapshotClass(GObject.GPointer): ...

class Surface(GObject.Object):
    """
    :Constructors:

    ::

        Surface(**properties)
        new_popup(parent:Gdk.Surface, autohide:bool) -> Gdk.Surface
        new_toplevel(display:Gdk.Display) -> Gdk.Surface

    Object GdkSurface

    Signals from GdkSurface:
      layout (gint, gint)
      render (CairoRegion) -> gboolean
      event (gpointer) -> gboolean
      enter-monitor (GdkMonitor)
      leave-monitor (GdkMonitor)

    Properties from GdkSurface:
      cursor -> GdkCursor: cursor
      display -> GdkDisplay: display
      frame-clock -> GdkFrameClock: frame-clock
      mapped -> gboolean: mapped
      width -> gint: width
      height -> gint: height
      scale-factor -> gint: scale-factor
      scale -> gdouble: scale

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        cursor: Cursor | None
        display: Display
        frame_clock: FrameClock
        height: int
        mapped: bool
        scale: float
        scale_factor: int
        width: int

    @property
    def props(self) -> Props: ...
    def __init__(
        self,
        *,
        cursor: Cursor | None = ...,
        display: Display = ...,
        frame_clock: FrameClock = ...,
    ) -> None: ...
    def beep(self) -> None: ...
    def create_cairo_context(self) -> CairoContext: ...
    def create_gl_context(self) -> GLContext: ...
    def create_similar_surface(
        self, content: cairo.Content, width: int, height: int
    ) -> cairo.Surface: ...
    def create_vulkan_context(self) -> VulkanContext: ...
    def destroy(self) -> None: ...
    def get_cursor(self) -> Cursor | None: ...
    def get_device_cursor(self, device: Device) -> Cursor | None: ...
    def get_device_position(
        self, device: Device
    ) -> tuple[bool, float, float, ModifierType]: ...
    def get_display(self) -> Display: ...
    def get_frame_clock(self) -> FrameClock: ...
    def get_height(self) -> int: ...
    def get_mapped(self) -> bool: ...
    def get_scale(self) -> float: ...
    def get_scale_factor(self) -> int: ...
    def get_width(self) -> int: ...
    def hide(self) -> None: ...
    def is_destroyed(self) -> bool: ...
    @classmethod
    def new_popup(cls, parent: Surface, autohide: bool) -> Surface: ...
    @classmethod
    def new_toplevel(cls, display: Display) -> Surface: ...
    def queue_render(self) -> None: ...
    def request_layout(self) -> None: ...
    def set_cursor(self, cursor: Cursor | None = None) -> None: ...
    def set_device_cursor(self, device: Device, cursor: Cursor) -> None: ...
    def set_input_region(self, region: cairo.Region | None = None) -> None: ...
    def set_opaque_region(self, region: cairo.Region | None = None) -> None: ...
    def translate_coordinates(self, to: Surface) -> tuple[bool, float, float]: ...

class SurfaceClass(GObject.GPointer): ...

class Texture(GObject.Object, Paintable, Gio.Icon, Gio.LoadableIcon):
    """
    :Constructors:

    ::

        Texture(**properties)
        new_for_pixbuf(pixbuf:GdkPixbuf.Pixbuf) -> Gdk.Texture
        new_from_bytes(bytes:GLib.Bytes) -> Gdk.Texture
        new_from_file(file:Gio.File) -> Gdk.Texture
        new_from_filename(path:str) -> Gdk.Texture
        new_from_resource(resource_path:str) -> Gdk.Texture

    Object GdkTexture

    Properties from GdkTexture:
      width -> gint: width
      height -> gint: height
      color-state -> GdkColorState: color-state

    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()

    Signals from GObject:
      notify (GParam)
    """
    class Props(GObject.Object.Props):
        color_state: ColorState
        height: int
        width: int

    @property
    def props(self) -> Props: ...
    def __init__(
        self, *, color_state: ColorState = ..., height: int = ..., width: int = ...
    ) -> None: ...
    def download(self, data: Sequence[int], stride: int) -> None: ...
    def get_color_state(self) -> ColorState: ...
    def get_format(self) -> MemoryFormat: ...
    def get_height(self) -> int: ...
    def get_width(self) -> int: ...
    @classmethod
    def new_for_pixbuf(cls, pixbuf: GdkPixbuf.Pixbuf) -> Texture: ...
    @classmethod
    def new_from_bytes(cls, bytes: GLib.Bytes) -> Texture: ...
    @classmethod
    def new_from_file(cls, file: Gio.File) -> Texture: ...
    @classmethod
    def new_from_filename(cls, path: str) -> Texture: ...
    @classmethod
    def new_from_resource(cls, resource_path: str) -> Texture: ...
    def save_to_png(self, filename: str) -> bool: ...
    def save_to_png_bytes(self) -> GLib.Bytes: ...
    def save_to_tiff(self, filename: str) -> bool: ...
    def save_to_tiff_bytes(self) -> GLib.Bytes: ...

class TextureClass(GObject.GPointer): ...

class TextureDownloader(GObject.GBoxed):
    """
    :Constructors:

    ::

        new(texture:Gdk.Texture) -> Gdk.TextureDownloader
    """
    @staticmethod
    def __new__(cls: type[Self], texture: Texture) -> Self: ...
    def copy(self) -> TextureDownloader: ...
    def download_bytes(self) -> tuple[GLib.Bytes, int]: ...
    def download_bytes_with_planes(self) -> tuple[GLib.Bytes, list[int], list[int]]: ...
    def download_into(self, data: Sequence[int], stride: int) -> None: ...
    def free(self) -> None: ...
    def get_color_state(self) -> ColorState: ...
    def get_format(self) -> MemoryFormat: ...
    def get_texture(self) -> Texture: ...
    @classmethod
    def new(cls, texture: Texture) -> TextureDownloader: ...
    def set_color_state(self, color_state: ColorState) -> None: ...
    def set_format(self, format: MemoryFormat) -> None: ...
    def set_texture(self, texture: Texture) -> None: ...

class TimeCoord(GObject.GPointer):
    """
    :Constructors:

    ::

        TimeCoord()
    """

    time: int
    flags: AxisFlags
    axes: list[float]

class Toplevel(GObject.GInterface):
    """
    Interface GdkToplevel

    Signals from GObject:
      notify (GParam)
    """
    def begin_move(
        self, device: Device, button: int, x: float, y: float, timestamp: int
    ) -> None: ...
    def begin_resize(
        self,
        edge: SurfaceEdge,
        device: Device | None,
        button: int,
        x: float,
        y: float,
        timestamp: int,
    ) -> None: ...
    def focus(self, timestamp: int) -> None: ...
    def get_capabilities(self) -> ToplevelCapabilities: ...
    def get_gravity(self) -> Gravity: ...
    def get_state(self) -> ToplevelState: ...
    def inhibit_system_shortcuts(self, event: Event | None = None) -> None: ...
    def lower(self) -> bool: ...
    def minimize(self) -> bool: ...
    def present(self, layout: ToplevelLayout) -> None: ...
    def restore_system_shortcuts(self) -> None: ...
    def set_decorated(self, decorated: bool) -> None: ...
    def set_deletable(self, deletable: bool) -> None: ...
    def set_gravity(self, gravity: Gravity) -> None: ...
    def set_icon_list(self, surfaces: list[Texture]) -> None: ...
    def set_modal(self, modal: bool) -> None: ...
    def set_startup_id(self, startup_id: str) -> None: ...
    def set_title(self, title: str) -> None: ...
    def set_transient_for(self, parent: Surface) -> None: ...
    def show_window_menu(self, event: Event) -> bool: ...
    def supports_edge_constraints(self) -> bool: ...
    def titlebar_gesture(self, gesture: TitlebarGesture) -> bool: ...

class ToplevelInterface(GObject.GPointer): ...

class ToplevelLayout(GObject.GBoxed):
    """
    :Constructors:

    ::

        new() -> Gdk.ToplevelLayout
    """
    @staticmethod
    def __new__(cls: type[Self]) -> Self: ...
    def copy(self) -> ToplevelLayout: ...
    def equal(self, other: ToplevelLayout) -> bool: ...
    def get_fullscreen(self) -> tuple[bool, bool]: ...
    def get_fullscreen_monitor(self) -> Monitor | None: ...
    def get_maximized(self) -> tuple[bool, bool]: ...
    def get_resizable(self) -> bool: ...
    @classmethod
    def new(cls) -> ToplevelLayout: ...
    def ref(self) -> ToplevelLayout: ...
    def set_fullscreen(
        self, fullscreen: bool, monitor: Monitor | None = None
    ) -> None: ...
    def set_maximized(self, maximized: bool) -> None: ...
    def set_resizable(self, resizable: bool) -> None: ...
    def unref(self) -> None: ...

class ToplevelSize(GObject.GPointer):
    def get_bounds(self) -> tuple[int, int]: ...
    def set_min_size(self, min_width: int, min_height: int) -> None: ...
    def set_shadow_width(
        self, left: int, right: int, top: int, bottom: int
    ) -> None: ...
    def set_size(self, width: int, height: int) -> None: ...

class TouchEvent(Event):
    """
    :Constructors:

    ::

        TouchEvent(**properties)
    """
    def get_emulating_pointer(self) -> bool: ...

class TouchpadEvent(Event):
    """
    :Constructors:

    ::

        TouchpadEvent(**properties)
    """
    def get_deltas(self) -> tuple[float, float]: ...
    def get_gesture_phase(self) -> TouchpadGesturePhase: ...
    def get_n_fingers(self) -> int: ...
    def get_pinch_angle_delta(self) -> float: ...
    def get_pinch_scale(self) -> float: ...

class VulkanContext(DrawContext):
    """
    :Constructors:

    ::

        VulkanContext(**properties)

    Object GdkVulkanContext

    Signals from GdkVulkanContext:
      images-updated ()

    Properties from GdkDrawContext:
      display -> GdkDisplay: display
      surface -> GdkSurface: surface

    Signals from GObject:
      notify (GParam)
    """
    class Props(DrawContext.Props):
        display: Display | None
        surface: Surface | None

    @property
    def props(self) -> Props: ...
    def __init__(self, *, display: Display = ..., surface: Surface = ...) -> None: ...

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
    DELTA_X = 8
    DELTA_Y = 16
    DISTANCE = 512
    PRESSURE = 32
    ROTATION = 1024
    SLIDER = 2048
    WHEEL = 256
    X = 2
    XTILT = 64
    Y = 4
    YTILT = 128

class DragAction(GObject.GFlags):
    ASK = 8
    COPY = 1
    LINK = 4
    MOVE = 2
    NONE = 0
    @staticmethod
    def is_unique(action: DragAction) -> bool: ...

class FrameClockPhase(GObject.GFlags):
    AFTER_PAINT = 64
    BEFORE_PAINT = 2
    FLUSH_EVENTS = 1
    LAYOUT = 8
    NONE = 0
    PAINT = 16
    RESUME_EVENTS = 32
    UPDATE = 4

class GLAPI(GObject.GFlags):
    GL = 1
    GLES = 2

class ModifierType(GObject.GFlags):
    ALT_MASK = 8
    BUTTON1_MASK = 256
    BUTTON2_MASK = 512
    BUTTON3_MASK = 1024
    BUTTON4_MASK = 2048
    BUTTON5_MASK = 4096
    CONTROL_MASK = 4
    HYPER_MASK = 134217728
    LOCK_MASK = 2
    META_MASK = 268435456
    NO_MODIFIER_MASK = 0
    SHIFT_MASK = 1
    SUPER_MASK = 67108864

class PaintableFlags(GObject.GFlags):
    CONTENTS = 2
    SIZE = 1
    STATIC_CONTENTS = 2
    STATIC_SIZE = 1

class SeatCapabilities(GObject.GFlags):
    ALL = 31
    ALL_POINTING = 7
    KEYBOARD = 8
    NONE = 0
    POINTER = 1
    TABLET_PAD = 16
    TABLET_STYLUS = 4
    TOUCH = 2

class ToplevelCapabilities(GObject.GFlags):
    EDGE_CONSTRAINTS = 1
    FULLSCREEN = 32
    INHIBIT_SHORTCUTS = 2
    LOWER = 128
    MAXIMIZE = 16
    MINIMIZE = 64
    TITLEBAR_GESTURES = 4
    WINDOW_MENU = 8

class ToplevelState(GObject.GFlags):
    ABOVE = 16
    BELOW = 32
    BOTTOM_RESIZABLE = 8192
    BOTTOM_TILED = 4096
    FOCUSED = 64
    FULLSCREEN = 8
    LEFT_RESIZABLE = 32768
    LEFT_TILED = 16384
    MAXIMIZED = 2
    MINIMIZED = 1
    RIGHT_RESIZABLE = 2048
    RIGHT_TILED = 1024
    STICKY = 4
    SUSPENDED = 65536
    TILED = 128
    TOP_RESIZABLE = 512
    TOP_TILED = 256

class AxisUse(GObject.GEnum):
    DELTA_X = 3
    DELTA_Y = 4
    DISTANCE = 9
    IGNORE = 0
    LAST = 12
    PRESSURE = 5
    ROTATION = 10
    SLIDER = 11
    WHEEL = 8
    X = 1
    XTILT = 6
    Y = 2
    YTILT = 7

class CicpRange(GObject.GEnum):
    FULL = 1
    NARROW = 0

class ColorChannel(GObject.GEnum):
    ALPHA = 3
    BLUE = 2
    GREEN = 1
    RED = 0

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

class DmabufError(GObject.GEnum):
    CREATION_FAILED = 2
    NOT_AVAILABLE = 0
    UNSUPPORTED_FORMAT = 1
    @staticmethod
    def quark() -> int: ...

class DragCancelReason(GObject.GEnum):
    ERROR = 2
    NO_TARGET = 0
    USER_CANCELLED = 1

class EventType(GObject.GEnum):
    BUTTON_PRESS = 2
    BUTTON_RELEASE = 3
    DELETE = 0
    DRAG_ENTER = 11
    DRAG_LEAVE = 12
    DRAG_MOTION = 13
    DROP_START = 14
    ENTER_NOTIFY = 6
    EVENT_LAST = 30
    FOCUS_CHANGE = 8
    GRAB_BROKEN = 16
    KEY_PRESS = 4
    KEY_RELEASE = 5
    LEAVE_NOTIFY = 7
    MOTION_NOTIFY = 1
    PAD_BUTTON_PRESS = 23
    PAD_BUTTON_RELEASE = 24
    PAD_DIAL = 29
    PAD_GROUP_MODE = 27
    PAD_RING = 25
    PAD_STRIP = 26
    PROXIMITY_IN = 9
    PROXIMITY_OUT = 10
    SCROLL = 15
    TOUCHPAD_HOLD = 28
    TOUCHPAD_PINCH = 22
    TOUCHPAD_SWIPE = 21
    TOUCH_BEGIN = 17
    TOUCH_CANCEL = 20
    TOUCH_END = 19
    TOUCH_UPDATE = 18

class FullscreenMode(GObject.GEnum):
    ALL_MONITORS = 1
    CURRENT_MONITOR = 0

class GLError(GObject.GEnum):
    COMPILATION_FAILED = 3
    LINK_FAILED = 4
    NOT_AVAILABLE = 0
    UNSUPPORTED_FORMAT = 1
    UNSUPPORTED_PROFILE = 2
    @staticmethod
    def quark() -> int: ...

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

class InputSource(GObject.GEnum):
    KEYBOARD = 2
    MOUSE = 0
    PEN = 1
    TABLET_PAD = 6
    TOUCHPAD = 4
    TOUCHSCREEN = 3
    TRACKPOINT = 5

class KeyMatch(GObject.GEnum):
    EXACT = 2
    NONE = 0
    PARTIAL = 1

class MemoryFormat(GObject.GEnum):
    A16 = 25
    A16_FLOAT = 26
    A32_FLOAT = 27
    A8 = 24
    A8B8G8R8 = 6
    A8B8G8R8_PREMULTIPLIED = 28
    A8R8G8B8 = 4
    A8R8G8B8_PREMULTIPLIED = 1
    B8G8R8 = 8
    B8G8R8A8 = 3
    B8G8R8A8_PREMULTIPLIED = 0
    B8G8R8G8_422 = 55
    B8G8R8X8 = 29
    G10X6_B10X6R10X6_420 = 39
    G12X4_B12X4R12X4_420 = 40
    G16 = 23
    G16A16 = 22
    G16A16_PREMULTIPLIED = 21
    G16_B16R16_420 = 41
    G16_B16_R16_420 = 62
    G16_B16_R16_422 = 63
    G16_B16_R16_444 = 64
    G8 = 20
    G8A8 = 19
    G8A8_PREMULTIPLIED = 18
    G8B8G8R8_422 = 52
    G8R8G8B8_422 = 53
    G8_B8R8_420 = 33
    G8_B8R8_422 = 35
    G8_B8R8_444 = 37
    G8_B8_R8_410 = 42
    G8_B8_R8_411 = 44
    G8_B8_R8_420 = 46
    G8_B8_R8_422 = 48
    G8_B8_R8_444 = 50
    G8_R8B8_420 = 34
    G8_R8B8_422 = 36
    G8_R8B8_444 = 38
    G8_R8_B8_410 = 43
    G8_R8_B8_411 = 45
    G8_R8_B8_420 = 47
    G8_R8_B8_422 = 49
    G8_R8_B8_444 = 51
    N_FORMATS = 65
    R16G16B16 = 9
    R16G16B16A16 = 11
    R16G16B16A16_FLOAT = 14
    R16G16B16A16_FLOAT_PREMULTIPLIED = 13
    R16G16B16A16_PREMULTIPLIED = 10
    R16G16B16_FLOAT = 12
    R32G32B32A32_FLOAT = 17
    R32G32B32A32_FLOAT_PREMULTIPLIED = 16
    R32G32B32_FLOAT = 15
    R8G8B8 = 7
    R8G8B8A8 = 5
    R8G8B8A8_PREMULTIPLIED = 2
    R8G8B8G8_422 = 54
    R8G8B8X8 = 31
    X4G12_X4B12_X4R12_420 = 59
    X4G12_X4B12_X4R12_422 = 60
    X4G12_X4B12_X4R12_444 = 61
    X6G10_X6B10_X6R10_420 = 56
    X6G10_X6B10_X6R10_422 = 57
    X6G10_X6B10_X6R10_444 = 58
    X8B8G8R8 = 32
    X8R8G8B8 = 30

class NotifyType(GObject.GEnum):
    ANCESTOR = 0
    INFERIOR = 2
    NONLINEAR = 3
    NONLINEAR_VIRTUAL = 4
    UNKNOWN = 5
    VIRTUAL = 1

class ScrollDirection(GObject.GEnum):
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    SMOOTH = 4
    UP = 0

class ScrollRelativeDirection(GObject.GEnum):
    IDENTICAL = 0
    INVERTED = 1
    UNKNOWN = 2

class ScrollUnit(GObject.GEnum):
    SURFACE = 1
    WHEEL = 0

class SubpixelLayout(GObject.GEnum):
    HORIZONTAL_BGR = 3
    HORIZONTAL_RGB = 2
    NONE = 1
    UNKNOWN = 0
    VERTICAL_BGR = 5
    VERTICAL_RGB = 4

class SurfaceEdge(GObject.GEnum):
    EAST = 4
    NORTH = 1
    NORTH_EAST = 2
    NORTH_WEST = 0
    SOUTH = 6
    SOUTH_EAST = 7
    SOUTH_WEST = 5
    WEST = 3

class TextureError(GObject.GEnum):
    CORRUPT_IMAGE = 1
    TOO_LARGE = 0
    UNSUPPORTED_CONTENT = 2
    UNSUPPORTED_FORMAT = 3
    @staticmethod
    def quark() -> int: ...

class TitlebarGesture(GObject.GEnum):
    DOUBLE_CLICK = 1
    MIDDLE_CLICK = 3
    RIGHT_CLICK = 2

class TouchpadGesturePhase(GObject.GEnum):
    BEGIN = 0
    CANCEL = 3
    END = 2
    UPDATE = 1

class VulkanError(GObject.GEnum):
    NOT_AVAILABLE = 1
    UNSUPPORTED = 0
    @staticmethod
    def quark() -> int: ...
