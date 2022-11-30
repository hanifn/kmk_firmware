from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.hid import HIDModes
from kmk.handlers.sequences import send_string
import supervisor
from kmk.extensions.peg_oled_display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.extensions.peg_rgb_matrix import Rgb_matrix
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.capsword import CapsWord
from kmk.modules.combos import Combos, Chord
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

modtap = ModTap()
modtap.prefer_hold = False
modtap.tap_time = 200
keyboard.modules.append(modtap)

layers_ext = Layers()
layers_ext.prefer_hold = False
layers_ext.tap_time = 200
keyboard.modules.append(layers_ext)

caps_word = CapsWord()
keyboard.modules.append(caps_word)

combos = Combos()
keyboard.modules.append(combos)

mouse_keys = MouseKeys()
keyboard.modules.append(mouse_keys)

media_keys = MediaKeys()
keyboard.modules.append(media_keys)

# oled
oled_ext = Oled( OledData(image={0:OledReactionType.LAYER,1:["1.bmp","2.bmp","3.bmp","4.bmp","5.bmp","6.bmp","7.bmp","8.bmp"]}),toDisplay=OledDisplayMode.IMG,flip=False)
# oled
keyboard.extensions.append(oled_ext)
# ledmap
rgb_ext = Rgb_matrix(ledDisplay=[[85,0,255],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[85,0,255],[85,0,255],[0,255,234],[0,255,234],[0,255,234],[0,255,234],[85,0,255]],split=True,rightSide=False,disable_auto_write=True)
# ledmap
keyboard.extensions.append(rgb_ext)
# TODO Comment one of these on each side
#split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT
split = Split(data_pin=keyboard.rx, data_pin2=keyboard.tx, uart_flip=False)
keyboard.modules.append(split)
# encodercount
# 2
# encodercount

# homerow modifiers
MOD_A = KC.MT(KC.A, KC.LGUI)
MOD_S = KC.MT(KC.S, KC.LALT)
MOD_D = KC.MT(KC.D, KC.LCTL)
MOD_F = KC.MT(KC.F, KC.LSFT)
MOD_J = KC.MT(KC.J, KC.RSFT)
MOD_K = KC.MT(KC.K, KC.RCTL)
MOD_L = KC.MT(KC.L, KC.RALT)
MOD_SCLN = KC.MT(KC.SCOLON, KC.RGUI)

# shortcuts
REDO = KC.LSFT(KC.LGUI(KC.Z))
PASTE = KC.LGUI(KC.V)
COPY = KC.LGUI(KC.C)
CUT = KC.LGUI(KC.X)
UNDO = KC.LGUI(KC.Z)
ALFRED = KC.LCTL(KC.SPACE)

# layer keys
QWERTY = 0
NAVI = 1
MOUSE = 2
MEDIA = 3
NUMBER = 4
SYMBOL = 5
FUNCTION = 6
GAMING = 7

LAY_NAV_SPC = KC.LT(NAVI, KC.SPACE)
LAY_MOUS_TAB = KC.LT(MOUSE, KC.TAB)
LAY_MEDIA_ESC = KC.LT(MEDIA, KC.ESCAPE)
LAY_NUM_BSPC = KC.LT(NUMBER, KC.BSPC)
LAY_SYM_ENT = KC.LT(SYMBOL, KC.ENTER)
LAY_FUN_DEL = KC.LT(FUNCTION, KC.DEL)

LAY_TGL_GAM = KC.TG(GAMING)

# combos
combos.combos = [
	Chord((KC.F, KC.J), KC.CW) # capsword on F + J
]

# keymap
keyboard.keymap = [ 
	[ # QWERTY layer
		KC.EQUAL,	KC.N1,	KC.N2,	KC.N3,	KC.N4,	KC.N5,									KC.N6,	KC.N7,	KC.N8,		KC.N9,	KC.N0,		KC.MINUS,
		KC.GRAVE,	KC.Q,	KC.W,	KC.E,	KC.R,	KC.T,									KC.Y,	KC.U,	KC.I,		KC.O,	KC.P,		KC.BSLASH,
		KC.LCTRL,	MOD_A,	MOD_S,	MOD_D,	MOD_F,	KC.G,									KC.H,	MOD_J,	MOD_K,		MOD_L,	MOD_SCLN,	KC.QUOTE,
		KC.LSHIFT,	KC.Z,	KC.X,	KC.C,	KC.V,	KC.B,	ALFRED,			LAY_TGL_GAM,	KC.N,	KC.M,	KC.COMMA,	KC.DOT,	KC.SLASH,	KC.RSHIFT,
				KC.LBRC,	LAY_MEDIA_ESC,	LAY_NAV_SPC,	LAY_MOUS_TAB,	LAY_SYM_ENT,	LAY_NUM_BSPC,	LAY_FUN_DEL,	KC.RBRC,
				# Rotary encoders
				KC.AUDIO_VOL_UP,	KC.AUDIO_VOL_DOWN,	KC.MEDIA_PREV_TRACK,	KC.MEDIA_NEXT_TRACK
	], 
	[ # Navigation layer
		KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,						KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,
		KC.NO,		KC.NO,		KC.NO,		KC.NO,		KC.NO,		KC.NO,							REDO,		PASTE,		COPY,		CUT,		UNDO,		KC.NO,
		KC.NO,		KC.LGUI,	KC.LALT,	KC.LCTL,	KC.LSFT,	KC.NO,							KC.LEFT,	KC.DOWN,	KC.UP,		KC.RIGHT,	KC.CW,		KC.NO,
		KC.NO,		KC.NO,		KC.RALT,	KC.NO,		KC.NO,		KC.NO,	KC.TRNS,	KC.TRNS,	KC.HOME,	KC.PGDN,	KC.PGUP,	KC.END,		KC.INS,		KC.NO,
												KC.NO,   KC.NO,   KC.NO,	KC.RESET,	KC.ENTER,	KC.BSPC,	KC.DEL,		KC.NO,
				# Rotary encoders
				KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS
	], 
	[ # Mouse layer
		KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,					KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,
		KC.NO,		KC.NO,		KC.NO,		KC.NO,		KC.NO,		KC.NO,						REDO,		PASTE,		COPY,		CUT,		UNDO,		KC.NO,
		KC.NO,		KC.LGUI,	KC.LALT,	KC.LCTL,	KC.LSFT,	KC.NO,						KC.MS_LT,	KC.MS_DN,	KC.MS_UP,	KC.MS_RT,	KC.NO,		KC.NO,
		KC.NO,		KC.NO,		KC.RALT,	KC.NO,		KC.NO,		KC.NO,	KC.TRNS,	KC.TRNS,	KC.NO,		KC.MW_DN,	KC.MW_UP,	KC.NO,		KC.NO,		KC.NO,
													KC.NO,	KC.NO,	KC.NO,	KC.NO,		KC.MB_RMB,	KC.MB_LMB,	KC.MB_MMB,		KC.NO,
				# Rotary encoders
				KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS
	], 
	[ # Media layer
		KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,				KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,
		KC.NO,		KC.NO,		KC.NO,		KC.NO,		KC.NO,		KC.NO,					KC.NO,		KC.RGB_BRD,	KC.RGB_BRI,	KC.RGB_TOG,	KC.NO,		KC.NO,
		KC.NO,		KC.LGUI,	KC.LALT,	KC.LCTL,	KC.LSFT,	KC.NO,					KC.MRWD,	KC.VOLD,	KC.VOLU,	KC.MFFD,	KC.NO,		KC.NO,
		KC.NO,		KC.NO,		KC.RALT,	KC.NO,		KC.NO,		KC.NO,	KC.NO,	KC.NO,	KC.NO,		KC.NO,	 	KC.NO,		KC.NO,		KC.NO,		KC.NO,
													KC.NO,	KC.NO,	KC.NO,	KC.NO,	KC.MSTP,	KC.MPLY,	KC.MUTE,		KC.NO,
				# Rotary encoders
				KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS
	], 
	[ # Number layer
		KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,						KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,
		KC.NO,		KC.LPRN,	KC.KP_7,	KC.KP_8,	KC.KP_9,	KC.RPRN,						KC.NO,		KC.NO,		KC.NO,		KC.NO,		KC.NO,		KC.NO,
		KC.NO,		KC.SCLN,	KC.KP_4,	KC.KP_5,	KC.KP_6,	KC.KP_EQUAL,					KC.NO,		KC.LSFT,	KC.LCTL,	KC.LALT,	KC.LGUI,		KC.NO,
		KC.NO,		KC.GRAVE,	KC.KP_1,	KC.KP_2,	KC.KP_3,	KC.KP_SLASH,	KC.NO,	KC.NO,	KC.NO,		KC.NO,	 	KC.NO,		KC.RALT,		KC.NO,		KC.NO,
													KC.NO,	KC.PDOT,	KC.KP_0,  KC.PMNS,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
				# Rotary encoders
				KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS
	], 
	[ # Symbol layer
		KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,					KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,
		KC.NO,		KC.LCBR,	KC.AMPR,	KC.ASTR,	KC.LPRN,	KC.RCBR,					KC.NO,		KC.NO,		KC.NO,		KC.NO,		KC.NO,		KC.NO,
		KC.NO,		KC.COLON,	KC.DLR,		KC.PERC,	KC.CIRC,	KC.KP_PLUS,					KC.NO,		KC.LSFT,	KC.LCTL,	KC.LALT,	KC.LGUI,	KC.NO,
		KC.NO,		KC.TILDE,	KC.EXLM,	KC.AT,		KC.HASH,	KC.PIPE,	KC.NO,	KC.NO,	KC.NO,		KC.NO,	 	KC.NO,		KC.RALT,	KC.NO,		KC.NO,
												KC.NO,	KC.LPRN,	KC.RPRN,  KC.UNDS,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
				# Rotary encoders
				KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS
	], 
	[ # Function layer
		KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,					KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS,
		KC.NO,		KC.F12,		KC.F7,		KC.F8,		KC.F9,		KC.PSCR,					KC.NO,		KC.NO,		KC.NO,		KC.NO,		KC.NO,		KC.NO,
		KC.NO,		KC.F11,		KC.F4,		KC.F5,		KC.F6,		KC.SLCK,					KC.NO,		KC.LSFT,	KC.LCTL,	KC.LALT,	KC.LGUI,	KC.NO,
		KC.NO,		KC.F10,		KC.F1,		KC.F2,		KC.F3,		KC.PAUSE,	KC.NO,	KC.NO,	KC.NO,		KC.NO,	 	KC.NO,		KC.RALT,	KC.NO,		KC.NO,
												KC.NO,	KC.APP,		KC.SPACE,  KC.TAB,	KC.NO,	KC.NO,	KC.NO,	KC.NO,
				# Rotary encoders
				KC.TRNS,	KC.TRNS,	KC.TRNS,	KC.TRNS
	], 
	[ # Gaming layer
		KC.EQUAL,	KC.N1,	KC.N2,	KC.N3,	KC.N4,	KC.N5,									KC.N6,	KC.N7,	KC.N8,		KC.N9,	KC.N0,		KC.MINUS,
		KC.GRAVE,	KC.Q,	KC.W,	KC.E,	KC.R,	KC.T,									KC.Y,	KC.U,	KC.I,		KC.O,	KC.P,		KC.BSLASH,
		KC.LCTRL,	KC.A,	KC.S,	KC.D,	KC.F,	KC.G,									KC.H,	MOD_J,	MOD_K,		MOD_L,	MOD_SCLN,	KC.QUOTE,
		KC.LSHIFT,	KC.Z,	KC.X,	KC.C,	KC.V,	KC.B,	KC.LBRACKET,	LAY_TGL_GAM,	KC.N,	KC.M,	KC.COMMA,	KC.DOT,	KC.SLASH,	KC.RSHIFT,
				KC.LALT,	LAY_MEDIA_ESC,	LAY_NAV_SPC,	LAY_MOUS_TAB,	LAY_SYM_ENT,	LAY_NUM_BSPC,	LAY_FUN_DEL,	KC.RGUI,
				# Rotary encoders
				KC.AUDIO_VOL_UP,	KC.AUDIO_VOL_DOWN,	KC.MEDIA_PREV_TRACK,	KC.MEDIA_NEXT_TRACK
	], 
]
# keymap

if __name__ == '__main__': 
    keyboard.go(hid_type=HIDModes.USB)