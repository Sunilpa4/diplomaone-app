"""DI01005021 Summer 2026 — Q5 answer parts."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from paperkit import frac, work, steps, result, table, bullets, numbered, h4, p, eq, figure
import matfigs as fig


def join(*chunks):
    return "\n".join(c for c in chunks if c)


Q5 = {
    'title_en': 'Q5 · Rubber, plastics, fibres, varnishes, gaskets and paints',
    'title_gu': 'પ્ર.5 · રબર, પ્લાસ્ટિક, ફાઇબર, વાર્નિશ, ગાસ્કેટ અને પેઇન્ટ',
    'cards': [],
}

Q5['cards'].append(dict(
    number='Q.5 (a)', marks=3, q='Write Difference between natural and vulcanized rubber.',
    en=join(
        p('<b>Natural rubber</b> is <i>cis</i>-polyisoprene obtained from the latex of the rubber tree; it is '
          'soft, sticky and weak. <b>Vulcanised rubber</b> is natural or synthetic rubber heated with '
          'sulphur (2–5 %) so that sulphur bridges form between the long chains and lock them into a '
          'three-dimensional network.'),
        table(['Point', 'Natural rubber', 'Vulcanised rubber'], [
            ['Structure', 'long, separate chains with weak van der Waals force between them',
             'chains cross-linked by sulphur bridges into a 3-D network'],
            ['Tensile strength', 'low, 1.5–3 MPa', 'high, 15–30 MPa'],
            ['Elasticity', 'good but it creeps and takes a permanent set',
             'excellent; returns to shape over a wide temperature range'],
            ['Effect of temperature', 'soft and sticky when warm, hard and brittle when cold',
             'serviceable from about −40 °C to 100 °C'],
            ['Solubility', 'swells and dissolves in petrol, benzene and oils',
             'only swells, does not dissolve; far better oil resistance'],
            ['Hardness and abrasion', 'soft, wears quickly', 'harder, good abrasion resistance'],
            ['Chemical resistance', 'poor', 'better against acids, alkalis and oxidation'],
            ['Use', 'adhesive tape, eraser, crepe sheet — limited', 'tyres, hoses, gaskets, belts, '
             'footwear, cable insulation'],
        ]),
        p('<b>Example:</b> natural rubber latex is used to make a dipped glove that is weak and sticky; the '
          'same glove after vulcanisation is strong, elastic and can be sterilised — a tyre could not be '
          'made from unvulcanised rubber at all, because it would soften on a hot road.'),
    ),
    gu=join(
        p('<b>Natural rubber</b> એ રબરના ઝાડના latexમાંથી મળતું <i>cis</i>-polyisoprene છે; એ soft, ચીકણું અને '
          'નબળું હોય. <b>Vulcanised rubber</b> એ natural કે synthetic rubberને sulphur (2–5 %) સાથે ગરમ '
          'કરીને બનાવાય, જેથી લાંબી chain વચ્ચે sulphur bridges બનીને એમને ત્રિપરિમાણીય networkમાં જકડી '
          'રાખે.'),
        table(['મુદ્દો', 'Natural rubber', 'Vulcanised rubber'], [
            ['Structure', 'લાંબી, અલગ chain વચ્ચે નબળું van der Waals force',
             'sulphur bridgeથી chain cross-link થઈને 3-D network'],
            ['Tensile strength', 'નીચી, 1.5–3 MPa', 'ઊંચી, 15–30 MPa'],
            ['Elasticity', 'સારી પણ creep કરે અને permanent set રહે',
             'ઉત્તમ; વિશાળ તાપમાન રેન્જમાં આકાર પાછો આવે'],
            ['તાપમાનની અસર', 'ગરમીમાં soft અને ચીકણું, ઠંડીમાં hard અને brittle',
             'લગભગ −40 °C થી 100 °C સુધી કામ ચાલે'],
            ['Solubility', 'પેટ્રોલ, benzene અને oilમાં ફૂલે અને ઓગળે',
             'ફક્ત ફૂલે, ઓગળે નહીં; oil resistance ઘણી સારી'],
            ['Hardness અને abrasion', 'soft, ઝડપથી ઘસાય', 'વધુ hard, abrasion resistance સારી'],
            ['Chemical resistance', 'નબળી', 'acid, alkali અને oxidation સામે વધુ સારી'],
            ['ઉપયોગ', 'adhesive tape, eraser, crepe sheet — મર્યાદિત',
             'tyre, hose, gasket, belt, પગરખું, cable insulation'],
        ]),
        p('<b>ઉદાહરણ:</b> natural rubber latexમાંથી બનેલું glove નબળું અને ચીકણું હોય; એ જ glove vulcanise '
          'કર્યા પછી મજબૂત, elastic અને sterilise કરવા યોગ્ય બને — unvulcanised રબરનું ટાયર તો બની જ ન શકે, '
          'કારણ કે ગરમ રસ્તા પર એ ઓગળી જાય.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (b)', marks=4, q='Give Classification of plastic explain any one.',
    en=join(
        h4('Definition'),
        p('<b>Plastics</b> are high polymers, natural or synthetic, that can be softened by heat or a '
          'solvent and shaped under pressure. Their long-chain molecules are held by strong covalent bonds '
          'along the chain and weak forces between chains.'),
        h4('Classification'),
        table(['Basis', 'Types', 'Examples'], [
            ['<b>By behaviour on heating</b>', 'thermoplastic · thermosetting', 'PE, PVC, PP / bakelite, '
             'epoxy, melamine'],
            ['<b>By source</b>', 'natural · synthetic', 'cellulose acetate, casein / PE, PVC, nylon'],
            ['<b>By structure</b>', 'homopolymer · copolymer · blend', 'PE / SBR, ABS / PC-ABS'],
            ['<b>By application</b>', 'commodity · engineering · specialty', 'PE, PP / nylon, POM / PEEK, '
             'PTFE, polyimide'],
            ['<b>By crystallinity</b>', 'amorphous · semi-crystalline', 'PS, PMMA / PE, PP, nylon'],
        ]),
        h4('Explanation of one class — thermoplastic'),
        p('A <b>thermoplastic</b> softens on heating and can be reshaped again and again, because its '
          'chains are held together only by weak secondary forces; heating lets the chains slide past one '
          'another and cooling locks them again. No cross-linking takes place, so the process is reversible.'),
        table(['Point', 'Thermoplastic'], [
            ['Structure', 'long separate chains, no cross-links'],
            ['On heating', 'softens, flows; on cooling, hardens — fully reversible'],
            ['Recycling', 'easy; scrap can be reground and remoulded'],
            ['Solubility', 'soluble in suitable solvents, so it can be cemented'],
            ['Strength', 'good, but creeps under steady load at high temperature'],
            ['Typical examples', 'PE, PP, PVC, polystyrene, PMMA, nylon, ABS, PC'],
            ['Typical products', 'buckets, pipes, bottles, cable insulation, car bumpers, toys'],
        ]),
        h4('Example'),
        p('A bucket is made of HDPE, a thermoplastic, so that a cracked or rejected bucket can be reground '
          'and moulded again. A melamine dinner plate, being thermosetting, cannot be softened again — the '
          'same property gives it a harder surface and better hot-liquid resistance.'),
    ),
    gu=join(
        h4('વ્યાખ્યા'),
        p('<b>Plastics</b> એ ઊંચા polymer છે, કુદરતી કે synthetic, જે heat કે solventથી soft થાય અને pressureમાં '
          'આકાર લે. એમની લાંબી chain molecules chainની દિશામાં મજબૂત covalent bondથી અને chain વચ્ચે નબળા '
          'બળથી બંધાયેલી હોય.'),
        h4('વર્ગીકરણ'),
        table(['આધાર', 'પ્રકાર', 'ઉદાહરણ'], [
            ['<b>ગરમ કરવાના વર્તન પ્રમાણે</b>', 'thermoplastic · thermosetting', 'PE, PVC, PP / bakelite, '
             'epoxy, melamine'],
            ['<b>સ્રોત પ્રમાણે</b>', 'natural · synthetic', 'cellulose acetate, casein / PE, PVC, nylon'],
            ['<b>Structure પ્રમાણે</b>', 'homopolymer · copolymer · blend', 'PE / SBR, ABS / PC-ABS'],
            ['<b>ઉપયોગ પ્રમાણે</b>', 'commodity · engineering · specialty', 'PE, PP / nylon, POM / PEEK, '
             'PTFE, polyimide'],
            ['<b>Crystallinity પ્રમાણે</b>', 'amorphous · semi-crystalline', 'PS, PMMA / PE, PP, nylon'],
        ]),
        h4('એક વર્ગની સમજ — thermoplastic'),
        p('<b>Thermoplastic</b> ગરમ કરવાથી soft થાય અને વારંવાર ફરી આકાર લઈ શકે, કારણ કે એની chain ફક્ત '
          'નબળા secondary બળથી જોડાયેલી હોય; ગરમીમાં chain એકબીજા પર સરકે અને ઠંડું થતાં ફરી જકડાય. કોઈ '
          'cross-linking થતું નથી, એટલે પ્રક્રિયા reversible છે.'),
        table(['મુદ્દો', 'Thermoplastic'], [
            ['Structure', 'લાંબી અલગ chain, cross-link નહીં'],
            ['ગરમ કરવાથી', 'soft થઈને વહે; ઠંડું થતાં hard — પૂરેપૂરું reversible'],
            ['Recycling', 'સહેલું; scrap ફરી grind કરીને mould કરાય'],
            ['Solubility', 'યોગ્ય solventમાં ઓગળે, એટલે cement કરી શકાય'],
            ['Strength', 'સારી, પણ ઊંચા તાપમાને steady loadમાં creep કરે'],
            ['સામાન્ય ઉદાહરણ', 'PE, PP, PVC, polystyrene, PMMA, nylon, ABS, PC'],
            ['સામાન્ય product', 'ડોલ, pipe, બોટલ, cable insulation, car bumper, રમકડાં'],
        ]),
        h4('ઉદાહરણ'),
        p('ડોલ HDPEની બને છે, જે thermoplastic છે, એટલે ફાટેલી કે reject થયેલી ડોલ ફરી grind કરીને mould થઈ '
          'શકે. Melamineની થાળી thermosetting હોવાથી ફરી soft ન થાય — એ જ ગુણધર્મ એને વધુ hard સપાટી અને ગરમ '
          'પ્રવાહી સામે સારો resistance આપે.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (c)', marks=7, q='Give Classification of fiber explain any one.',
    en=join(
        h4('Definition'),
        p('A <b>fibre</b> is a long, thin, flexible thread of material whose length is at least a hundred '
          'times its diameter, and which can be spun into yarn or woven into fabric, or used as '
          'reinforcement in a composite. The high length-to-diameter ratio and the alignment of the '
          'molecules along the axis give a fibre its strength and flexibility.'),
        h4('Classification'),
        table(['Group', 'Sub-group', 'Examples'], [
            ['<b>Natural — vegetable</b>', 'seed, bast, leaf, fruit', 'cotton; jute, flax, hemp; sisal; '
             'coir'],
            ['<b>Natural — animal</b>', 'hair, silk', 'wool, cashmere, mohair; silk'],
            ['<b>Natural — mineral</b>', 'mineral', 'asbestos, basalt fibre'],
            ['<b>Synthetic — regenerated</b>', 'from cellulose or protein', 'rayon (viscose), acetate, '
             'cellulose triacetate'],
            ['<b>Synthetic — condensation polymer</b>', 'polyamide, polyester, polyurethane',
             'nylon 6,6; PET; spandex'],
            ['<b>Synthetic — addition polymer</b>', 'vinyl and acrylic', 'polypropylene, acrylic, '
             'polyethylene, PVC'],
            ['<b>Synthetic — high performance</b>', 'aramid, carbon, glass', 'Kevlar, carbon fibre, '
             'E-glass fibre'],
        ]),
        figure(fig.fibre_tree(),
               'Fig. 5.1 · The two main families of textile fibre.'),
        h4('Explanation of one class — synthetic fibres (nylon as the example)'),
        p('<b>Nylon</b> is a polyamide, made by the condensation polymerisation of adipic acid and '
          'hexamethylene diamine. The repeating unit is held by <b>amide bonds</b>, and hydrogen bonding '
          'between neighbouring chains gives the fibre its strength. It is melt-spun: the polymer is '
          'melted and forced through a spinneret with fine holes, and the filaments are drawn to several '
          'times their length so that the chains align along the axis.'),
        table(['Property', 'Behaviour', 'Engineering meaning'], [
            ['Tenacity', 'high, 4–8 g/denier', 'strong for its weight; ropes and tyre cord'],
            ['Elasticity', 'excellent, recovers almost completely', 'hosiery, stretch fabric, '
             'safe slings'],
            ['Abrasion resistance', 'very good', 'ropes, conveyor belts, brush bristles'],
            ['Moisture regain', 'low, 3.5–4.5 %', 'dries quickly, but clammy in hot weather'],
            ['Chemical resistance', 'good against alkalis; attacked by strong acids and phenol',
             'not for acid service'],
            ['Heat', 'melts at about 250 °C, softens near 220 °C', 'not for high-temperature use'],
            ['Density', '1.14 g/cm<sup>3</sup>', 'lighter than cotton and wool'],
            ['Dyeability', 'good, dyed in the fibre or the yarn', 'coloured fabric'],
        ]),
        h4('Working — from polymer to fibre'),
        steps(('Step 1 · Polymerisation', 'Adipic acid and hexamethylene diamine are heated together and '
                                          'condense, losing water, to give the polyamide. Reason: the '
                                          'reaction has to reach a high molecular weight before spinning, '
                                          'because short chains give a weak fibre.'),
              ('Step 2 · Melt spinning', 'The molten polymer is pumped through a spinneret. Reason: the fine '
                                         'holes decide the filament diameter, which decides the feel and '
                                         'strength of the yarn.'),
              ('Step 3 · Quenching', 'The filaments are cooled in air. Reason: fast cooling gives fine '
                                     'crystals and a smooth surface.'),
              ('Step 4 · Drawing', 'The filaments are stretched 3–5 times their length between rollers. '
                                   'Reason: the chains align along the axis, so the fibre becomes many '
                                   'times stronger — this step is what turns a weak filament into a '
                                   'strong fibre.'),
              ('Step 5 · Texturising, crimping and cutting', 'The yarn is crimped or cut to staple length. '
                                                             'Reason: crimp gives bulk and warmth; staple '
                                                             'allows blending with cotton.')),
        h4('Worked example — linear density of a yarn'),
        p('A 1 km length of nylon filament weighs 4.4 g. Express its linear density in denier and in tex.'),
        work('Given: length = 1 km = 1000 m · mass = 4.4 g',
             'Formula: tex = ' + frac('mass in g', 'length in km'),
             'Substitute: tex = ' + frac('4.4', '1') + ' = 4.4 tex',
             'Denier = 9 × tex = 9 × 4.4'),
        result('Linear density = 4.4 tex = 39.6 denier'),
        p('Sanity check: textile nylon is normally 20–100 denier, and 40 denier is a common hosiery yarn — '
          'the value falls in the expected range.'),
        h4('Limitations and applications'),
        bullets('Synthetic fibres are not biodegradable, they melt and drip when burnt, and they build up '
                'static charge and pick up oil — so they are usually blended with cotton.',
                'Nylon loses strength in strong acids and creeps under sustained load in sunlight; carbon '
                'and aramid fibres are used where stiffness matters but they fail in compression.',
                'Applications: nylon in ropes, hosiery, parachutes, tyre cord, fishing nets, zip fasteners '
                'and brush bristles; polyester in clothing and bottles; aramid in bulletproof vests; glass '
                'and carbon fibre as reinforcement in FRP tanks and pipe.'),
    ),
    gu=join(
        h4('વ્યાખ્યા'),
        p('<b>Fibre</b> એટલે લાંબો, પાતળો, લચીલો દોરો જેની લંબાઈ વ્યાસ કરતાં ઓછામાં ઓછી સો ગણી હોય, અને '
          'જેને yarnમાં કાંતીને કાપડ બનાવી શકાય, કે compositeમાં reinforcement તરીકે વાપરી શકાય. ઊંચો '
          'length-to-diameter ગુણોત્તર અને અક્ષ સાથે moleculeની ગોઠવણી જ fibreને strength અને flexibility આપે.'),
        h4('વર્ગીકરણ'),
        table(['જૂથ', 'ઉપજૂથ', 'ઉદાહરણ'], [
            ['<b>Natural — વનસ્પતિ</b>', 'seed, bast, leaf, fruit', 'કપાસ; જ્યૂટ, flax, hemp; sisal; coir'],
            ['<b>Natural — પ્રાણી</b>', 'વાળ, રેશમ', 'ઊન, pashmina, mohair; રેશમ'],
            ['<b>Natural — ખનિજ</b>', 'mineral', 'asbestos, basalt fibre'],
            ['<b>Synthetic — regenerated</b>', 'cellulose કે proteinમાંથી', 'rayon (viscose), acetate, '
             'cellulose triacetate'],
            ['<b>Synthetic — condensation polymer</b>', 'polyamide, polyester, polyurethane',
             'nylon 6,6; PET; spandex'],
            ['<b>Synthetic — addition polymer</b>', 'vinyl અને acrylic', 'polypropylene, acrylic, '
             'polyethylene, PVC'],
            ['<b>Synthetic — high performance</b>', 'aramid, carbon, glass', 'Kevlar, carbon fibre, '
             'E-glass fibre'],
        ]),
        figure(fig.fibre_tree(),
               'Fig. 5.1 · Textile fibreનાં બે મુખ્ય પરિવાર.'),
        h4('એક વર્ગની સમજ — synthetic fibre (ઉદાહરણ nylon)'),
        p('<b>Nylon</b> એ polyamide છે, જે adipic acid અને hexamethylene diamineના condensation '
          'polymerisationથી બને. Repeating unit <b>amide bond</b>થી જોડાયેલો હોય, અને પાસપાસેની chain વચ્ચેના '
          'hydrogen bond fibreને strength આપે. એ melt-spun છે: polymer ઓગાળીને નાના છિદ્રવાળા spinneretમાંથી '
          'દબાવાય, અને filamentને એની લંબાઈ કરતાં ઘણા ગણા ખેંચાય જેથી chain અક્ષ સાથે ગોઠવાય.'),
        table(['ગુણધર્મ', 'વર્તન', 'engineering અર્થ'], [
            ['Tenacity', 'ઊંચી, 4–8 g/denier', 'વજન પ્રમાણે મજબૂત; દોરડું અને tyre cord'],
            ['Elasticity', 'ઉત્તમ, લગભગ પૂરેપૂરું પાછું આવે', 'hosiery, stretch કાપડ, સલામત sling'],
            ['Abrasion resistance', 'ખૂબ સારી', 'દોરડું, conveyor belt, brushનું bristle'],
            ['Moisture regain', 'ઓછું, 3.5–4.5 %', 'ઝડપથી સૂકાય, પણ ગરમીમાં ચીકણું લાગે'],
            ['Chemical resistance', 'alkali સામે સારી; મજબૂત acid અને phenolથી હુમલો',
             'acid સેવા માટે નહીં'],
            ['Heat', 'લગભગ 250 °C પર ઓગળે, 220 °C પાસે soft થાય', 'ઊંચા તાપમાને ન વપરાય'],
            ['Density', '1.14 g/cm<sup>3</sup>', 'કપાસ અને ઊન કરતાં હલકું'],
            ['Dyeability', 'સારી, fibre કે yarnમાં રંગાય', 'રંગીન કાપડ'],
        ]),
        h4('કાર્ય — polymerથી fibre સુધી'),
        steps(('Step 1 · Polymerisation', 'Adipic acid અને hexamethylene diamine સાથે ગરમ થાય અને પાણી '
                                          'ગુમાવીને polyamide બને. કારણ: spinning પહેલાં ઊંચું molecular weight '
                                          'જરૂરી છે, કારણ કે ટૂંકી chain નબળો fibre આપે.'),
              ('Step 2 · Melt spinning', 'ઓગળેલો polymer spinneretમાંથી દબાય. કારણ: નાના છિદ્ર filamentનો '
                                         'વ્યાસ નક્કી કરે, જે yarnની feel અને strength નક્કી કરે.'),
              ('Step 3 · Quenching', 'Filament હવામાં ઠંડા થાય. કારણ: ઝડપી cooling નાના crystal અને સરળ '
                                     'સપાટી આપે.'),
              ('Step 4 · Drawing', 'Filamentને roller વચ્ચે 3–5 ગણા ખેંચાય. કારણ: chain અક્ષ સાથે ગોઠવાય, એટલે '
                                   'fibre ઘણા ગણો મજબૂત બને — આ જ પગલું નબળા filamentને મજબૂત fibre બનાવે.'),
              ('Step 5 · Texturising, crimping અને કાપણી', 'Yarnને crimp કરાય કે staple લંબાઈમાં કાપાય. '
                                                           'કારણ: crimpથી bulk અને ઉષ્ણતા મળે; stapleથી કપાસ '
                                                           'સાથે blend કરી શકાય.')),
        h4('ઉકેલેલું ઉદાહરણ — yarnની linear density'),
        p('1 km લાંબા nylon filamentનું વજન 4.4 g છે. એની linear density denier અને texમાં કહો.'),
        work('Given: લંબાઈ = 1 km = 1000 m · દળ = 4.4 g',
             'Formula: tex = ' + frac('દળ gમાં', 'લંબાઈ kmમાં'),
             'Substitution: tex = ' + frac('4.4', '1') + ' = 4.4 tex',
             'Denier = 9 × tex = 9 × 4.4'),
        result('Linear density = 4.4 tex = 39.6 denier'),
        p('Sanity check: textile nylon સામાન્ય રીતે 20–100 denier હોય, અને 40 denier સામાન્ય hosiery yarn '
          'છે — કિંમત અપેક્ષિત રેન્જમાં આવે.'),
        h4('મર્યાદાઓ અને ઉપયોગો'),
        bullets('Synthetic fibre biodegradable નથી, બળે ત્યારે ઓગળીને ટપકે, અને static charge તથા oil લે — '
                'એટલે સામાન્ય રીતે કપાસ સાથે blend થાય.',
                'Nylon મજબૂત acidમાં strength ગુમાવે અને સૂર્યપ્રકાશમાં સતત load પર creep કરે; carbon અને '
                'aramid fibre જ્યાં stiffness જોઈએ ત્યાં વપરાય પણ compressionમાં નિષ્ફળ જાય.',
                'ઉપયોગ: nylon — દોરડું, hosiery, parachute, tyre cord, માછલીની જાળ, zip, brush bristle; '
                'polyester — કપડાં અને બોટલ; aramid — bulletproof jacket; glass અને carbon fibre — FRP tank '
                'તથા pipeમાં reinforcement.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (a)', marks=3, tag='OR', q='Give Classification of Varnishes explain any one.',
    en=join(
        p('<b>Varnish</b> is a clear, transparent coating of resin, oil and a solvent (with driers and '
          'thinners) that dries to a hard, glossy film on wood or metal. It protects the surface and shows '
          'the grain or the metal beneath, because it has no pigment.'),
        table(['Basis', 'Types', 'Examples / note'], [
            ['<b>By composition</b>', 'oil varnish · spirit varnish · water varnish',
             'linseed-oil varnish / shellac in spirit / acrylic emulsion'],
            ['<b>By resin used</b>', 'oleoresinous · phenolic · alkyd · polyurethane · epoxy · '
             'cellulose (lacquer)', 'long-oil alkyd, 2-pack PU, epoxy floor varnish'],
            ['<b>By solvent</b>', 'spirit · turpentine · water-borne', 'shellac in methylated spirit'],
            ['<b>By finish</b>', 'gloss · matt · satin', 'furniture varnish, matt wall varnish'],
            ['<b>By use</b>', 'wood · metal · electrical (insulating) · marine',
             'spar varnish for boats, insulating varnish for motor windings'],
        ]),
        h4('Explanation of one class — polyurethane varnish'),
        p('<b>Polyurethane varnish</b> is a two-pack (or moisture-curing) system in which an isocyanate '
          'reacts with a hydroxyl-bearing resin to form a cross-linked urethane network. It is the toughest '
          'clear wood finish in common use.'),
        bullets('<b>Properties:</b> very hard and abrasion resistant, excellent against water, alcohol and '
                'most household chemicals, good gloss retention, resistant to mild alkali.',
                '<b>Use:</b> floors, tabletops, kitchen and bathroom woodwork, exterior woodwork and '
                'marine brightwork.',
                '<b>Limitation:</b> two-pack material has a short pot life after mixing, the solvent is '
                'harmful, it yellows on exterior exposure unless a UV-stable grade is used, and it needs a '
                'dry surface because isocyanate reacts with water and gives carbon dioxide bubbles.'),
        p('<b>Example:</b> a wooden table top finished with two coats of PU varnish resists hot cups and '
          'spilled water, where a shellac (spirit) varnish would turn white within minutes — shellac is '
          'easy to apply and polish but has poor water and heat resistance.'),
    ),
    gu=join(
        p('<b>Varnish</b> એટલે resin, oil અને solvent (drier તથા thinner સાથે) નું સ્વચ્છ, પારદર્શક coating, જે '
          'લાકડા કે ધાતુ પર સૂકીને hard, ચમકદાર પડ બનાવે. એ સપાટીને બચાવે અને નીચેનું grain કે ધાતુ દેખાવા દે, '
          'કારણ કે એમાં pigment હોતું નથી.'),
        table(['આધાર', 'પ્રકાર', 'ઉદાહરણ / નોંધ'], [
            ['<b>રચના પ્રમાણે</b>', 'oil varnish · spirit varnish · water varnish',
             'linseed-oil varnish / spiritમાં shellac / acrylic emulsion'],
            ['<b>વપરાયેલા resin પ્રમાણે</b>', 'oleoresinous · phenolic · alkyd · polyurethane · epoxy · '
             'cellulose (lacquer)', 'long-oil alkyd, 2-pack PU, epoxy floor varnish'],
            ['<b>Solvent પ્રમાણે</b>', 'spirit · turpentine · water-borne', 'methylated spiritમાં shellac'],
            ['<b>Finish પ્રમાણે</b>', 'gloss · matt · satin', 'ફર્નિચર varnish, matt wall varnish'],
            ['<b>ઉપયોગ પ્રમાણે</b>', 'લાકડું · ધાતુ · electrical (insulating) · marine',
             'હોડી માટે spar varnish, motor winding માટે insulating varnish'],
        ]),
        h4('એક પ્રકારની સમજ — polyurethane varnish'),
        p('<b>Polyurethane varnish</b> એ two-pack (કે moisture-curing) system છે જેમાં isocyanate, hydroxyl '
          'વાળા resin સાથે પ્રક્રિયા કરીને cross-linked urethane network બનાવે. સામાન્ય વપરાતા સ્વચ્છ લાકડાના '
          'finishમાં એ સૌથી મજબૂત છે.'),
        bullets('<b>ગુણધર્મ:</b> ખૂબ hard અને abrasion-resistant, પાણી, alcohol અને ઘરેલું રસાયણ સામે ઉત્તમ, '
                'gloss લાંબો ટકે, હળવા alkali સામે ટકે.',
                '<b>ઉપયોગ:</b> ફર્શ, ટેબલની સપાટી, રસોડું અને બાથરૂમનું લાકડાનું કામ, બહારનું woodwork અને '
                'હોડીનું brightwork.',
                '<b>મર્યાદા:</b> બે ભાગ ભેળવ્યા પછી pot life ટૂંકી, solvent નુકસાનકારક, UV-stable ગ્રેડ ન '
                'હોય તો બહાર પીળું પડે, અને સપાટી સૂકી હોવી જોઈએ કારણ કે isocyanate પાણી સાથે પ્રક્રિયા '
                'કરીને carbon dioxideના પરપોટા આપે.'),
        p('<b>ઉદાહરણ:</b> PU varnishનાં બે coat લગાડેલું લાકડાનું ટેબલ ગરમ કપ અને પડેલું પાણી ઝીલે, જ્યાં '
          'shellac (spirit) varnish થોડી મિનિટમાં સફેદ પડી જાય — shellac લગાડવા અને polish કરવા સહેલું છે પણ '
          'પાણી તથા ગરમી સામે નબળું છે.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (b)', marks=4, q='Give classification and uses of Gaskets',
    en=join(
        h4('Definition'),
        p('A <b>gasket</b> is a deformable sealing element clamped between two stationary mating surfaces '
          '(flanges, a cylinder head, a pump casing) to prevent leakage of a fluid. It works by being '
          'compressed until it fills every microscopic irregularity of the joint faces, so the seal is '
          'achieved by <b>yielding</b> of the gasket and not by the bolt force alone.'),
        h4('Classification'),
        table(['Basis', 'Type', 'Material / example', 'Service'], [
            ['<b>By material</b>', 'metallic', 'soft iron, copper, aluminium, monel, SS spiral-wound',
             'high pressure and high temperature'],
            ['', 'non-metallic', 'rubber, PTFE, graphite, CAF, cork, paper', 'low to medium pressure'],
            ['', 'composite', 'graphite on SS tanged insert, PTFE-envelope with rubber core',
             'chemical plant flanges'],
            ['<b>By construction</b>', 'sheet / flat', 'CAF, graphite sheet, rubber sheet', 'general '
             'flanges, covers'],
            ['', 'jacketed', 'PTFE or lead jacket over a soft core', 'glass-lined and plastic vessels'],
            ['', 'spiral-wound', 'SS windings with graphite or PTFE filler', 'high P and T, cyclic duty'],
            ['', 'ring joint (RTJ)', 'oval or octagonal steel ring in a grooved flange', 'oil and gas, '
             'very high pressure'],
            ['', 'kammprofile', 'grooved metal core with soft facing layers', 'heat exchangers'],
            ['', 'O-ring / moulded', 'nitrile, silicone, EPDM, viton', 'pump covers, valve stems, '
             'instrument joints'],
            ['<b>By application</b>', 'steam, oil, water, chemical, cryogenic, food grade',
             'graphite / NBR / EPDM / PTFE / PTFE / silicone', 'chosen to suit the fluid'],
        ]),
        h4('Uses'),
        bullets('Flanged pipe joints and valve bonnets in process plants — the commonest use.',
                'Heat-exchanger and condenser covers and channel flanges (kammprofile and spiral-wound).',
                'Pump casings and covers, compressor heads and cylinder heads of engines.',
                'Glass-lined reactors, where a PTFE-envelope gasket is the only chemically inert choice.',
                'High-pressure oil and gas flanges with ring-joint gaskets, and cryogenic lines with '
                'PTFE or aluminium gaskets.'),
        h4('Choice of gasket — the deciding factors'),
        bullets('<b>Fluid:</b> rubber for water and air, PTFE for acids and solvents, graphite for steam and '
                'hot oils, and no CAF where the fluid is a strong oxidiser.',
                '<b>Pressure:</b> flat sheet up to about 20 bar, spiral-wound to 100 bar, ring joint above '
                'that.',
                '<b>Temperature:</b> nitrile to 100 °C, EPDM to 150 °C, compressed fibre to 400 °C, '
                'graphite to 500 °C and beyond.',
                '<b>Flange condition:</b> a thin gasket needs smooth, flat faces; a thick soft gasket can '
                'take a slightly warped or scored flange.'),
        p('<b>Example:</b> a 10 bar steam line at 250 °C uses a graphite sheet or spiral-wound gasket — '
          'ordinary rubber would harden and fail in a week, and CAF would lose its binder.'),
    ),
    gu=join(
        h4('વ્યાખ્યા'),
        p('<b>Gasket</b> એટલે બે સ્થિર મળતી સપાટી (flange, cylinder head, pump casing) વચ્ચે દબાવીને '
          'રાખાતું deform થઈ શકે એવું sealing element, જે પ્રવાહી લીક થતું અટકાવે. એ દબાઈને jointની સપાટીની '
          'દરેક સૂક્ષ્મ ખામી ભરી દે, એટલે seal gasketના <b>yield</b> થવાથી થાય, ફક્ત bolt forceથી નહીં.'),
        h4('વર્ગીકરણ'),
        table(['આધાર', 'પ્રકાર', 'Material / ઉદાહરણ', 'સેવા'], [
            ['<b>Material પ્રમાણે</b>', 'metallic', 'soft iron, copper, aluminium, monel, SS spiral-wound',
             'ઊંચું pressure અને ઊંચું તાપમાન'],
            ['', 'non-metallic', 'રબર, PTFE, graphite, CAF, cork, paper', 'નીચાથી મધ્યમ pressure'],
            ['', 'composite', 'SS tanged insert પર graphite, rubber core પર PTFE envelope',
             'chemical plantના flange'],
            ['<b>બાંધકામ પ્રમાણે</b>', 'sheet / flat', 'CAF, graphite sheet, રબર sheet', 'સામાન્ય flange, '
             'cover'],
            ['', 'jacketed', 'soft core પર PTFE કે lead jacket', 'glass-lined અને plastic vessel'],
            ['', 'spiral-wound', 'graphite કે PTFE filler સાથે SS winding', 'ઊંચું P અને T, cyclic સેવા'],
            ['', 'ring joint (RTJ)', 'grooved flangeમાં oval કે octagonal steel ring', 'oil અને gas, ખૂબ ઊંચું '
             'pressure'],
            ['', 'kammprofile', 'grooved metal core પર soft facing', 'heat exchanger'],
            ['', 'O-ring / moulded', 'nitrile, silicone, EPDM, viton', 'pump cover, valve stem, instrument '
             'joint'],
            ['<b>ઉપયોગ પ્રમાણે</b>', 'steam, oil, water, chemical, cryogenic, food grade',
             'graphite / NBR / EPDM / PTFE / PTFE / silicone', 'પ્રવાહી પ્રમાણે પસંદ'],
        ]),
        h4('ઉપયોગો'),
        bullets('Process plantમાં flanged pipe joint અને valve bonnet — સૌથી સામાન્ય ઉપયોગ.',
                'Heat exchanger અને condenserના cover તથા channel flange (kammprofile અને spiral-wound).',
                'Pump casing અને cover, compressor head, અને engineનું cylinder head.',
                'Glass-lined reactor, જ્યાં PTFE-envelope gasket જ રાસાયણિક રીતે નિષ્ક્રિય વિકલ્પ છે.',
                'ઊંચા pressureના oil અને gas flange પર ring-joint gasket, અને cryogenic લાઇન પર PTFE કે '
                'aluminium gasket.'),
        h4('Gasketની પસંદગી — નિર્ણાયક પરિબળો'),
        bullets('<b>પ્રવાહી:</b> પાણી અને હવા માટે રબર, acid અને solvent માટે PTFE, steam અને ગરમ oil માટે '
                'graphite, અને મજબૂત oxidiser હોય ત્યાં CAF નહીં.',
                '<b>Pressure:</b> લગભગ 20 bar સુધી flat sheet, 100 bar સુધી spiral-wound, એથી ઉપર ring joint.',
                '<b>તાપમાન:</b> nitrile 100 °C સુધી, EPDM 150 °C સુધી, compressed fibre 400 °C સુધી, graphite '
                '500 °C અને એથી ઉપર.',
                '<b>Flangeની સ્થિતિ:</b> પાતળા gasketને સપાટ, ચોખ્ખી સપાટી જોઈએ; જાડું soft gasket થોડું વાંકું કે '
                'ખૂંચેલું flange પણ ઝીલે.'),
        p('<b>ઉદાહરણ:</b> 250 °C પરની 10 bar steam લાઇનમાં graphite sheet કે spiral-wound gasket વપરાય — '
          'સામાન્ય રબર એક અઠવાડિયામાં hard થઈને નિષ્ફળ જાય, અને CAF પોતાનું binder ગુમાવે.'),
    ),
))

Q5['cards'].append(dict(
    number='Q.5 (c)', marks=7, q='Give Properties, classification, ingredients and uses of paint',
    en=join(
        h4('Definition'),
        p('<b>Paint</b> is a fluid, pigmented coating which, when applied as a thin layer, forms a solid '
          'adherent film that decorates and protects the surface beneath. Unlike varnish it contains '
          '<b>pigment</b>, so it hides the surface instead of showing it.'),
        h4('Ingredients'),
        table(['Ingredient', 'Function', 'Typical example and proportion'], [
            ['<b>Binder / resin / vehicle</b>', 'forms the continuous film and sticks it to the surface; '
             'decides hardness, flexibility and durability', 'alkyd, acrylic, epoxy, PU; 20–40 %'],
            ['<b>Pigment</b>', 'gives colour, opacity and hiding power; also gives corrosion inhibition and '
             'weather resistance', 'TiO<sub>2</sub> white, red iron oxide, zinc chromate primer; 10–40 %'],
            ['<b>Extender / filler</b>', 'cheapens the film, gives sanding and film-build properties, '
             'controls gloss', 'talc, calcium carbonate, barytes; 5–25 %'],
            ['<b>Solvent / thinner</b>', 'dissolves the binder so the paint can be brushed or sprayed, then '
             'evaporates', 'white spirit, xylene, water; 20–50 %'],
            ['<b>Additives</b>', 'small amounts that control specific behaviour',
             'driers (cobalt naphthenate), anti-skinning, anti-settling, dispersant, biocide, '
             'anti-foam; 0.1–2 %'],
        ]),
        figure(fig.paint_layers(),
               'Fig. 5.2 · Primer, under coat and top coat, each with its own job.'),
        h4('Classification'),
        table(['Basis', 'Types', 'Examples'], [
            ['<b>By vehicle</b>', 'oil · alkyd · acrylic · epoxy · polyurethane · cellulosic · '
             'cementitious · bituminous · water-based emulsion',
             'linseed-oil paint, 2-pack epoxy, emulsion distemper, bitumen paint'],
            ['<b>By solvent</b>', 'solvent-borne · water-borne · solvent-free (100 % solids) · powder',
             'enamel / latex paint / epoxy coating / powder coating'],
            ['<b>By function</b>', 'primer · under coat · finishing coat · sealer · putty',
             'zinc chromate primer, gloss enamel'],
            ['<b>By finish</b>', 'gloss · semi-gloss · matt · satin',
             'rich gloss enamel, matt emulsion'],
            ['<b>By service</b>', 'interior · exterior · heat-resisting · marine · chemical-resistant · '
             'fire-retardant · anti-fouling',
             'aluminium paint for hot surfaces, epoxy for tanks'],
        ]),
        h4('Properties required of a good paint'),
        table(['Property', 'Meaning'], [
            ['Opacity / hiding power', 'one coat covers the old colour and the bare surface'],
            ['Adhesion', 'the film sticks to the substrate and does not peel or blister'],
            ['Flexibility and hardness together', 'it bends with the metal without cracking, and still '
             'resists scratching'],
            ['Water and chemical resistance', 'it does not soften or chalk in the weather or in the '
             'plant atmosphere'],
            ['Drying time', 'touch-dry in a reasonable time, but not so fast that brush marks are left'],
            ['Colour and gloss retention', 'the colour does not fade and the gloss does not chalk away'],
            ['Non-toxic and safe', 'no lead or chrome pigments on articles that children or food touch'],
        ]),
        h4('Working — how a paint film forms'),
        steps(('Step 1 · Surface preparation', 'The surface is degreased, derusted and primed. Reason: paint '
                                              'sticks only to a clean, rough surface; rust under a film '
                                              'continues to grow.'),
              ('Step 2 · Primer', 'The first coat is applied and wets the surface. Reason: the primer bonds '
                                  'to the metal and carries the corrosion inhibitor, so it must be in '
                                  'direct contact with the steel.'),
              ('Step 3 · Solvent evaporation', 'The thinner leaves the film. Reason: the film loses its '
                                               'fluidity and stops running; this is the physical part of '
                                               'drying.'),
              ('Step 4 · Oxidation or curing', 'The binder cross-links, by taking oxygen from the air (oil '
                                               'and alkyd) or by reacting with a hardener (epoxy and PU). '
                                               'Reason: the cross-linked network gives hardness, adhesion '
                                               'and chemical resistance.'),
              ('Step 5 · Under coat and top coat', 'Further coats build the film thickness. Reason: a total '
                                                   'dry film thickness of 150–250 µm is needed in a '
                                                   'chemical plant; one thin coat has pinholes and cannot '
                                                   'resist the atmosphere.')),
        h4('Uses'),
        bullets('Protection of steel structures, bridges, pipelines, storage tanks and process equipment '
                '(primer + under coat + top coat system).',
                'Marine and offshore: epoxy and antifouling systems on hulls and platforms.',
                'Buildings: emulsion on walls, enamel on wood and metal, distemper in rural areas.',
                'Special duties: heat-resisting aluminium paint on furnaces and exhausts, chemical-resistant '
                'epoxy inside tanks, food-grade and non-toxic paints in dairies.',
                'Traffic and safety marking: road marking paint, and colour coding of pipes as per IS '
                '2379.'),
        h4('Worked example — paint required for a tank'),
        p('A cylindrical tank of diameter 4 m and height 3 m is to be painted on the outside with two '
          'coats at a coverage of 10 m<sup>2</sup> per litre per coat. Find the quantity of paint, adding '
          '10 % for loss.'),
        work('Given: D = 4 m · H = 3 m · coverage = 10 m<sup>2</sup>/litre/coat · number of coats = 2 · '
             'loss = 10 %',
             'Shell area = π · D · H = 3.1416 × 4 × 3',
             'Shell area = 37.70 m<sup>2</sup>',
             'Area for two coats = 2 × 37.70 = 75.40 m<sup>2</sup>',
             'Paint = ' + frac('75.40', '10') + ' = 7.54 litre',
             'With 10 % loss = 7.54 × 1.10 = 8.29 litre'),
        result('Paint required ≈ 8.3 litre (add a little more for the top and the nozzles)'),
        p('Sanity check: about 4.2 litre per coat for 37.7 m<sup>2</sup> is a normal figure for enamel at '
          '50 µm dry film thickness — correct.'),
        h4('Limitations'),
        bullets('Paint is a barrier, not a structural repair: it cannot stop corrosion once the film is '
                'broken, so the coating must be repaired at the first sign of damage.',
                'Solvent-borne paints release VOC, so water-borne and high-solids systems are now preferred '
                'in enclosed areas.',
                'Multiple thin coats are needed; a single thick coat traps solvent, blisters and peels.',
                'The film fails quickly if the surface was not prepared or was wet, and no paint survives '
                'above its rated temperature — aluminium paint is needed above 200 °C.'),
    ),
    gu=join(
        h4('વ્યાખ્યા'),
        p('<b>Paint</b> એ પ્રવાહી, pigment વાળું coating છે જે પાતળા સ્તરમાં લગાડતાં સપાટી પર મજબૂત ચોંટતો '
          'ઘન પડ બનાવે અને નીચેની સપાટીને શણગારે તથા બચાવે. Varnishથી વિપરીત એમાં <b>pigment</b> હોય, એટલે '
          'એ સપાટી દેખાવા ન દે, ઢાંકી દે.'),
        h4('ઘટકો'),
        table(['ઘટક', 'કામ', 'સામાન્ય ઉદાહરણ અને પ્રમાણ'], [
            ['<b>Binder / resin</b>', 'સતત પડ બનાવે અને સપાટી સાથે ચોંટાડે; hardness, flexibility અને '
             'durability નક્કી કરે', 'alkyd, acrylic, epoxy, PU; 20–40 %'],
            ['<b>Pigment</b>', 'રંગ, opacity અને hiding power આપે; corrosion inhibition અને weather '
             'resistance પણ', 'TiO<sub>2</sub> સફેદ, red iron oxide, zinc chromate primer; 10–40 %'],
            ['<b>Extender / filler</b>', 'પડ સસ્તું કરે, sanding અને film-build ગુણ આપે, gloss નિયંત્રિત કરે',
             'talc, calcium carbonate, barytes; 5–25 %'],
            ['<b>Solvent / thinner</b>', 'binder ઓગાળે જેથી brush કે spray થઈ શકે, પછી ઊડી જાય',
             'white spirit, xylene, પાણી; 20–50 %'],
            ['<b>Additive</b>', 'ખૂબ ઓછા પ્રમાણમાં ચોક્કસ વર્તન નિયંત્રિત કરે',
             'drier (cobalt naphthenate), anti-skinning, anti-settling, dispersant, biocide, anti-foam; '
             '0.1–2 %'],
        ]),
        figure(fig.paint_layers(),
               'Fig. 5.2 · Primer, under coat અને top coat — દરેકનું પોતાનું કામ.'),
        h4('વર્ગીકરણ'),
        table(['આધાર', 'પ્રકાર', 'ઉદાહરણ'], [
            ['<b>Vehicle પ્રમાણે</b>', 'oil · alkyd · acrylic · epoxy · polyurethane · cellulosic · '
             'cementitious · bituminous · water-based emulsion',
             'linseed-oil paint, 2-pack epoxy, emulsion distemper, bitumen paint'],
            ['<b>Solvent પ્રમાણે</b>', 'solvent-borne · water-borne · solvent-free (100 % solids) · powder',
             'enamel / latex paint / epoxy coating / powder coating'],
            ['<b>કામ પ્રમાણે</b>', 'primer · under coat · finishing coat · sealer · putty',
             'zinc chromate primer, gloss enamel'],
            ['<b>Finish પ્રમાણે</b>', 'gloss · semi-gloss · matt · satin', 'rich gloss enamel, matt emulsion'],
            ['<b>સેવા પ્રમાણે</b>', 'interior · exterior · heat-resisting · marine · chemical-resistant · '
             'fire-retardant · anti-fouling', 'ગરમ સપાટી માટે aluminium paint, tank માટે epoxy'],
        ]),
        h4('સારા paintમાં જરૂરી ગુણધર્મ'),
        table(['ગુણધર્મ', 'અર્થ'], [
            ['Opacity / hiding power', 'એક coatમાં જૂનો રંગ અને ખુલ્લી સપાટી ઢંકાય'],
            ['Adhesion', 'પડ સપાટી સાથે ચોંટેલું રહે, peel કે blister ન થાય'],
            ['Flexibility અને hardness સાથે', 'ધાતુ સાથે વળે પણ ફાટે નહીં, અને ખૂટે પણ નહીં'],
            ['પાણી અને chemical resistance', 'હવામાં કે plantના વાતાવરણમાં soft કે chalk થાય નહીં'],
            ['Drying time', 'વાજબી સમયમાં touch-dry થાય, પણ એટલી ઝડપી નહીં કે brushના નિશાન રહી જાય'],
            ['રંગ અને gloss ટકે', 'રંગ ઝાંખો ન પડે અને gloss chalk થઈને ન જાય'],
            ['Non-toxic અને સલામત', 'બાળકો કે ખાવાની વસ્તુ સ્પર્શે એવી વસ્તુ પર lead કે chrome pigment નહીં'],
        ]),
        h4('કાર્ય — paintનો પડ કેવી રીતે બને'),
        steps(('Step 1 · સપાટીની તૈયારી', 'સપાટી degrease, derust અને prime કરાય. કારણ: paint ફક્ત સાફ, ખરબચડી '
                                          'સપાટી પર ચોંટે; પડ નીચેનો કાટ વધતો જાય.'),
              ('Step 2 · Primer', 'પહેલો coat લગાડાય અને સપાટીને ભીની કરે. કારણ: primer ધાતુ સાથે ચોંટે અને '
                                 'corrosion inhibitor લઈ જાય, એટલે એ સીધો steelના સંપર્કમાં જોઈએ.'),
              ('Step 3 · Solvent ઊડવું', 'Thinner પડમાંથી નીકળી જાય. કારણ: પડ પ્રવાહીપણું ગુમાવે અને વહેવાનું '
                                        'અટકે; સૂકવણીનો આ ભૌતિક ભાગ છે.'),
              ('Step 4 · Oxidation કે curing', 'Binder cross-link થાય — હવામાંથી oxygen લઈને (oil અને alkyd) કે '
                                              'hardener સાથે પ્રક્રિયા કરીને (epoxy અને PU). કારણ: cross-linked '
                                              'network hardness, adhesion અને chemical resistance આપે.'),
              ('Step 5 · Under coat અને top coat', 'વધુ coat પડની થિકનેસ વધારે. કારણ: chemical plantમાં કુલ '
                                                  'dry film thickness 150–250 µm જોઈએ; એક પાતળા coatમાં '
                                                  'pinhole રહે અને વાતાવરણ ઝીલી ન શકે.')),
        h4('ઉપયોગો'),
        bullets('Steel structure, પુલ, pipeline, storage tank અને process equipmentની સુરક્ષા (primer + under '
                'coat + top coat system).',
                'Marine અને offshore: હોડી તથા platform પર epoxy અને antifouling system.',
                'મકાન: દીવાલ પર emulsion, લાકડા અને ધાતુ પર enamel, ગામડામાં distemper.',
                'ખાસ કામ: furnace અને exhaust પર heat-resisting aluminium paint, tankની અંદર '
                'chemical-resistant epoxy, dairyમાં food-grade અને non-toxic paint.',
                'Traffic અને સલામતી: road marking paint, અને IS 2379 પ્રમાણે pipeનું colour coding.'),
        h4('ઉકેલેલું ઉદાહરણ — tank માટે કેટલું paint'),
        p('4 m વ્યાસ અને 3 m ઊંચાઈના cylinder tankની બહારની સપાટી પર બે coat લગાડવાના છે, અને દર coatે '
          '10 m<sup>2</sup> પ્રતિ લિટર coverage છે. 10 % loss ગણીને paintનો જથ્થો શોધો.'),
        work('Given: D = 4 m · H = 3 m · coverage = 10 m<sup>2</sup>/લિટર/coat · coat = 2 · loss = 10 %',
             'Shell area = π · D · H = 3.1416 × 4 × 3',
             'Shell area = 37.70 m<sup>2</sup>',
             'બે coat માટે ક્ષેત્રફળ = 2 × 37.70 = 75.40 m<sup>2</sup>',
             'Paint = ' + frac('75.40', '10') + ' = 7.54 લિટર',
             '10 % loss સાથે = 7.54 × 1.10 = 8.29 લિટર'),
        result('જરૂરી paint ≈ 8.3 લિટર (ઉપરના ભાગ અને nozzle માટે થોડું વધારે રાખવું)'),
        p('Sanity check: 37.7 m<sup>2</sup> માટે પ્રતિ coat લગભગ 4.2 લિટર એ 50 µm dry film thickness પર enamel '
          'માટે સામાન્ય આંકડો છે — સાચું છે.'),
        h4('મર્યાદાઓ'),
        bullets('Paint એ barrier છે, structural મરામત નહીં: પડ તૂટ્યા પછી કાટ અટકાવી ન શકે, એટલે પહેલી નિશાની '
                'દેખાય ત્યાં જ repair કરવી પડે.',
                'Solvent-borne paint VOC છોડે, એટલે બંધ જગ્યામાં હવે water-borne અને high-solids system પસંદ '
                'કરાય.',
                'પાતળા ઘણા coat જોઈએ; એક જાડો coat solvent ફસાવે, blister થાય અને peel થાય.',
                'સપાટી તૈયાર ન હોય કે ભીની હોય તો પડ ઝડપથી નિષ્ફળ જાય, અને રેટ કરેલા તાપમાનથી ઉપર કોઈ paint '
                'ટકતું નથી — 200 °Cથી ઉપર aluminium paint જોઈએ.'),
    ),
))
