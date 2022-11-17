from aiogram import executor
import logging
from config import dp
from inline import *
from reply import *

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands='start')
async def start(msg: Message):
    img = open("image/kirish.png", "rb")
    await msg.answer_photo(img, f"<b>Assalomu alekum {msg.from_user.full_name}</b>\n"
                           f"<b>Mp3 botiga xush kelibsiz</b>\n"
                           f"Qo'shiq yoki qo'shiqchining nomini jo'nating, musiqani topib beraman!\n", parse_mode='html', reply_markup=menuKirish)

@dp.message_handler(text="Mp3")
async def mp3(msg: Message):
    await msg.answer(f"<b>Mp3</b>\n"
                     f"<b>Tanlang...</b>", parse_mode='html', reply_markup=InMp3)
    await msg.delete()

@dp.message_handler(text="Yordam")
async def yordam(msg: Message):
    await msg.answer(f"<b>Yordam kerak bo'lsa ushbu http://t.me/iammokhammed profilga murojaat qiling</b>", parse_mode='html', reply_markup=menuKirish)
    await msg.delete()

@dp.message_handler(text="Artist")
async def artistt(msg: Message):
    img = open("image/photo_2022-05-14_17-31-25.jpg", "rb")
    await msg.answer_photo(img, reply_markup=InArtist)

@dp.callback_query_handler(text="like")
async def like(call: CallbackQuery):
    await call.answer("Thank you 👍")

@dp.callback_query_handler(text="dis_like")
async def dis_like(call: CallbackQuery):
    await call.answer("Oh no 👎")

@dp.callback_query_handler(text="otmen")
async def otmen(call: CallbackQuery):
    await call.message.delete()

@dp.callback_query_handler(text="back_start")
async def back_start(call: CallbackQuery):
    await call.message.answer(f"<b>Back...</b>", parse_mode='html', reply_markup=menuKirish)
    await call.message.delete()
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="ummon")
async def ummon(call: CallbackQuery):
    await call.message.answer(textuzb1, reply_markup=InUmmon)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="benom")
async def benom(call: CallbackQuery):
    await call.message.answer(textuzb2, reply_markup=InBenom)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="yulduz_usmonova")
async def yulduz(call: CallbackQuery):
    await call.message.answer(textuzb3, reply_markup=InYulduz)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="mband")
async def mband(call: CallbackQuery):
    await call.message.answer(textrus1, reply_markup=InMband)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="jony")
async def jony(call: CallbackQuery):
    await call.message.answer(textrus2, reply_markup=InJony)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="blackstar")
async def blackstar(call: CallbackQuery):
    await call.message.answer(textrus3, reply_markup=InBlackstart)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="billie_eilish")
async def billie_eilish(call: CallbackQuery):
    await call.message.answer(textzarubej1, reply_markup=InBillie)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="tentaction")
async def tentaction(call: CallbackQuery):
    await call.message.answer(textzarubej2, reply_markup=InTentaction)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="michel_jakson")
async def michel_jakson(call: CallbackQuery):
    await call.message.answer(textzarubej3, reply_markup=InMichel)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="uzb")
async def uzb(call: CallbackQuery):
    await call.message.answer(textuzb1, reply_markup=InUmmon)
    await call.message.delete()
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="yulduzga")
async def uzb1(call: CallbackQuery):
    await call.message.answer(textuzb3, reply_markup=InYulduz)
    await call.message.delete()
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="benomga")
async def uzb2(call: CallbackQuery):
    await call.message.answer(textuzb2, reply_markup=InBenom)
    await call.message.delete()
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="ochirish")
async def ochirish(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"<b>Mp3...........</b>", parse_mode='html', reply_markup=InMp3)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="rus")
async def rus(call: CallbackQuery):
    await call.message.answer(textrus1, reply_markup=InMband)
    await call.message.delete()
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="jonyga")
async def rus1(call: CallbackQuery):
    await call.message.answer(textrus2, reply_markup=InJony)
    await call.message.delete()
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="blackstarga")
async def rus2(call: CallbackQuery):
    await call.message.answer(textrus3, reply_markup=InBlackstart)
    await call.message.delete()
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="zarubej")
async def zarubej(call: CallbackQuery):
    await call.message.answer(textzarubej1, reply_markup=InBillie)
    await call.message.delete()
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="tentactionga")
async def zarubej1(call: CallbackQuery):
    await call.message.answer(textzarubej2, reply_markup=InTentaction)
    await call.message.delete()
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="michelga")
async def zarubej2(call: CallbackQuery):
    await call.message.answer(textzarubej3, reply_markup=InMichel)
    await call.message.delete()
    await call.answer(cache_time=30, show_alert=True)

#ummon
@dp.message_handler(text="Ummon")
async def ummon(msg: Message):
    await msg.answer(textuzb1, reply_markup=InUmmon)

@dp.callback_query_handler(text="1ummon")
async def ummon1(call: CallbackQuery):
    await call.message.answer_audio(open("ummon/2_5312353501194491752.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="2ummon")
async def ummon2(call: CallbackQuery):
    await call.message.answer_audio(open("ummon/2_5458449961978958820.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="3ummon")
async def ummon3(call: CallbackQuery):
    await call.message.answer_audio(open("ummon/562. Ummon guruhi - Oq gulim (Bestmedia.Uz).mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="4ummon")
async def ummon4(call: CallbackQuery):
    await call.message.answer_audio(open("ummon/Qaydasan gulim        Ummon.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="5ummon")
async def ummon5(call: CallbackQuery):
    await call.message.answer_audio(open("ummon/Sokin Tun   Ummon Guruhi.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="6ummon")
async def ummon6(call: CallbackQuery):
    await call.message.answer_audio(open("ummon/Ummon – Ana endi Yig'la (www.Xorazm.Net).mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="7ummon")
async def ummon7(call: CallbackQuery):
    await call.message.answer_audio(open("ummon/Ummon_-_Dengiz_Zamonaviy.com.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="8ummon")
async def ummon8(call: CallbackQuery):
    await call.message.answer_audio(open("ummon/Xamdam_Sobirov_va_Shoxrux_(Ummon)_So_ngi_Marta_-_RtUV874Kpks.m4a", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="9ummon")
async def ummon9(call: CallbackQuery):
    await call.message.answer_audio(open("ummon/shohrux_ummon_do_st_94.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="10ummon")
async def ummon10(call: CallbackQuery):
    await call.message.answer_audio(open("ummon/Ummon_-_Dengiz_Zamonaviy.com.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

#benom
@dp.message_handler(text="Benom")
async def benom(msg: Message):
    await msg.answer(textuzb2, reply_markup=InBenom)

@dp.callback_query_handler(text="1benom")
async def benom1(call: CallbackQuery):
    await call.message.answer_audio(open("benom/2_5215721482973353846.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="2benom")
async def benom2(call: CallbackQuery):
    await call.message.answer_audio(open("benom/2_5285317291951525874.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="3benom")
async def benom3(call: CallbackQuery):
    await call.message.answer_audio(open("benom/Balki Tun (OST Salom Sevgi)    Benom.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="4benom")
async def benom4(call: CallbackQuery):
    await call.message.answer_audio(open("benom/Benom.Guruhi-Eslamading.www.Daxshat.Uz.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="5benom")
async def benom5(call: CallbackQuery):
    await call.message.answer_audio(open("benom/Benom_guruhi_Sen_baxtli_bo'l_cover_by_Hilola_Gayratova_&_RE_M_&.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="6benom")
async def benom6(call: CallbackQuery):
    await call.message.answer_audio(open("benom/Benom_guruhi__Parcha(@TaronaM_Uz).mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="7benom")
async def benom7(call: CallbackQuery):
    await call.message.answer_audio(open("benom/Gulim .mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="8benom")
async def benom8(call: CallbackQuery):
    await call.message.answer_audio(open("benom/uzxitnet_675089552.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="9benom")
async def benom9(call: CallbackQuery):
    await call.message.answer_audio(open("benom/Yog adi yomg ir (zaycev.net)   Benom Guruhi.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="10benom")
async def benom10(call: CallbackQuery):
    await call.message.answer_audio(open("benom/Benom.Guruhi-Eslamading.www.Daxshat.Uz.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

#yulduz
@dp.message_handler(text="Yulduz")
async def yulduz(msg: Message):
    await msg.answer(textuzb3, reply_markup=InYulduz)

@dp.callback_query_handler(text="1yulduz")
async def yulduz1(call: CallbackQuery):
    await call.message.answer_audio(open("yulduz/2_5212946848200791653.m4a", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="2yulduz")
async def yulduz2(call: CallbackQuery):
    await call.message.answer_audio(open("yulduz/4_5805620268823020668.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="3yulduz")
async def yulduz3(call: CallbackQuery):
    await call.message.answer_audio(open("yulduz/1662664166_yulduz-usmonova-sevgidan-toydim-man_(uzxit.net).mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="4yulduz")
async def yulduz4(call: CallbackQuery):
    await call.message.answer_audio(open("yulduz/j664fght3ohzeqnqxs.m4a", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="5yulduz")
async def yulduz5(call: CallbackQuery):
    await call.message.answer_audio(open("yulduz/julduz_usmanova_yulduz_usmonova_dadajon_yangi_kilp_2017_zf_fm.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="6yulduz")
async def yulduz6(call: CallbackQuery):
    await call.message.answer_audio(open("yulduz/KEL (2022).mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="7yulduz")
async def yulduz7(call: CallbackQuery):
    await call.message.answer_audio(open("yulduz/Muhabbat   Yulduz Usmonova.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="8yulduz")
async def yulduz8(call: CallbackQuery):
    await call.message.answer_audio(open("yulduz/yulduz-usmonova-nola-kunam-namesha-yor-biyo-2022.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="9yulduz")
async def yulduz9(call: CallbackQuery):
    await call.message.answer_audio(open("yulduz/Yulduz_Usmonova_Malik-Tojiki_medonet.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="10yulduz")
async def yulduz10(call: CallbackQuery):
    await call.message.answer_audio(open("yulduz/julduz_usmanova_yulduz_usmonova_dadajon_yangi_kilp_2017_zf_fm.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

#jony
@dp.message_handler(text="Jony")
async def jony(msg: Message):
    await msg.answer(textrus2, reply_markup=InJony)

@dp.callback_query_handler(text="1jony")
async def jony1(call: CallbackQuery):
    await call.message.answer_audio(open("jony/@Yuragimdagi_Suzlar_JONY_Rauf_Faik.m4a", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="2jony")
async def jony2(call: CallbackQuery):
    await call.message.answer_audio(open("jony/JONY - Пустота.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="3jony")
async def jony3(call: CallbackQuery):
    await call.message.answer_audio(open("jony/JONY,_HammAli_Наверно_ты_меня_не_помнишь_HammAli_Navai.m4a", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="4jony")
async def jony4(call: CallbackQuery):
    await call.message.answer_audio(open("jony/Lolipop .mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="5jony")
async def jony5(call: CallbackQuery):
    await call.message.answer_audio(open("jony/Титры.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="6jony")
async def jony6(call: CallbackQuery):
    await call.message.answer_audio(open("jony/Титры.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="7jony")
async def jony7(call: CallbackQuery):
    await call.message.answer_audio(open("jony/@Yuragimdagi_Suzlar_JONY_Rauf_Faik.m4a", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="8jony")
async def jony8(call: CallbackQuery):
    await call.message.answer_audio(open("jony/JONY - Пустота.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="9jony")
async def jony9(call: CallbackQuery):
    await call.message.answer_audio(open("jony/JONY,_HammAli_Наверно_ты_меня_не_помнишь_HammAli_Navai.m4a", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="10jony")
async def jony10(call: CallbackQuery):
    await call.message.answer_audio(open("jony/Lolipop .mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

#mband
@dp.message_handler(text="Mband")
async def mband(msg: Message):
    await msg.answer(textrus1, reply_markup=InMband)

@dp.callback_query_handler(text="1mband")
async def mband1(call: CallbackQuery):
    await call.message.answer_audio(open("mband/Mband – Всё исправить.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="2mband")
async def mband2(call: CallbackQuery):
    await call.message.answer_audio(open("mband/MBAND - Помедленнее (dodasi.com).mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="3mband")
async def mband3(call: CallbackQuery):
    await call.message.answer_audio(open("mband/MBAND – Она вернётся (оригинал).mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="4mband")
async def mband4(call: CallbackQuery):
    await call.message.answer_audio(open("mband/Посмотри на меня (EUROPA PLUS)   MBAND.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="5mband")
async def mband5(call: CallbackQuery):
    await call.message.answer_audio(open("mband/MBAND – Она вернётся (оригинал).mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="6mband")
async def mband6(call: CallbackQuery):
    await call.message.answer_audio(open("mband/Mband – Всё исправить.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="7mband")
async def mband7(call: CallbackQuery):
    await call.message.answer_audio(open("mband/MBAND – Она вернётся (оригинал).mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="8mband")
async def mband8(call: CallbackQuery):
    await call.message.answer_audio(open("mband/MBAND - Помедленнее (dodasi.com).mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="9mband")
async def mband9(call: CallbackQuery):
    await call.message.answer_audio(open("mband/Посмотри на меня (EUROPA PLUS)   MBAND.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="10mband")
async def mband10(call: CallbackQuery):
    await call.message.answer_audio(open("mband/MBAND – Она вернётся (оригинал).mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

#blackstar
@dp.message_handler(text="Blackstar")
async def black(msg: Message):
    await msg.answer(textrus3, reply_markup=InBlackstart)

@dp.callback_query_handler(text="1black")
async def black1(call: CallbackQuery):
    await call.message.answer_audio(open("blackstar/Blackstar (Instrumental) - Celldweller.m4a", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="2black")
async def black2(call: CallbackQuery):
    await call.message.answer_audio(open("blackstar/doc_2022-11-08_17-11-57.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="3black")
async def black3(call: CallbackQuery):
    await call.message.answer_audio(open("blackstar/Mannequins for the Beast   Blackstar Halo.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="4black")
async def black4(call: CallbackQuery):
    await call.message.answer_audio(open("blackstar/Octopizzo feat. Tracy  – BlackStar 2014.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="5black")
async def black5(call: CallbackQuery):
    await call.message.answer_audio(open("blackstar/Slw   blackstar.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="6black")
async def black6(call: CallbackQuery):
    await call.message.answer_audio(open("blackstar/Slw   blackstar.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="7black")
async def black7(call: CallbackQuery):
    await call.message.answer_audio(open("blackstar/Blackstar (Instrumental) - Celldweller.m4a", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="8black")
async def black8(call: CallbackQuery):
    await call.message.answer_audio(open("blackstar/doc_2022-11-08_17-11-57.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="9black")
async def black9(call: CallbackQuery):
    await call.message.answer_audio(open("blackstar/Mannequins for the Beast   Blackstar Halo.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="10black")
async def black10(call: CallbackQuery):
    await call.message.answer_audio(open("blackstar/Octopizzo feat. Tracy  – BlackStar 2014.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

#michel jekson
@dp.message_handler(text="Michel")
async def michel(msg: Message):
    await msg.answer(textzarubej3, reply_markup=InMichel)

@dp.callback_query_handler(text="1michel")
async def michel1(call: CallbackQuery):
    await call.message.answer_audio(open("michel/Michel Jakson – Black & White.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="2michel")
async def michel2(call: CallbackQuery):
    await call.message.answer_audio(open("michel/MICHEL JAKSON – TRILLER.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="3michel")
async def michel3(call: CallbackQuery):
    await call.message.answer_audio(open("michel/Michel Jakson – Get Out Of My Mind.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="4michel")
async def michel4(call: CallbackQuery):
    await call.message.answer_audio(open("michel/Michel Jakson – Blck in Wait(Dj Rad-Mix remix).mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="5michel")
async def michel5(call: CallbackQuery):
    await call.message.answer_audio(open("michel/michel jakson – You are not alone.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="6michel")
async def michel6(call: CallbackQuery):
    await call.message.answer_audio(open("michel/michel jakson – You are not alone.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="7michel")
async def michel7(call: CallbackQuery):
    await call.message.answer_audio(open("michel/Michel Jakson – Black & White.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="8michel")
async def michel8(call: CallbackQuery):
    await call.message.answer_audio(open("michel/MICHEL JAKSON – TRILLER.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="9michel")
async def michel9(call: CallbackQuery):
    await call.message.answer_audio(open("michel/MICHEL JAKSON – TRILLER.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="10michel")
async def michel10(call: CallbackQuery):
    await call.message.answer_audio(open("michel/Michel Jakson – Get Out Of My Mind.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

#xxxtentaction
@dp.message_handler(text="Xxxtentaction")
async def tentaction(msg: Message):
    await msg.answer(textzarubej2, reply_markup=InTentaction)

@dp.callback_query_handler(text="1tentaction")
async def tentaction1(call: CallbackQuery):
    await call.message.answer_audio(open("tentaction/look at me   xxxtentaction.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="2tentaction")
async def tentaction2(call: CallbackQuery):
    await call.message.answer_audio(open("tentaction/SAD!    XXXTentaction.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="3tentaction")
async def tentaction3(call: CallbackQuery):
    await call.message.answer_audio(open("tentaction/Show Time [Ft. XXXTentaction] - Juicy j.mp3S", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="4tentaction")
async def tentaction4(call: CallbackQuery):
    await call.message.answer_audio(open("tentaction/Slipknot.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="5tentaction")
async def tentaction5(call: CallbackQuery):
    await call.message.answer_audio(open("tentaction/XXXTENTACTION – MIX.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="6tentaction")
async def tentaction6(call: CallbackQuery):
    await call.message.answer_audio(open("tentaction/XXXTENTACTION – MIX.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="7tentaction")
async def tentaction7(call: CallbackQuery):
    await call.message.answer_audio(open("tentaction/Slipknot.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="8tentaction")
async def tentaction8(call: CallbackQuery):
    await call.message.answer_audio(open("tentaction/Show Time [Ft. XXXTentaction] - Juicy j.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="9tentaction")
async def tentaction9(call: CallbackQuery):
    await call.message.answer_audio(open("tentaction/SAD!    XXXTentaction.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="10tentaction")
async def tentaction10(call: CallbackQuery):
    await call.message.answer_audio(open("tentaction/look at me   xxxtentaction.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

#billie eilish
@dp.message_handler(text="Billie")
async def billie(msg: Message):
    await msg.answer(textzarubej1, reply_markup=InBillie)

@dp.callback_query_handler(text="1billie")
async def billie1(call: CallbackQuery):
    await call.message.answer_audio(open("billie/2_5291933289639054223.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="2billie")
async def billie2(call: CallbackQuery):
    await call.message.answer_audio(open("billie/4_5789597730116471621.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="3billie")
async def billie3(call: CallbackQuery):
    await call.message.answer_audio(open("billie/31.-I Love You.flac", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="4billie")
async def billie4(call: CallbackQuery):
    await call.message.answer_audio(open("billie/Billie_Eilish-everything_i_wanted.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="5billie")
async def billie5(call: CallbackQuery):
    await call.message.answer_audio(open("billie/Billie_Eilish-everything_i_wanted.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="6billie")
async def billie6(call: CallbackQuery):
    await call.message.answer_audio(open("billie/Billie Eilish - Happier Than Ever (Official Music Video).mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="7billie")
async def billie7(call: CallbackQuery):
    await call.message.answer_audio(open("billie/Billie Eilish - Happier Than Ever (Official Music Video).mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="8billie")
async def billie8(call: CallbackQuery):
    await call.message.answer_audio(open("billie/31.-I Love You.flac", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="9billie")
async def billie9(call: CallbackQuery):
    await call.message.answer_audio(open("billie/4_5789597730116471621.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)

@dp.callback_query_handler(text="10billie")
async def billie10(call: CallbackQuery):
    await call.message.answer_audio(open("billie/2_5291933289639054223.mp3", "rb"), reply_markup=InLike)
    await call.answer(cache_time=30, show_alert=True)







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
