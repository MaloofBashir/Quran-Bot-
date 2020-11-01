<h3 align="center">بِسْمِ ٱللّٰهِ الرَّحْمٰنِ الرَّحِيْمِ</h3>

<h1>@AlQuranBot_  Documentation</h1> <hr>
<h6>Assalaamu Álaykum and welcome to our documention page <h6>
This bot will help users to easily retrive Quranic ayahs on twitter micro blogging website,The bot has been restricted to fetch only single ayah at once because of twitter limting API request policy <hr>

<h3>How to retrieve The ayah</h3>
In its simplified version,english translation of ayah can be retrieved by first mentioning the username of bot (@AlQuranBot_) followed by two parameters(key value pairs) <code>surah={value}</code>or<code>s_name={value}</code>and<code>ayah={value}</code> e.g <br>
 <img src="https://user-images.githubusercontent.com/44017606/97796511-c859b280-1c38-11eb-9510-98a8eeaf9f62.jpg" alt="Surah no and Ayah no" height="500" width="350"><br><img src="https://user-images.githubusercontent.com/44017606/97796450-381b6d80-1c38-11eb-96c1-37ac4b745ab0.jpg" alt="Surah name and ayah number" height="500" width="350">
 <br>
By default the bot will retrieve and reply the mentioned tweet with englsih Translation by Ahmad Ali,You can change the edition(translation) by passing in the <code>ed</code> parameter ,hook with us and and we will discuss how to do that effortlessly
<br>


<h3>How to get differnet editions (translations) of Quran and in different languages</h3>

Users can get the translations of their own choice and the choice of thier own language just by writing one extra parameter <code> ed={value}</code> e.g <code>ed=hi.farooq</code> as shown in images below , here <code>hi</code> represents hindi language and Farooq reprersents the writer's name.All values are written below in a table below .we provide 139 editions by different people in different languages ,Thanks to <a href="https://alquran.cloud/">Al Quran API's</a>  for providing free API's and making it possible for us to spread their work , May Allah bless their team <br>
 <img src="https://user-images.githubusercontent.com/44017606/97796436-2043e980-1c38-11eb-9669-031104395899.jpg" alt="" height="500" width="300"><img src="https://user-images.githubusercontent.com/44017606/97796476-87619e00-1c38-11eb-80a8-792c490a2d4e.jpg" alt="" height="600" width="300"> <br>
 <h3>Commands/Parameters<h3>
  
<table>
  <tr>
    <th>Command/Parameter</th>
   <th>Value</th>
   <th>Type</th>
  </tr>
  <tr>
   <td><code>surah</code></td>
    <td>surah  number from Quran</td>
    <td>Integers ony</td>
  </tr>
  <tr>
   <td><code>ayah</code></td>
    <td>Ayah of mentioned surah</td>
    <td>Integers</td>
  </tr>
  <tr>
   <td><code>s-name</code></td>
    <td>name of the surah</td>
    <td>string </td>
  </tr>
  <tr>
   <td><code>ed</code></td>
    <td>Edition you want</td>
    <td>String</td>
  </tr>
</table>
<h6>We all are very much familiar with the values of surah and ayah so we will be mentioning the values of s-name and ed ony.This will help you to  fetch the diferent editions easily</h6>
<h3>Vaues for ed and s-name </h3>

<table>
  <tr>
   <th><code>s-name</code></th>
   <th><code>ed</code></th>
  </tr>
  <tr>
    <td>
Al-Faatiha <br>
 Al-Baqara  <br>
 Aal-i-Imraan <br>
 An-Nisaa <br>
 Al-Maaida <br>
 Al-An'aam <br>
 Al-A'raaf <br>
 Al-Anfaal <br>
 At-Tawba <br>
 Yunus <br>
 Hud <br>
 Yusuf <br>
 Ar-Ra'd <br>
 Ibrahim <br>
 Al-Hijr <br>
 An-Nahl <br>
 Al-Israa <br>
 Al-Kahf <br>
 Maryam <br>
 Taa-Haa <br>
 Al-Anbiyaa <br>
 Al-Hajj <br>
 Al-Muminoon <br>
 An-Noor <br>
 Al-Furqaan <br>
 Ash-Shu'araa <br>
 An-Naml <br>
 Al-Qasas <br>
 Al-Ankaboot <br>
 Ar-Room <br>
 Luqman <br>
 As-Sajda <br>
 Al-Ahzaab <br>
 Saba <br>
 Faatir <br>
 Yaseen <br>
 As-Saaffaat <br>
 Saad <br>
 Az-Zumar <br>
 Ghafir <br>
 Fussilat <br>
 Ash-Shura <br>
 Az-Zukhruf <br>
 Ad-Dukhaan <br>
 Al-Jaathiya <br>
 Al-Ahqaf <br>
 Muhammad <br>
 Al-Fath <br>
 Al-Hujuraat <br>
 Qaaf <br>
 Adh-Dhaariyat <br>
 At-Tur <br>
 An-Najm <br>
 Al-Qamar <br>
 Ar-Rahmaan <br>
 Al-Waaqia <br>
 Al-Hadid <br>
 Al-Mujaadila <br>
 Al-Hashr <br>
 Al-Mumtahana <br>
 As-Saff <br>
 Al-Jumu'a <br>
 Al-Munaafiqoon <br>
 At-Taghaabun <br>
 At-Talaaq <br>
 At-Tahrim <br>
 Al-Mulk <br>
 Al-Qalam <br>
 Al-Haaqqa <br>
 Al-Ma'aarij <br>
 Nooh <br>
 Al-Jinn <br>
 Al-Muzzammil <br>
 Al-Muddaththir <br>
 Al-Qiyaama <br>
 Al-Insaan <br>
 Al-Mursalaat <br>
 An-Naba <br>
 An-Naazi'aat <br>
 Abasa <br>
 At-Takwir <br>
 Al-Infitaar <br>
 Al-Mutaffifin <br>
 Al-Inshiqaaq <br>
 Al-Burooj <br>
 At-Taariq <br>
 Al-A'laa <br>
 Al-Ghaashiya <br>
 Al-Fajr <br>
 Al-Balad <br>
 Ash-Shams <br>
 Al-Lail <br>
 Ad-Dhuhaa <br>
 Ash-Sharh <br>
 At-Tin <br>
 Al-Alaq <br>
 Al-Qadr <br>
 Al-Bayyina <br>
 Az-Zalzala <br>
 Al-Aadiyaat <br>
 Al-Qaari'a <br>
 At-Takaathur <br>
 Al-Asr <br>
 Al-Humaza <br>
 Al-Fil <br>
 Quraish <br>
 Al-Maa'un <br>
 Al-Kawthar <br>
 Al-Kaafiroon <br>
 An-Nasr <br>
 Al-Masad <br>
 Al-Ikhlaas <br>
 Al-Falaq <br>
 An-Naas <br>
    </td>
    <td>
az.mammadaliyev <br>
 az.musayev <br>
 bn.bengali <br>
 cs.hrbek <br>
 cs.nykl <br>
 de.aburida <br>
 de.bubenheim <br>
 de.khoury <br>
 de.zaidan <br>
 dv.divehi <br>
 en.ahmedali <br>
 en.ahmedraza <br>
 en.arberry <br>
 en.asad <br>
 en.daryabadi <br>
 en.hilali <br>
 en.pickthall <br>
 en.qaribullah <br>
 en.sahih <br>
 en.sarwar <br>
 en.yusufali <br>
 fa.ayati <br>
 fa.fooladvand <br>
 fa.ghomshei <br>
 fa.makarem <br>
 fr.hamidullah <br>
 ha.gumi <br>
 hi.hindi <br>
 id.indonesian <br>
 it.piccardo <br>
 ja.japanese <br>
 ko.korean <br>
 ku.asan <br>
 ml.abdulhameed <br>
 nl.keyzer <br>
 no.berg <br>
 pl.bielawskiego <br>
 pt.elhayek <br>
 ro.grigore <br>
 ru.kuliev <br>
 ru.osmanov <br>
 ru.porokhova <br>
 sd.amroti <br>
 so.abduh <br>
 sq.ahmeti <br>
 sq.mehdiu <br>
 sq.nahi <br>
 sv.bernstrom <br>
 sw.barwani <br>
 ta.tamil <br>
 tg.ayati <br>
 th.thai <br>
 tr.ates <br>
 tr.bulac <br>
 tr.diyanet <br>
 tr.golpinarli <br>
 tr.ozturk <br>
 tr.transliteration <br>
 tr.vakfi <br>
 tr.yazir <br>
 tr.yildirim <br>
 tr.yuksel <br>
 tt.nugman <br>
 ug.saleh <br>
 ur.ahmedali <br>
 ur.jalandhry <br>
 ur.jawadi <br>
 ur.kanzuliman <br>
 ur.qadri <br>
 uz.sodik <br>
 en.maududi <br>
 en.shakir <br>
 en.transliteration <br>
 es.cortes <br>
 fa.ansarian <br>
 quran-simple <br>
 quran-simple-clean <br>
 quran-simple-enhanced <br>
 quran-simple-min <br>
 quran-uthmani-min <br>
 quran-uthmani <br>
 bg.theophanov <br>
 bs.mlivo <br>
 fa.bahrampour <br>
 es.asad <br>
 fa.khorramshahi <br>
 fa.mojtabavi <br>
 hi.farooq <br>
 id.muntakhab <br>
 ms.basmeih <br>
 ru.abuadel <br>
 ru.krachkovsky <br>
 ru.muntahab <br>
 ru.sablukov <br>
 ur.junagarhi <br>
 ur.maududi <br>
 zh.jian <br>
 zh.majian <br>
 fa.khorramdel <br>
 fa.moezzi <br>
 bs.korkut <br>
 ar.jalalayn <br>
 quran-tajweed <br>
 quran-wordbyword <br>
 ar.abdulbasitmurattal <br>
 ar.abdullahbasfar <br>
 ar.abdurrahmaansudais <br>
 ar.abdulsamad <br>
 ar.shaatree <br>
 ar.ahmedajamy <br>
 ar.alafasy <br>
 ar.hanirifai <br>
 ar.husary <br>
 ar.husarymujawwad <br>
 ar.hudhaify <br>
 ar.ibrahimakhbar <br>
 ar.mahermuaiqly <br>
 ar.minshawi <br>
 ar.minshawimujawwad <br>
 ar.muhammadayyoub <br>
 ar.muhammadjibreel <br>
 ar.saoodshuraym <br>
 en.walk <br>
 fa.hedayatfarfooladvand <br>
 ar.parhizgar <br>
 ur.khan <br>
 zh.chinese <br>
 fr.leclerc <br>
 quran-kids <br>
 quran-corpus-qd <br>
 si.naseemismail <br>
 quran-buck <br>
 zh.mazhonggang <br>
 ar.aymanswoaid <br>
 quran-wordbyword-2 <br>
 quran-unicode <br>
 quran-uthmani-quran-academy <br>
 ba.mehanovic <br>
    </td>
  </tr>
</table>

<h3>dos and don'ts</h3>
<ul>
  <li>Mentioning any glyphs or emojis in the tweets will get you an error message</li>
  <li>There should be no space inbetween key value pairs while writing the parameters </li>
  <li>Paramaters can be seperated by the space/multispace or by commas/multicommas</li>
  <li>The bot's username must be mentioned at the beginning of the tweet, 
    positioning the username inbetween will get you an error message </li>
</ul>

<hr>
To make things easy for urdu speaking people,they can write <code>ed=urdu</code> to retrieve the urdu translation of Quran.By default the bot will reply with Ahmad Ali's edition of quran

<hr> We thank you all for comming and reading this documentation page, The bot is still in testing and development mode,for any kinds of queries and suggestions mail us at maloofbashir70@gmail.com or send direct dm to our bot account
