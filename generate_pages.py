#!/usr/bin/env python3
"""Gjeneron 30 faqet HTML për projektin shkollor."""

import os

BASE = os.path.dirname(os.path.abspath(__file__))

FALLBACK_IMG = (
    "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9"
    "?auto=format&fit=crop&w=1600&q=85"
)


def u(photo_id: str, w: int = 1400) -> str:
    return f"https://images.unsplash.com/{photo_id}?auto=format&fit=crop&w={w}&q=85"


HEAD = """<!DOCTYPE html>
<html lang="sq">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{desc}" />
  <title>{title} — Vendi ku dua të jetoj: New York</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
</head>
"""

HERO = """
  <section class="hero" style="--hero-image: url('{hero_img}')">
    <div class="hero-inner">
      <span class="hero-label">Projekt Gjuhe · New York City</span>
      <h1>{h1}</h1>
      <p class="subtitle">{sub}</p>
    </div>
  </section>
"""

CHROME = """
  <div id="site-footer"></div>
  <script src="js/navigation.js"></script>
  <script src="js/effects.js"></script>
</body>
</html>
"""

BODY_START = '<body>\n  <div id="site-header"></div>\n'

PAGES = [
    {
        "file": "index.html",
        "title": "Hyrja",
        "desc": "Harvard Zani — Projekt Gjuhe: Vendi ku dua të jetoj, New York City, 30 faqe.",
        "hero": ("Vendi ku dua të jetoj", "Harvard Zani · SHKA 26 Nëntori · Tiranë"),
        "img": (u("photo-1496442226666-8d4d0e62e6e9"), "Skylajni i New York City"),
        "home": True,
    },
    {
        "file": "rreth-projektit.html",
        "title": "Rreth Projektit",
        "desc": "Informacione rreth projektit shkollor për New Yorkun.",
        "hero": ("Rreth Projektit", "Qëllimi, struktura dhe burimet e këtij punimi"),
        "sections": [
            ("Qëllimi i projektit", "<p>Ky website është <strong>projekti im për lëndën e Gjuhës Shqipe</strong> me temën <em>Vendi ku dua të jetoj</em>. Kam zgjedhur <strong>New York City</strong> sepse dua të shpreh me shkrim ëndrrën time për të jetuar në një qytet plot kulturë, histori dhe mundësi.</p><p>Projekti përbëhet nga <strong>30 faqe</strong> që përshkruajnë qytetin me gjuhë të pasur dhe të qartë shqipe.</p>"),
            ("Struktura e punimit", "<p>Faqet janë të organizuara tematikisht: fillojmë me arsyet e zgjedhjes së qytetit, vazhdojmë me informacione gjeografike dhe demografike, pastaj eksplorojmë pesë borough-et, infrastrukturën, arsimin, ekonominë dhe kulturën.</p><ul class='check-list'><li>Faqet 1–7: Hyrje dhe kontekst i përgjithshëm</li><li>Faqet 8–12: Lagjet (borough-et)</li><li>Faqet 13–19: Jeta praktike</li><li>Faqet 20–28: Kultura dhe atraksione</li><li>Faqet 29–30: Siguria dhe përfundimi</li></ul>"),
            ("Burimet", "<p>Informacionet bazohen në burime publike zyrtare (NYC.gov, Census Bureau, MTA), materiale edukative dhe enciklopedi të besueshme. Fotot janë nga Unsplash me qëllim ilustrues.</p>"),
        ],
        "fact": "New York City quhet shpesh \"Qyteti që nuk fle kurrë\" (The City That Never Sleeps).",
        "img": (u("photo-1496442226666-8d4d0e62e6e9"), "Pamje e Manhattan-it"),
    },
    {
        "file": "pse-new-york.html",
        "title": "Pse New York?",
        "desc": "Arsyet pse dua të jetoj në New York City.",
        "hero": ("Pse New York?", "Arsyet personale dhe objektive për zgjedhjen e këtij qyteti"),
        "sections": [
            ("Zgjedhja ime personale", "<p>New York më tërheq sepse është një <strong>qendër globale</strong> e financave, artit, teknologjisë dhe shkencës. Këtu mund të gjesh njerëz nga çdo kulturë dhe të mësosh nga diversiteti i tyre.</p><p>Dua të jetoj në një vend ku <strong>çdo ditë ofron diçka të re</strong> — ekspozita, koncerte, biblioteka të mëdha dhe mundësi vullnetarizmi.</p>"),
            ("Mundësitë", "<p>NYC ka mijëra shkolla dhe universitete të njohura. Kompanitë më të mëdha botërore kanë zyra këtu. Për dikë ambicioz, qyteti ofron rrjet profesional dhe kreativ të pakrahasueshëm.</p>"),
            ("Sfida që pranoj", "<p>E di që jeta është e shtrenjtë dhe ritmi i shpejtë. Por për mua sfida është pjesë e rritjes personale. Plani im është të studioj mirë, të punoj me kohë të pjesshme dhe të zgjedh lagjen e duhur.</p>"),
        ],
        "fact": "Mbi 800 gjuhë fliten në shtëpitë e New Yorkut — më shumë se në çdo qytet tjetër në SHBA.",
        "img": (u("photo-1549923746-c497d50f3720"), "Times Square natën"),
    },
    {
        "file": "historia.html",
        "title": "Historia",
        "desc": "Historia e shkurtër e New York City.",
        "hero": ("Historia e New Yorkut", "Nga fshatrat holandeze te metropoli i sotëm"),
        "sections": [
            ("Fillimet", "<p>Më parë quhej <strong>New Amsterdam</strong>, themeluar nga Hollandezët në vitin <strong>1624</strong> në ishullin Manhattan. Më vonë u mor nga britanikët dhe u riemërtua New York, nderuar Dukësit James të Yorkut.</p>"),
            ("Rritja e qytetit", "<p>Në shekullin XIX, fluksi i emigrantëve e shndërroi qytetin. Ndërtimi i <strong>Erie Canal</strong> (1825) e lidhi NYC me brendësinë e Amerikës. Statuja e Lirisë (1886) u bë simbol i mirëseardhjes për miliona emigrantë.</p>"),
            ("Shekulli XX dhe XXI", "<p>Ndërtesa Empire State (1931), zhvillimi i Wall Street, 11 Shtatori 2001 dhe rimëkëmbja pas tij — çdo epokë ka lënë gjurmë. Sot NYC është qyteti më i populluar i SHBA-së.</p>"),
        ],
        "fact": "Manhattan u ble nga vendasit amerikanë me mallra vlerë rreth 60 guldenë holandeze (legjenda e famshme).",
        "img": (u("photo-1477959858617-67f85cf4f646"), "Arkitekturë historike në NYC"),
    },
    {
        "file": "gjeografia.html",
        "title": "Gjeografia",
        "desc": "Gjeografia dhe vendndodhja e New York City.",
        "hero": ("Gjeografia", "Vendndodhja, ishujt dhe peizazhi urban"),
        "sections": [
            ("Ku ndodhet", "<p>New York City ndodhet në <strong>shtetin New York</strong>, në bregun atlantik të SHBA-së, ku lumrat Hudson dhe East takohen me oqeanin. Qyteti përbëhet nga pesë <strong>borough-e</strong> të mëdha.</p>"),
            ("Relievi dhe uji", "<p>Manhattan është ishull, i lidhur me Brooklyn përmes urave. Hudson në perëndim, East River në lindje. <strong>Central Park</strong> është hapësirë e gjelbër në zemër të Manhattan-it.</p>"),
            ("Zona metropolitane", "<p>NYC është qendra e zonës metropolitane tri-shtetërore (NY, NJ, CT) me mbi 20 milionë banorë — një nga zonat më të dendura në botë.</p>"),
        ],
        "fact": "Sipërfaqja e NYC është rreth 789 km² — më e vogël se shumë kryeqytete, por shumë e denduar.",
        "img": (u("photo-1524661134678-49403ce4c74c"), "Harta dhe peizazh urban"),
    },
    {
        "file": "klima.html",
        "title": "Klima",
        "desc": "Klima dhe stinët në New York City.",
        "hero": ("Klima", "Katër stinë të qarta në qytetin atlantik"),
        "sections": [
            ("Stinët", "<p><strong>Pranverë</strong> (mars–maj): ngrohet gradualisht, shpesh me shi. <strong>Verë</strong> (qershor–gusht): e nxehtë dhe lagësht, 25–32°C. <strong>Vjeshtë</strong>: ngjyra të bukura në Central Park. <strong>Dimër</strong>: i ftohtë, borë dhe era nga oqeani.</p>"),
            ("Çfarë të pres", "<p>Temperaturat dimërore mund të bien nën -10°C me erë të fortë. Vera kërkon klimatizim në apartamente. Vjeshta është stina më e këndshme për ecje turistike.</p>"),
            ("Ndryshimet klimatike", "<p>Stuhitë si Sandy (2012) treguan vulnerabilitetin e zonave bregdetare. Qyteti investon në mbrojtje dhe infrastrukturë rezistente.</p>"),
        ],
        "fact": "NYC merr mesatarisht rreth 120 cm bore në vit — më shumë se shumë qytete në Evropë.",
        "img": (u("photo-1549501269-5a0166c263b0"), "Dimër në qytet"),
    },
    {
        "file": "popullsia.html",
        "title": "Popullsia",
        "desc": "Popullsia dhe diversiteti i New York City.",
        "hero": ("Popullsia", "Mbi 8 milionë banorë, kultura dhe komunitete"),
        "sections": [
            ("Numrat", "<p>New York City ka rreth <strong>8,3 milionë</strong> banorë (2024). Dendësia është një nga më të lartat në Amerikën e Veriut — mbi 10 000 banorë për km² në shumë zona.</p>"),
            ("Diversiteti", "<p>Emigrantët kanë formuar komunitete: Chinatown, Little Italy, Koreatown, Brighton Beach (rusë), Jackson Heights (latinë dhe aziatikë) etj. Kjo e bën qytetin <strong>gjeli të botës</strong>.</p>"),
            ("Moshat dhe familjet", "<p>Qyteti tërheq të rinjtë për studim dhe karrierë, por ka edhe familje shumë breza që jetojnë këtu. Politikat sociale dhe shërbimet publike janë të rëndësishme për jetën urbane.</p>"),
        ],
        "fact": "Rreth 37% e banorëve të NYC lindën jashtë Shteteve të Bashkuara.",
        "img": (u("photo-1449824913935-59a10b8d2000"), "Njerëz në rrugët e qytetit"),
    },
    {
        "file": "manhattan.html",
        "title": "Manhattan",
        "desc": "Manhattan — zemra e New York City.",
        "hero": ("Manhattan", "Financa, teatër dhe skylajni ikonik"),
        "sections": [
            ("Përshkrimi", "<p>Manhattan është ishulli më i famshëm — <strong>Wall Street</strong>, Broadway, Fifth Avenue, Central Park. Këtu ndodhet shumica e zyrave dhe atraksioneve turistike.</p>"),
            ("Lagjet", "<p>Harlem në veri, Upper East/West Side, Midtown me Times Square, SoHo, Greenwich Village, Financial District në jug. Çdo zonë ka karakter unik.</p>"),
            ("Pse dua të jetoj këtu", "<p>Manhattan është e shtrenjtë, por ofron akses në gjithçka me këmbë ose metro. Për një student ambicioz, të jetosh këtu është ëndërr — edhe nëse fillon në lagje fqinje më të lira.</p>"),
        ],
        "fact": "Manhattan ka rreth 1,6 milionë banorë por ditën popullsia rritet me miliona që punojnë këtu.",
        "img": (u("photo-1496442226666-8d4d0e62e6e9"), "Skylajni i Manhattan-it"),
    },
    {
        "file": "brooklyn.html",
        "title": "Brooklyn",
        "desc": "Brooklyn — lagje kreative dhe familjare.",
        "hero": ("Brooklyn", "Art, muzikë dhe komunitete në rritje"),
        "sections": [
            ("Karakteri", "<p>Brooklyn është borough-i më i populluar (~2,6 milionë). Ka lagje si <strong>Williamsburg</strong> (hipster, teknologji), DUMBO (pamje në urë), Park Slope (familje).</p>"),
            ("Kultura", "<p>Brooklyn Museum, Barclays Center, plazhet e Coney Island. Shumë artistë dhe muzikantë jetojnë këtu për shkak të çmimeve më të arsyeshme se Manhattan.</p>"),
            ("Për mua", "<p>Brooklyn do të ishte zgjedhja ime realiste për banim: më afër Manhattan me metro, por me hapësirë më të madhe dhe komunitet të ngrohtë.</p>"),
        ],
        "fact": "Nëse Brooklyn ishte qytet i veçantë, do të ishte i 4-ti më i madh në SHBA.",
        "img": (u("photo-1555507036-ab781f05f2c9"), "Rrugë në Brooklyn"),
    },
    {
        "file": "queens.html",
        "title": "Queens",
        "desc": "Queens — diversiteti më i madh në NYC.",
        "hero": ("Queens", "Aeroportet, sporti dhe kuzhina botërore"),
        "sections": [
            ("Përshkrimi", "<p>Queens është borough-i më i madh sipërfaqësorisht dhe shumë i larmishëm. Këtu janë <strong>JFK</strong> dhe LaGuardia — dy aeroportet kryesore.</p>"),
            ("Atraksione", "<p>Flushing Meadows (panairi i vitit 1964), US Open tenis, MoMA PS1 në Long Island City. Restorante autentike nga çdo vend.</p>"),
            ("Banorët", "<p>Çmimet e banesave janë më të ulëta se Manhattan; shumë familje emigrante zgjedhin Queens për shkollat dhe hapësirën.</p>"),
        ],
        "fact": "Queens është borough-i më shumëllojshëm etnikisht në të gjithë Amerikën.",
        "img": (u("photo-1469854523086-cc02fe5d8800"), "Lagje në Queens"),
    },
    {
        "file": "bronx.html",
        "title": "Bronx",
        "desc": "Bronx — muzikë, baseball dhe Bronx Zoo.",
        "hero": ("Bronx", "Vendlindja e hip-hop dhe Yankees"),
        "sections": [
            ("Historia kulturore", "<p>Bronx konsiderohet <strong>vendlindja e hip-hop</strong> (vite 1970). Ka identitet të fortë dhe histori të pasur afro-amerikane dhe latine.</p>"),
            ("Atraksione", "<p>Yankee Stadium, Bronx Zoo (një nga më të mëdhenjt në botë), New York Botanical Garden. Pelham Bay Park është hapësira e gjelbër më e madhe.</p>"),
            ("Zhvillimi", "<p>Bronx ka pasur sfida ekonomike, por investime të reja dhe projekte banimi po ndryshojnë peizazhin.</p>"),
        ],
        "fact": "Hip-hop u lind në festat e bllokut në Bronx në vitet 1970.",
        "img": (u("photo-1598038184677-2aee902f9c9c"), "Bronx dhe skylajni"),
    },
    {
        "file": "staten-island.html",
        "title": "Staten Island",
        "desc": "Staten Island — qetësi dhe natyrë.",
        "hero": ("Staten Island", "Trageti, natyrë dhe ritëm më i ngadaltë"),
        "sections": [
            ("Karakteri", "<p>Staten Island është më i izoluar — lidhet me Manhattan me <strong>tragetin falas</strong> Staten Island Ferry, me pamje të Statujës së Lirisë.</p>"),
            ("Jeta", "<p>Më shumë shtëpi private, më pak apartamente. Banorët shpesh punojnë në Manhattan por duan qetësi familjare.</p>"),
            ("Greenbelt", "<p>Zona të gjera të gjelbra, plazhe dhe parku Greenbelt ofrojnë pushim nga zhurma e qytetit.</p>"),
        ],
        "fact": "Trageti Staten Island është falas dhe transporton mbi 70 000 pasagjerë në ditë.",
        "img": (u("photo-1570168009150-c09975c327ec"), "Trageti drejt Manhattan-it"),
    },
    {
        "file": "transporti.html",
        "title": "Transporti",
        "desc": "Transporti publik dhe privat në NYC.",
        "hero": ("Transporti", "Metro, autobus, taksi dhe biçikleta"),
        "sections": [
            ("Pse nuk duhet makinë", "<p>Shumica e banorëve nuk kanë nevojë për makinë. <strong>MTA</strong> (Metropolitan Transportation Authority) drejton sistemin më të madh në Amerikën e Veriut.</p>"),
            ("Mënyra të tjera", "<p>Autobusët, tramvajët në lagje të caktuara, Yellow Cabs dhe aplikacionet (Uber/Lyft). Ecja me këmbë është normale — distancat në Manhattan janë të arsyeshme.</p>"),
            ("Citi Bike", "<p>Sistemi i biçikletave të përbashkëta lejon lëvizje të shpejtë për distanca të shkurtra, veçanërisht në verë.</p>"),
        ],
        "fact": "Vetëm rreth 45% e familjeve në Manhattan kanë makinë.",
        "img": (u("photo-1544620341-cfb3403f1c47"), "Transport publik"),
    },
    {
        "file": "metroja.html",
        "title": "Metropolitana",
        "desc": "Metropolitana e New York City.",
        "hero": ("Metropolitana", "24 orë, 472 stacione, legjendë urbane"),
        "sections": [
            ("Sistemi", "<p>Metroja e NYC hapet në <strong>1904</strong>. Sot ka 472 stacione dhe rreth 660 milje shinash. Funksionon <strong>24/7</strong> — e rrallë në qytete amerikane.</p>"),
            ("Si funksionon", "<p>Paguhet me MetroCard ose pa kontakt (OMNY). Një udhëtim koston rreth $2.90 (2024). Linjat identifikohen me shkronja dhe numra (A, C, 1, 2, etj.).</p>"),
            ("Këshilla", "<p>Shmang orarin 8–9 dhe 17–18 në ditët e javës. Lexo hartën e linjave para se të hipësh — ndonjëherë duhet të ndërrosh stacion.</p>"),
        ],
        "fact": "Metroja e NYC transporton mbi 3 miliardë pasagjerë në vit.",
        "img": (u("photo-1515896769750-31548aa180ed"), "Stacion metroje"),
    },
    {
        "file": "shkollat.html",
        "title": "Shkollat",
        "desc": "Sistemi arsimor publik në New York City.",
        "hero": ("Shkollat", "NYC Department of Education — sistemi më i madh në SHBA"),
        "sections": [
            ("Arsimi publik", "<p><strong>NYC DOE</strong> ka mbi 1,1 milion nxënës në shkolla publike — më i madhi se shumë shtete amerikane. Shkollat fillore (elementary), të mesme (middle) dhe të larta (high school).</p>"),
            ("Shkollat e specializuara", "<p>Stuyvesant, Bronx Science, Brooklyn Tech — shkolla të larta teknike me pranim konkurrues. Art, muzikë dhe sport ofrohen në shumë shkolla.</p>"),
            ("Plani im", "<p>Do të aplikoja për shkolla me programe të mira në shkenca dhe gjuhë të huaja. Prindërit dhe këshilltarët ndihmojnë në zgjedhjen e shkollës së duhur.</p>"),
        ],
        "fact": "Rreth 40% e nxënësve flasin një gjuhë tjetër përveç anglishtes në shtëpi.",
        "img": (u("photo-1524999729-8d8e47d126e6"), "Kampus shkollor"),
    },
    {
        "file": "universitetet.html",
        "title": "Universitetet",
        "desc": "Universitetet dhe kolegjet në NYC.",
        "hero": ("Universitetet", "Columbia, NYU, CUNY dhe shumë të tjera"),
        "sections": [
            ("Institucione elitare", "<p><strong>Columbia University</strong> në Manhattan Verior, <strong>New York University (NYU)</strong> në Greenwich Village, The New School për art dhe shkenca sociale.</p>"),
            ("CUNY", "<p>City University of New York — sistem publik me Baruch, Hunter, Queens College etj. Çmime më të arsyeshme për banorët e NYC.</p>"),
            ("Pse dua të studioj këtu", "<p>Universitetet e NYC ofrojnë praktika në kompani lokale, qasje në biblioteka dhe rrjet alumni global. Ëndrra ime është të studioj drejtësi, biznes ose informatikë këtu.</p>"),
        ],
        "fact": "NYC ka mbi 110 kolegje dhe universitete brenda kufijve të qytetit.",
        "img": (u("photo-1562774053-701939374585"), "Kampus universitar"),
    },
    {
        "file": "karriera.html",
        "title": "Karriera",
        "desc": "Punësimi dhe karriera në New York City.",
        "hero": ("Karriera", "Wall Street, media, modë dhe teknologji"),
        "sections": [
            ("Sektoret kryesorë", "<p><strong>Financa</strong> (Wall Street), <strong>media</strong> (NBC, CNN, NY Times), <strong>modë</strong> (Garment District), <strong>teknologji</strong> (Silicon Alley), turizëm, shëndetësi, arsim.</p>"),
            ("Punë për studentë", "<p>Shumë punë me kohë të pjesshme: barista, shitës, ndihmës në biblioteka, internship. Rroga minimale në NYC është më e lartë se mesatarja kombëtare.</p>"),
            ("Rrjetimi", "<p>Evente profesionale, LinkedIn, alumni networks — në NYC takimi i duhur mund të ndryshojë karrierën.</p>"),
        ],
        "fact": "Produkti metropolitan i NYC është mbi 2 trilionë dollarë — si ekonomi e madhe e një vendi.",
        "img": (u("photo-1486406146926-c627a92ad1ab"), "Zyrat e Manhattan-it"),
    },
    {
        "file": "kostoja.html",
        "title": "Kostoja e Jetesës",
        "desc": "Sa kushton të jetosh në New York City.",
        "hero": ("Kostoja e Jetesës", "E shtrenjtë, por me planifikim është e mundur"),
        "sections": [
            ("Çmimet", "<p>Qiraja e një apartamenti 1-dhomësh në Manhattan mund të kalojë <strong>$3,500–4,500/muaj</strong>. Në Brooklyn ose Queens, $2,000–2,800. Ushqimi, sigurimet dhe argëtimi shtojnë kosto.</p>"),
            ("Krahasimi", "<p>NYC renditet ndër qytetet më të shtrenjta në botë. Por pagat mesatare janë më të larta, dhe shërbimet publike (metro, shkolla) lehtësojnë jetën.</p>"),
            ("Strategjitë", "<p>Të ndash apartamentin (roommates), të jetosh në periferi, të gatuash në shtëpi, të përdorësh bibliotekat falas — këto janë mënyra që studentët i përdorin.</p>"),
        ],
        "fact": "Indeksi i kostos së jetesës në NYC është rreth 40% më i lartë se mesatarja kombëtare amerikane.",
        "img": (u("photo-1560518883-ce09059eeffa"), "Apartamente në qytet"),
    },
    {
        "file": "banesa.html",
        "title": "Banesat",
        "desc": "Ku dhe si banojnë njerëzit në NYC.",
        "hero": ("Banesat", "Apartamente, brownstones dhe kooperativa"),
        "sections": [
            ("Llojet e banesave", "<p><strong>Apartamente në ndërtesa të larta</strong> (pre-war, luxury high-rises), <strong>brownstones</strong> në Brooklyn, studiot e vogla për studentë.</p>"),
            ("Qiraja vs blerja", "<p>Shumica qiranë. Blerja e apartamentit në Manhattan kërkon shuma shumë të mëdha. Co-op dhe condo kanë rregulla të veçanta.</p>"),
            ("Plani im i banimit", "<p>Fillimisht do të qeroja me shokë shkolle në Brooklyn ose Queens, afër stacionit të metrosë. Me kalimin e kohës, synoj apartament më të mirë.</p>"),
        ],
        "fact": "Mbi 70% e banorëve të NYC jetojnë me qira, jo si pronarë.",
        "img": (u("photo-1502672260266-1c1ef1d93788"), "Apartament tipik urban"),
    },
    {
        "file": "kultura.html",
        "title": "Kultura",
        "desc": "Kultura dhe arti në New York City.",
        "hero": ("Kultura", "Teatër, muzikë, art dhe letërsi 24/7"),
        "sections": [
            ("Skena artistike", "<p><strong>Broadway</strong> për teatër muzikor, Carnegie Hall për muzikë klasike, galeri në Chelsea, street art në Bushwick.</p>"),
            ("Letërsia dhe media", "<p>Shumë autorë kanë shkruar për NYC — Fitzgerald, Baldwin, Angelou. Revistat dhe podcast-et kulturore janë kudo.</p>"),
            ("Pjesëmarrja", "<p>Studentët mund të blejnë bileta me zbritje (TKTS), të shkojnë në ngjarje falas në park, të vullnetarizojnë në festivale.</p>"),
        ],
        "fact": "NYC ka mbi 1,500 galeri arti dhe mbi 200 teatra.",
        "img": (u("photo-1578662996442-48f60103fc96"), "Teatër dhe kulturë"),
    },
    {
        "file": "muzeet.html",
        "title": "Muzeet",
        "desc": "Muzeet më të famshme të New York City.",
        "hero": ("Muzeet", "Nga Metropolitan te MoMA dhe Museum of Natural History"),
        "sections": [
            ("Metropolitan Museum of Art", "<p>Met — një nga muzeet më të mëdha në botë, me art nga çdo epokë. Rrugë e Museum Mile në Upper East Side.</p>"),
            ("Të tjerat", "<p><strong>MoMA</strong> (art modern), <strong>Guggenheim</strong> (arkitekturë e Frank Lloyd Wright), <strong>American Museum of Natural History</strong> (dinozaurë, planete).</p>"),
            ("Akses", "<p>Shumë muze kanë ditë me pagesë sipas mundësisë (pay-what-you-wish) ose hyrje falas për studentë me kartë.</p>"),
        ],
        "fact": "Met ka mbi 2 milionë vepra arti në koleksion.",
        "img": (u("photo-1564399579883-451a5d44ec08"), "Muze arti"),
    },
    {
        "file": "central-park.html",
        "title": "Central Park",
        "desc": "Central Park — parajsa e gjelbër e Manhattan-it.",
        "hero": ("Central Park", "843 hektarë natyrë në zemër të qytetit"),
        "sections": [
            ("Historia", "<p>Hapësirë e dizajnuar në vitet 1850 nga Frederick Law Olmsted dhe Calvert Vaux. Sot është <strong>parku më i vizituar urban</strong> në SHBA.</p>"),
            ("Çfarë të bësh", "<p>Ecje, vozitje me çaj, liqeni me jahte, Zoo, skulptura, koncerte verore. Dimer me patina dhe vozitje me qerre.</p>"),
            ("Rëndësia", "<p>Central Park është frymëmarrja e qytetit — pa të, jeta në Manhattan do të ishte shumë më e vështirë psikologjikisht.</p>"),
        ],
        "fact": "Central Park është më i madh se Monaco sa i përket sipërfaqes.",
        "img": (u("photo-1588426778066-7becf028f543"), "Central Park"),
    },
    {
        "file": "times-square.html",
        "title": "Times Square",
        "desc": "Times Square — zemra e turizmit në NYC.",
        "hero": ("Times Square", "Ekrane gjigante, Broadway dhe miliona vizitorë"),
        "sections": [
            ("Përshkrimi", "<p>Kryqëzimi i Broadway dhe 7th Avenue në Midtown. E njohur për <strong>reklamat LED</strong>, turmën dhe festimin e Vitit të Ri (ball drop).</p>"),
            ("Turizmi", "<p>Mbi 50 milionë vizitorë në vit. Dyqane, teatro Broadway afër, personazhe me kostum (Mickey Mouse etj.).</p>"),
            ("Kritika dhe dashuri", "<p>Banorët e shmangin për shkak të turmës, por për vizitorin e parë është magjike. Unë do ta vizitoja me miq, por nuk do të banoja këtu.</p>"),
        ],
        "fact": "Times Square quhej më parë Longacre Square deri në 1904.",
        "img": (u("photo-1549923746-c497d50f3720"), "Times Square"),
    },
    {
        "file": "statuja-e-lirise.html",
        "title": "Statuja e Lirisë",
        "desc": "Statuja e Lirisë — simbol i lirisë dhe emigracionit.",
        "hero": ("Statuja e Lirisë", "Liberty Enlightening the World — 1886"),
        "sections": [
            ("Origjina", "<p>Dhuruar nga Franca, dizajnuar nga Auguste Bartholdi. Në bazë shkruan: <em>\"Give me your tired, your poor...\"</em> — poemë e Emma Lazarus për emigrantët.</p>"),
            ("Vizita", "<p>Ndodhet në Liberty Island. Trageti nga Battery Park. Mund të ngjitesh në kurorë me rezervim paraprak.</p>"),
            ("Simbolizmi", "<p>Për miliona familje, Statuja ishte e para që shiheshin duke ardhur me anije — shpresa për jetë të re. Për mua, përfaqëson vlerat e diversitetit.</p>"),
        ],
        "fact": "Statuja është 93 metra e lartë nga toka deri në majë të pishtarit.",
        "img": (u("photo-1485735672647-775a7092da25"), "Statuja e Lirisë"),
    },
    {
        "file": "ura-brooklyn.html",
        "title": "Ura e Brooklyn",
        "desc": "Brooklyn Bridge — ikonë inxhinierike.",
        "hero": ("Ura e Brooklyn", "Lidh Manhattan me Brooklyn që nga 1883"),
        "sections": [
            ("Ndërtimi", "<p>Kur u hap, ishte ura më e gjatë e varur në botë. Dizajn i John Roebling. Simbol i forcës amerikane pas Luftës Civile.</p>"),
            ("Sot", "<p>Kalojnë makina, biçikletë dhe këmbësorë. Ecja në kanal të dedikuar ofron pamje spektakolare të skylajnit.</p>"),
            ("Fotografia", "<p>Është një nga vendet më të fotografuara në botë — veçanërisht në agim dhe perëndim.</p>"),
        ],
        "fact": "Ndërtimi zgjati 14 vjet dhe kushtoi jetën e disa punëtorëve.",
        "img": (u("photo-1514565131-fce0801e5785"), "Brooklyn Bridge"),
    },
    {
        "file": "sporti.html",
        "title": "Sporti",
        "desc": "Sporti profesional në New York City.",
        "hero": ("Sporti", "Yankees, Mets, Knicks, Rangers dhe më shumë"),
        "sections": [
            ("Baseball", "<p><strong>NY Yankees</strong> (Bronx) — 27 tituj World Series. <strong>NY Mets</strong> (Queens) — rivalë në National League.</p>"),
            ("Basketboll dhe hokej", "<p><strong>Knicks</strong> (NBA) dhe <strong>Nets</strong> (Brooklyn). <strong>Rangers</strong> dhe Islanders në NHL.</p>"),
            ("Maratona dhe tenis", "<p><strong>NYC Marathon</strong> në nëntor — një nga më të mëdhenjt. <strong>US Open</strong> tenis në Flushing Meadows.</p>"),
        ],
        "fact": "New York është qyteti i vetëm amerikan me dy ekipe në të njëjtën ligë për baseball.",
        "img": (u("photo-1574629810360-7efbbe195a0b"), "Stadium sportiv"),
    },
    {
        "file": "gastronomia.html",
        "title": "Gastronomia",
        "desc": "Ushqimi dhe restorantet në NYC.",
        "hero": ("Gastronomia", "Nga pizza newyorkeze te kuzhina botërore"),
        "sections": [
            ("Specialitetet", "<p><strong>Pizza</strong> me copë (slice), bagels me lox, hot dog nga karrocave, cheesecake, pastrami sandwich në delikatese të vjetra.</p>"),
            ("Diversiteti", "<p>Mund të hash sushi në Japantown, curry në Little India, tacos në Bronx, falafel në Queens — cilësia është e lartë.</p>"),
            ("Buxheti", "<p>Nga street food $5 deri te restorante me yje Michelin. Studentët gjejnë oferta në aplikacione dhe happy hour.</p>"),
        ],
        "fact": "NYC ka mbi 27,000 restorante — më shumë se shumë vende europiane kanë në total.",
        "img": (u("photo-1555396273-367ea4eb4db5"), "Restorant në NYC"),
    },
    {
        "file": "festivalet.html",
        "title": "Festivalet",
        "desc": "Festivalet dhe ngjarjet në New York City.",
        "hero": ("Festivalet", "Parada, koncerte dhe festa gjatë gjithë vitit"),
        "sections": [
            ("Paradat", "<p><strong>Thanksgiving Parade</strong> (Macy's), paradë St. Patrick's Day, Pride March në qershor, West Indian Day Parade.</p>"),
            ("Muzikë dhe film", "<p>SummerStage koncerte falas, Tribeca Film Festival, Governors Ball në Randalls Island.</p>"),
            ("Festat", "<p>Ball drop në Times Square (31 dhjetor), festa të lagjeve, Nënat e Muzeve, Open House New York.</p>"),
        ],
        "fact": "Macy's Thanksgiving Parade filloi në vitin 1924.",
        "img": (u("photo-1514525253161-7a46d19cd819"), "Festë në qytet"),
    },
    {
        "file": "siguria.html",
        "title": "Siguria",
        "desc": "Siguria dhe jetë e përditshme në NYC.",
        "hero": ("Siguria", "Realiteti urban dhe këshilla për banorë"),
        "sections": [
            ("Statistikat", "<p>NYC është <strong>më i sigurt</strong> sesa në vitet 1980–90. Krimi ka rënë shumë, por si çdo metropol, kërkon vëmendje — veçanërisht natën në zona të izoluara.</p>"),
            ("Këshilla", "<p>Mos trego telefonin në metro, qëndro në zona të ndriçuara, njofto shokët ku je, përdor aplikacione të sigurta për taksi.</p>"),
            ("Emergjencat", "<p>Numri 911 për polici/zjarr/ambulancë. Shumë kamra sigurie dhe komunitete të organizuara ndihmojnë në lagje.</p>"),
        ],
        "fact": "NYC ka rreth 36,000 oficerë policie — një nga forcat më të mëdha në SHBA.",
        "img": (u("photo-1529156069898-49953e39b3ac"), "Rrugët e qytetit"),
    },
    {
        "file": "konkluzioni.html",
        "title": "Konkluzioni",
        "desc": "Përfundimi i projektit — Vendi ku dua të jetoj.",
        "hero": ("Konkluzioni", "Pse New York mbetet vendi ku dua të jetoj"),
        "sections": [
            ("Çfarë mësova", "<p>Duke punuar këtë projekt me <strong>30 faqe</strong>, kuptova që New York nuk është vetëm turizëm — është sistem kompleks i transportit, arsimit, ekonomisë dhe kulturave që bashkëjetojnë.</p>"),
            ("Plani im", "<p>Plani im është të përfundoj shkollën me nota të mira, të mësoj anglishten dhe një gjuhë tjetër, të aplikoj për universitet në NYC dhe të filloj karrierën me internship. Do të jetoj fillimisht në Brooklyn ose Queens.</p>"),
            ("Mesazhi final", "<p>New York është <strong>vendi ku dua të jetoj</strong> sepse më sfidon, më frymëzon dhe më ofron mundësi për të kontribuar në botë. Edhe nëse rruga është e gjatë, çdo hap më afër këtij qyteti është investim në të ardhmen time.</p>"),
            ("Faleminderit", "<p>Faleminderit që lexuat projektin tim për Gjuhën Shqipe. Unë, <strong>Harvard Zani</strong> nga SHKA \"26 Nëntori\" në Tiranë, shpresoj që këto 30 faqe ju ndihmuan të njihni më mirë New York City — qytetin ku dua të jetoj.</p>"),
        ],
        "fact": "„If I can make it there, I'll make it anywhere“ — kënga e famshme për NYC.",
        "img": (u("photo-1496442226666-8d4d0e62e6e9", 1800), "New York — vendi ku dua të jetoj"),
    },
]


def home_page(p):
    toc_rows = ""
    titles = [
        "Hyrja", "Rreth Projektit", "Pse New York?", "Historia", "Gjeografia",
        "Klima", "Popullsia", "Manhattan", "Brooklyn", "Queens", "Bronx",
        "Staten Island", "Transporti", "Metropolitana", "Shkollat", "Universitetet",
        "Karriera", "Kostoja e Jetesës", "Banesat", "Kultura", "Muzeet",
        "Central Park", "Times Square", "Statuja e Lirisë", "Ura e Brooklyn",
        "Sporti", "Gastronomia", "Festivalet", "Siguria", "Konkluzioni",
    ]
    files = [x["file"] for x in PAGES]
    for i, (f, t) in enumerate(zip(files, titles), 1):
        toc_rows += f'<tr><td>{i}</td><td><a href="{f}">{t}</a></td></tr>\n'

    cards = [
        ("pse-new-york.html", "Pse New York?", "Arsyet e zgjedhjes së qytetit", "photo-1549923746-c497d50f3720"),
        ("manhattan.html", "Manhattan", "Zemra e qytetit", "photo-1496442226666-8d4d0e62e6e9"),
        ("metroja.html", "Metropolitana", "Transporti 24/7", "photo-1515896769750-31548aa180ed"),
        ("central-park.html", "Central Park", "Natyrë në qytet", "photo-1588426778066-7becf028f543"),
        ("konkluzioni.html", "Konkluzioni", "Përfundimi i projektit", "photo-1496442226666-8d4d0e62e6e9"),
    ]
    card_html = ""
    for href, title, desc, img_id in cards:
        card_html += f"""
        <article class="home-card">
          <a href="{href}">
            <div class="img-wrap">
              <img class="content-image" src="{u(img_id, 800)}" alt="{title}" loading="lazy" decoding="async" />
            </div>
            <div class="body"><h3>{title}</h3><p>{desc}</p></div>
          </a>
        </article>"""

    hero_img = p.get("img", (FALLBACK_IMG, ""))[0]

    return f"""{HEAD.format(desc=p["desc"], title=p["title"])}{BODY_START}
{HERO.format(h1=p["hero"][0], sub=p["hero"][1], hero_img=hero_img)}
  <main class="container wide">
    <section class="student-info">
      <div class="student-info-header">
        <h2>Informacione për projektin</h2>
        <p>Punim për lëndën e Gjuhës Shqipe — viti shkollor 2025–2026</p>
      </div>
      <div class="student-info-body">
        <dl>
          <dt>Studenti:</dt><dd class="highlight">Harvard Zani</dd>
          <dt>Klasa:</dt><dd>Klasa IX (9-vjeçare)</dd>
          <dt>Shkolla:</dt><dd>SHKA "26 Nëntori", Tiranë</dd>
          <dt>Lënda:</dt><dd>Gjuha Shqipe</dd>
          <dt>Tema:</dt><dd>Vendi ku dua të jetoj</dd>
          <dt>Qyteti:</dt><dd>New York City, SHBA</dd>
          <dt>Numri i faqeve:</dt><dd>30</dd>
        </dl>
      </div>
    </section>
    <p class="lead">Përshëndetje! Unë jam <strong>Harvard Zani</strong> dhe kjo është puna ime për Gjuhën Shqipe. Këtu do të gjeni <strong>30 faqe</strong> rreth New York City — qytetit ku dua të jetoj një ditë.</p>
    <div class="home-grid">{card_html}</div>
    <h2 class="section-title">Tabela e përmbajtjes — të 30 faqet</h2>
    <table class="toc-table">
      <thead><tr><th>#</th><th>Faqja</th></tr></thead>
      <tbody>{toc_rows}</tbody>
    </table>
    <div class="fact-box"><strong>E ditët?</strong> New York City quhet "Big Apple" — emri u përhap në vitet 1920 nga gazetarët e sportit.</div>
  </main>
{CHROME}
"""


def content_page(p):
    sections_html = ""
    for title, body in p.get("sections", []):
        sections_html += f"""
    <section class="content-section">
      <h2>{title}</h2>
      {body}
    </section>"""

    img_url, img_cap = p.get("img", (FALLBACK_IMG, ""))
    hero_img = img_url or FALLBACK_IMG
    img_block = f"""
    <figure class="figure-block">
      <img class="content-image" src="{img_url}" alt="{img_cap}" loading="lazy" decoding="async" />
      <figcaption>{img_cap}</figcaption>
    </figure>"""

    fact = p.get("fact", "")
    fact_block = f'<div class="fact-box"><strong>E ditët?</strong> {fact}</div>' if fact else ""

    return f"""{HEAD.format(desc=p["desc"], title=p["title"])}{BODY_START}
{HERO.format(h1=p["hero"][0], sub=p["hero"][1], hero_img=hero_img)}
  <main class="container">
    <p class="lead">{p["desc"]}</p>
    {img_block}
    {sections_html}
    {fact_block}
  </main>
{CHROME}
"""


def main():
    for p in PAGES:
        path = os.path.join(BASE, p["file"])
        if p.get("home"):
            html = home_page(p)
        else:
            html = content_page(p)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print("Created:", p["file"])


if __name__ == "__main__":
    main()
