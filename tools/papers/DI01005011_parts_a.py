"""DI01005011 Winter 2025 — Q1 and Q2 answer parts."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from paperkit import frac, work, steps, result, table, bullets, numbered, h4, p, eq, figure
import chemfigs as fig


def join(*chunks):
    return "\n".join(c for c in chunks if c)


# ---------------------------------------------------------------- Q1
Q1 = {
    'title_en': 'Q1 · Ice refrigeration, UV sterilisation and water softening',
    'title_gu': 'પ્ર.1 · આઇસ રેફ્રિજરેશન, UV સ્ટરીલાઇઝેશન અને પાણી સોફ્ટ કરવું',
    'cards': [],
}

Q1['cards'].append(dict(
    number='Q.1 (a)', marks=3, q='Explain Ice refrigeration.',
    en=join(
        h4('Definition'),
        p('<b>Ice refrigeration</b> is the oldest method of cooling. Ice is manufactured in an ice plant, '
          'stored, and then used to keep a space or a product below room temperature.'),
        p('The cooling is not done by a machine at the point of use — it comes from the <b>latent heat of '
          'fusion</b> of ice: about <b>334 kJ</b> is absorbed by every kilogram of ice that melts at 0 °C.'),
        h4('Working'),
        bullets('A vapour-compression unit cools CaCl<sub>2</sub> <b>brine</b> to about −10 °C in the brine tank.',
                'Ice cans filled with clean water stand in the brine; the water freezes into blocks in 24–36 hours.',
                'The blocks are stored in an insulated house and carried to the cold room, wagon or fish box.',
                'While the ice melts it takes heat from the load, so the load stays near 0–5 °C.'),
        h4('Where it is used, and the limit'),
        p('Ice is used for fish and meat transport, milk chilling, and small cold stores where the power '
          'supply is unreliable. Its limit is fixed by the melting point: it cannot go below 0 °C, it is bulky, '
          'and the melted water has to be drained away.'),
        figure(fig.ice_plant(), 'Fig. 1.1 · Ice plant — the unit chills brine, the brine freezes the ice cans.'),
    ),
    gu=join(
        h4('વ્યાખ્યા'),
        p('<b>Ice refrigeration</b> એ સૌથી જૂની ઠંડક પદ્ધતિ છે. Ice plantમાં બરફ બનાવીને સંગ્રહ કરાય છે અને '
          'પછી તેનાથી જગ્યા કે product ને room temperatureથી નીચે રાખવામાં આવે છે.'),
        p('ઠંડક વાપરવાની જગ્યાએ કોઈ machineથી નહીં, પણ બરફના <b>latent heat of fusion</b>થી મળે છે: '
          '0 °C પર પીગળતા દરેક કિલો બરફ સામે લગભગ <b>334 kJ</b> heat શોષાય છે.'),
        h4('કેવી રીતે કામ કરે છે'),
        bullets('Vapour-compression unit brine tankમાં CaCl<sub>2</sub> <b>brine</b>ને લગભગ −10 °C સુધી ઠંડો કરે છે.',
                'સાફ પાણી ભરેલા ice cans brineમાં રહે છે; 24–36 કલાકમાં પાણી બરફના blocks બને છે.',
                'Blocksને insulated houseમાં રાખીને cold room, wagon કે fish boxમાં લઈ જવાય છે.',
                'બરફ પીગળતી વખતે loadમાંથી heat લે છે, એટલે load 0–5 °C આસપાસ રહે છે.'),
        h4('ઉપયોગ અને મર્યાદા'),
        p('Fish–meat transport, milk chilling અને નાના cold storeમાં વપરાય છે, ખાસ કરીને જ્યાં electricity '
          'બરાબર ન હોય. મર્યાદા melting pointથી નક્કી થાય: 0 °Cથી નીચે જઈ શકે નહીં, જગ્યા વધુ લાગે અને '
          'પીગળેલું પાણી કાઢવું પડે.'),
        figure(fig.ice_plant(), 'આકૃતિ 1.1 · Ice plant — unit brineને ઠંડો કરે, brine ice cansને થિજવે.'),
    ),
))

Q1['cards'].append(dict(
    number='Q.1 (b)', marks=4, q='Explain Sterilization using UV rays as green techniques.',
    en=join(
        h4('Principle'),
        p('<b>UV sterilisation</b> kills micro-organisms with ultraviolet light of about <b>254 nm</b>. The '
          'photon energy is absorbed by the nucleic acid of the cell, so the DNA cannot replicate and the '
          'bacteria, virus or spore becomes inactive within seconds.'),
        figure(fig.uv_sterilizer(), 'Fig. 1.2 · UV chamber fitted in a water line.'),
        h4('Construction and working'),
        numbered('A stainless-steel chamber holds one or more low-pressure mercury lamps inside quartz sleeves.',
                 'Filtered water flows as a thin film around the lamp, so every layer receives the light.',
                 'The lamp is switched on before the flow starts; a contact time of a few seconds gives the dose.',
                 'Treated water leaves the chamber. The quartz sleeve is cleaned regularly and lamp hours are logged.'),
        h4('Why it is called a green technique'),
        bullets('No chlorine or other chemical is dosed, so no harmful by-product such as trihalomethane is formed.',
                'Taste, colour and odour of the water do not change.',
                'No chemical to store, transport or dispose of — only electricity is consumed.',
                'No corrosive chemical on site, so handling is safe.'),
        h4('Limitations'),
        p('UV gives <b>no residual protection</b>: water stored after treatment can grow bacteria again. '
          'Turbidity and colour shield the microbes, so the water must be clear. Lamps lose output with age, '
          'so they are replaced every 8,000–9,000 hours.'),
    ),
    gu=join(
        h4('સિદ્ધાંત'),
        p('<b>UV sterilisation</b>માં લગભગ <b>254 nm</b>નું ultraviolet light વાપરીને સૂક્ષ્મ જીવોને મારવામાં '
          'આવે છે. UV energy cellના nucleic acid શોષી લે છે, એટલે DNA વધી શકતું નથી અને bacteria, virus કે '
          'spore થોડી સેકન્ડમાં નિષ્ક્રિય થઈ જાય છે.'),
        figure(fig.uv_sterilizer(), 'આકૃતિ 1.2 · પાણીની લાઇનમાં લગાડેલું UV chamber.'),
        h4('રચના અને કાર્ય'),
        numbered('Stainless-steel chamberમાં quartz sleeveમાં એક કે વધુ low-pressure mercury lamp રાખાય છે.',
                 'Filter કરેલું પાણી lampની આસપાસ પાતળા પડમાં વહે છે, જેથી દરેક layerને light મળે.',
                 'Flow શરૂ કરતાં પહેલાં lamp ચાલુ કરાય છે; થોડી સેકન્ડનો contact time પૂરતો dose આપે છે.',
                 'Treated પાણી બહાર નીકળે છે. Quartz sleeve નિયમિત સાફ થાય છે અને lampના કલાક નોંધાય છે.'),
        h4('કેમ green technique કહેવાય'),
        bullets('કોઈ chemical dose થતું નથી, એટલે trihalomethane જેવું harmful by-product બનતું નથી.',
                'પાણીનો taste, રંગ કે ગંધ બદલાતાં નથી.',
                'Chemical સાચવવાની, લઈ જવાની કે નિકાલ કરવાની જરૂર નથી — ફક્ત electricity વપરાય છે.',
                'Corrosive chemical ન હોવાથી કામ કરવું સુરક્ષિત છે.'),
        h4('મર્યાદાઓ'),
        p('UV પછી પાણીમાં <b>residual protection</b> રહેતું નથી: treatment પછી પાણી સંગ્રહ કરીએ તો bacteria '
          'ફરી વધી શકે. Turbidity અને રંગ UVને રોકે છે, એટલે પાણી સાફ હોવું જોઈએ. Lamp જૂની થતાં output '
          'ઘટે છે, એટલે 8,000–9,000 કલાકે lamp બદલાય છે.'),
    ),
))

Q1['cards'].append(dict(
    number='Q.1 (c)', marks=7, q='Explain Lime soda process (Hot &Cold) for water softening.',
    en=join(
        h4('Purpose and principle'),
        p('<b>Lime–soda softening</b> removes carbonate as well as non-carbonate hardness by precipitating '
          'Ca and Mg as insoluble compounds. <b>Lime Ca(OH)<sub>2</sub></b> handles the bicarbonate hardness '
          'and the magnesium, and <b>soda ash Na<sub>2</sub>CO<sub>3</sub></b> handles the sulphate and '
          'chloride hardness.'),
        p('The precipitate settles as sludge, the clear water is filtered, and the hardness falls to about '
          '30–50 ppm in the cold process and 15–25 ppm in the hot process.'),
        h4('Reactions'),
        work('Ca(HCO3)2 + Ca(OH)2 → 2CaCO3↓ + 2H2O   (carbonate hardness removed by lime)',
             'Mg(HCO3)2 + 2Ca(OH)2 → Mg(OH)2↓ + 2CaCO3↓ + 2H2O',
             'CaSO4 + Na2CO3 → CaCO3↓ + Na2SO4   (non-carbonate hardness removed by soda)',
             'CaCl2 + Na2CO3 → CaCO3↓ + 2NaCl',
             'MgSO4 + Ca(OH)2 → Mg(OH)2↓ + CaSO4   (the CaSO4 formed is again removed by soda)'),
        figure(fig.lime_soda(True), 'Fig. 1.3 · Cold lime–soda softener: mixer, settling tank and sand filter.'),
        h4('Construction — part and purpose'),
        table(['Part', 'Purpose'], [
            ['Chemical mixer with slow stirrer', 'mixes raw water with lime and soda slurry so the reaction starts'],
            ['Flocculation and settling tank', 'gives time for the precipitate to grow into flocs and settle as sludge'],
            ['Sludge blow-down line', 'draws off the CaCO<sub>3</sub> and Mg(OH)<sub>2</sub> sludge from the bottom'],
            ['Pressure sand filter', 'retains the fine floc that did not settle'],
            ['Soft-water storage tank', 'holds treated water for boiler or process use'],
        ]),
        h4('Working — step and reason'),
        steps(('Step 1', 'Raw water enters the chemical mixer. Lime and soda doses are fixed from the titrated '
                         'hardness of that water — a slight excess of lime raises the pH and helps the floc form.'),
              ('Step 2', 'The mixture passes to the settling chamber, where the stirrer speed is reduced so '
                         'that CaCO<sub>3</sub> and Mg(OH)<sub>2</sub> particles grow and settle.'),
              ('Step 3', 'Sludge is blown down at intervals. The clear overflow goes to the pressure sand filter.'),
              ('Step 4', 'Filtered soft water is stored. Residual hardness 30–50 ppm is normal for this process.')),
        h4('Cold and hot process compared'),
        table(['Point', 'Cold lime–soda', 'Hot lime–soda'], [
            ['Temperature', '20–30 °C', '90–110 °C'],
            ['Reaction speed', 'slow, needs a big tank', 'fast, smaller tank is enough'],
            ['Residual hardness', 'about 30–50 ppm', 'about 15–25 ppm'],
            ['Sludge', 'bulky, holds more water', 'dense, easy to filter'],
            ['Use', 'general plant and process water', 'boiler feed water'],
        ]),
        h4('Advantages and limitations'),
        bullets('Cheap chemicals and simple equipment; hardness is reduced without costly resin.',
                'The dose can be corrected every shift from the analysis of the incoming water.',
                'Sludge disposal is the main cost, zero hardness is not possible, and excess lime can itself '
                'cause scale in the boiler — so the dose has to be controlled and tested.'),
    ),
    gu=join(
        h4('હેતુ અને સિદ્ધાંત'),
        p('<b>Lime–soda softening</b>માં Ca અને Mgને અદ્રાવ્ય સંયોજન તરીકે અલગ કરીને carbonate અને '
          'non-carbonate બંને hardness દૂર કરાય છે. <b>Lime Ca(OH)<sub>2</sub></b> bicarbonate hardness અને '
          'magnesium સંભાળે છે, ને <b>soda ash Na<sub>2</sub>CO<sub>3</sub></b> sulphate તથા chloride hardness.'),
        p('Precipitate sludge તરીકે નીચે બેસે, ઉપરનું સાફ પાણી filter થાય, અને hardness cold processમાં '
          'લગભગ 30–50 ppm તથા hot processમાં 15–25 ppm સુધી આવે.'),
        h4('પ્રક્રિયાઓ'),
        work('Ca(HCO3)2 + Ca(OH)2 → 2CaCO3↓ + 2H2O   (carbonate hardness, limeથી)',
             'Mg(HCO3)2 + 2Ca(OH)2 → Mg(OH)2↓ + 2CaCO3↓ + 2H2O',
             'CaSO4 + Na2CO3 → CaCO3↓ + Na2SO4   (non-carbonate hardness, sodaથી)',
             'CaCl2 + Na2CO3 → CaCO3↓ + 2NaCl',
             'MgSO4 + Ca(OH)2 → Mg(OH)2↓ + CaSO4   (બનેલું CaSO4 ફરી sodaથી દૂર થાય)'),
        figure(fig.lime_soda(True), 'આકૃતિ 1.3 · Cold lime–soda softener: mixer, settling tank અને sand filter.'),
        h4('રચના — ભાગ અને કામ'),
        table(['ભાગ', 'કામ'], [
            ['Chemical mixer (ધીમા stirrer સાથે)', 'raw water સાથે lime–soda slurry ભેળવી reaction શરૂ કરવો'],
            ['Flocculation અને settling tank', 'floc મોટા થાય અને sludge તરીકે બેસે તે માટે સમય આપવો'],
            ['Sludge blow-down line', 'નીચે જમા થયેલો CaCO<sub>3</sub> અને Mg(OH)<sub>2</sub> sludge કાઢવો'],
            ['Pressure sand filter', 'બારીક floc પકડી રાખવો'],
            ['Soft-water tank', 'boiler કે process માટે soft પાણી સંગ્રહ કરવું'],
        ]),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1', 'Raw water chemical mixerમાં જાય. એ પાણીની titrated hardness પ્રમાણે lime અને sodaનો '
                         'dose ઠરાવાય — થોડી excess lime pH વધારે છે અને floc બનવામાં મદદ કરે છે.'),
              ('Step 2', 'પછી mixture settling chamberમાં જાય, જ્યાં stirrerની ઝડપ ઘટાડાય છે જેથી CaCO<sub>3</sub> '
                         'અને Mg(OH)<sub>2</sub>ના કણ મોટા થઈને બેસે.'),
              ('Step 3', 'Sludge સમયાંતરે blow-down થાય. ઉપરનું સાફ પાણી pressure sand filterમાં જાય.'),
              ('Step 4', 'Filter થયેલું soft પાણી tankમાં એકઠું થાય. 30–50 ppm residual hardness આ processમાં સામાન્ય છે.')),
        h4('Cold અને hot processની સરખામણી'),
        table(['મુદ્દો', 'Cold lime–soda', 'Hot lime–soda'], [
            ['Temperature', '20–30 °C', '90–110 °C'],
            ['Reactionની ઝડપ', 'ધીમી, મોટી tank જોઈએ', 'ઝડપી, નાની tank પૂરતી'],
            ['Residual hardness', 'લગભગ 30–50 ppm', 'લગભગ 15–25 ppm'],
            ['Sludge', 'જાડો, પાણી વધુ પકડે', 'ગાઢ, filter કરવો સહેલો'],
            ['ઉપયોગ', 'સામાન્ય plant–process પાણી', 'boiler feed water'],
        ]),
        h4('ફાયદા અને મર્યાદાઓ'),
        bullets('Chemical સસ્તાં અને equipment સાદું; મોંઘા resin વગર hardness ઘટે.',
                'આવતા પાણીના analysis પ્રમાણે દર shiftે dose સુધારી શકાય.',
                'Sludge નિકાલ મુખ્ય ખર્ચ છે, શૂન્ય hardness મળતી નથી, અને excess lime પોતે boilerમાં scale '
                'કરે — એટલે dose નિયંત્રિત રાખીને ટેસ્ટ કરવો પડે.'),
    ),
))

Q1['cards'].append(dict(
    number='Q.1 (c)', marks=7, tag='OR', q='Explain Ion exchange process for water softening.',
    en=join(
        h4('Principle'),
        p('<b>Ion exchange</b> softens water without precipitating anything. The hardness ions are held on a '
          'resin and replaced by ions that cause no hardness. A cation resin in <b>H<sup>+</sup> form</b> '
          'gives <b>demineralised water</b> when followed by an anion resin; a cation resin in '
          '<b>Na<sup>+</sup> form</b> gives soft water.'),
        h4('Construction — part and purpose'),
        table(['Part', 'Purpose'], [
            ['Cation-exchange column', 'R–H resin; exchanges Ca<sup>2+</sup> and Mg<sup>2+</sup> for H<sup>+</sup>'],
            ['Anion-exchange column', 'R–OH resin; exchanges Cl<sup>−</sup> and SO<sub>4</sub><sup>2−</sup> for OH<sup>−</sup>'],
            ['Degasser', 'removes the CO<sub>2</sub> released when H<sup>+</sup> meets bicarbonate'],
            ['Acid and alkali tanks', 'regenerate the two resins'],
            ['Flow, pH and conductivity meters', 'watch the quality of the outgoing water'],
        ]),
        figure(fig.ion_exchange(), 'Fig. 1.4 · Two-bed ion-exchange (demineralisation) plant.'),
        h4('Working — step and reason'),
        steps(('Service', 'Hard water flows down the cation bed. Ca<sup>2+</sup> and Mg<sup>2+</sup> are held by the '
                          'resin and H<sup>+</sup> is released: 2R–H + Ca<sup>2+</sup> → R<sub>2</sub>–Ca + 2H<sup>+</sup>.'),
              ('Anion bed', 'The acidic water then meets R–OH resin, which takes the anions and releases OH<sup>−</sup>; '
                            'H<sup>+</sup> and OH<sup>−</sup> combine to give water.'),
              ('Exhaustion', 'When the outlet conductivity rises or hardness appears, the resin is spent.'),
              ('Backwash', 'Upward water flow loosens the bed and washes out dirt.'),
              ('Regeneration', 'Cation bed with dilute HCl or H<sub>2</sub>SO<sub>4</sub>, anion bed with NaOH. '
                               'The waste carries the removed Ca, Mg and anions.'),
              ('Rinse', 'Slow and fast rinse remove the regenerant before service starts again.')),
        h4('Advantages, limitations, use'),
        bullets('Gives almost zero hardness; the two-bed form gives demineralised water for high-pressure '
                'boilers, laboratories and electronics.',
                'Compact, automatic, and no sludge handling — unlike lime–soda.',
                'Resins and chemicals are costly; turbidity, chlorine and organics foul the resin, so '
                'pre-treatment is necessary; the regeneration effluent has to be neutralised.'),
    ),
    gu=join(
        h4('સિદ્ધાંત'),
        p('<b>Ion exchange</b>માં કોઈ precipitate બનતું નથી. Hardness આપતા ions resin પર પકડાય છે અને તેમની '
          'જગ્યાએ hardness ન આપતા ions પાણીમાં જાય છે. <b>H<sup>+</sup> form</b>નું cation resin પછી anion '
          'resin સાથે <b>demineralised water</b> આપે છે; <b>Na<sup>+</sup> form</b>નું cation resin soft water આપે છે.'),
        h4('રચના — ભાગ અને કામ'),
        table(['ભાગ', 'કામ'], [
            ['Cation-exchange column', 'R–H resin; Ca<sup>2+</sup> અને Mg<sup>2+</sup> સામે H<sup>+</sup> આપે'],
            ['Anion-exchange column', 'R–OH resin; Cl<sup>−</sup> અને SO<sub>4</sub><sup>2−</sup> સામે OH<sup>−</sup> આપે'],
            ['Degasser', 'H<sup>+</sup> અને bicarbonate મળવાથી બનતો CO<sub>2</sub> કાઢે'],
            ['Acid અને alkali tank', 'બંને resinની regeneration માટે'],
            ['Flow, pH અને conductivity meter', 'બહાર જતા પાણીની ગુણવત્તા ચેક કરે'],
        ]),
        figure(fig.ion_exchange(), 'આકૃતિ 1.4 · Two-bed ion-exchange (demineralisation) plant.'),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Service', 'Hard પાણી cation bedમાં નીચે વહે. Ca<sup>2+</sup> અને Mg<sup>2+</sup> resin પર રહે અને '
                          'H<sup>+</sup> પાણીમાં જાય: 2R–H + Ca<sup>2+</sup> → R<sub>2</sub>–Ca + 2H<sup>+</sup>.'),
              ('Anion bed', 'પછી acidic પાણી R–OH resin પાસે જાય, જે anions લે અને OH<sup>−</sup> આપે; H<sup>+</sup> '
                            'અને OH<sup>−</sup> મળીને પાણી બને.'),
              ('Exhaustion', 'Outletની conductivity વધે કે hardness દેખાય ત્યારે resin થાકેલું ગણાય.'),
              ('Backwash', 'ઉપરની તરફ પાણી વહાવીને bed ઢીલું કરાય અને ગряж ધોવાય.'),
              ('Regeneration', 'Cation bed ને dilute HCl કે H<sub>2</sub>SO<sub>4</sub>થી, anion bed ને NaOHથી '
                               'regenerate કરાય. Wasteમાં દૂર થયેલા Ca, Mg અને anions જાય.'),
              ('Rinse', 'Service શરૂ કરતાં પહેલાં slow અને fast rinseથી regenerant કાઢાય.')),
        h4('ફાયદા, મર્યાદાઓ, ઉપયોગ'),
        bullets('લગભગ શૂન્ય hardness મળે; two-bed system high-pressure boiler, laboratory અને electronics માટે '
                'demineralised water આપે.',
                'Compact, automatic, અને lime–soda જેવો sludge સાચવવો ન પડે.',
                'Resin અને chemical મોંઘા; turbidity, chlorine કે organic પ્રમાણ વધુ હોય તો resin બગડે, એટલે '
                'pre-treatment જરૂરી; regeneration effluent neutralise કરવું પડે.'),
    ),
))

# ---------------------------------------------------------------- Q2
Q2 = {
    'title_en': 'Q2 · Hardness of water and softening methods',
    'title_gu': 'પ્ર.2 · પાણીની hardness અને soft કરવાની રીતો',
    'cards': [],
}

Q2['cards'].append(dict(
    number='Q.2 (a)', marks=3, q='Differentiate soft water & hard water.',
    en=join(
        h4('Difference'),
        table(['Point', 'Soft water', 'Hard water'], [
            ['Lather with soap', 'gives lather easily', 'gives lather only with much more soap'],
            ['Cause', 'little or no dissolved Ca and Mg', 'Ca and Mg salts in solution'],
            ['Hardness value', 'below about 50 ppm as CaCO<sub>3</sub>', 'above about 100 ppm as CaCO<sub>3</sub>'],
            ['With soap', 'no scum', 'insoluble scum forms'],
            ['In a boiler', 'no scale', 'CaCO<sub>3</sub> and CaSO<sub>4</sub> scale'],
            ['Typical source', 'rain water, soft river water', 'bore well, limestone ground water'],
        ]),
        p('<b>Quick test:</b> shake a sample with soap solution. Hard water needs far more soap before a '
          'lasting lather appears, and the water turns cloudy with scum.'),
    ),
    gu=join(
        h4('તફાવત'),
        table(['મુદ્દો', 'Soft water', 'Hard water'], [
            ['Soap સાથે lather', 'સહેલાઈથી lather આપે', 'ઘણું વધુ soap વાપર્યા પછી lather આપે'],
            ['કારણ', 'Ca અને Mg લગભગ નહીં', 'Ca અને Mgના ક્ષાર દ્રાવ્ય સ્થિતિમાં'],
            ['Hardnessનું મૂલ્ય', 'CaCO<sub>3</sub> તરીકે લગભગ 50 ppmથી ઓછી', 'લગભગ 100 ppmથી વધુ'],
            ['Soap સાથે', 'scum નહીં', 'અદ્રાવ્ય scum બને'],
            ['Boilerમાં', 'scale નહીં', 'CaCO<sub>3</sub> અને CaSO<sub>4</sub>નો scale'],
            ['સામાન્ય સ્રોત', 'વરસાદનું પાણી, soft નદીનું પાણી', 'bore well, ચૂનાવાળી જમીનનું પાણી'],
        ]),
        p('<b>ઝડપી ચેક:</b> soap solution સાથે shake કરો. Hard waterમાં લાંબો lather ટકે તે પહેલાં ઘણું વધુ '
          'soap લાગે અને પાણી scumથી ધૂંધળું થાય.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (b)', marks=4, q='Explain Causes of hardness in water.',
    en=join(
        h4('How water becomes hard'),
        p('Rain water is naturally soft. Water becomes hard while it seeps through soil and rock, because it '
          'dissolves the calcium and magnesium salts present there.'),
        h4('Causes, one by one'),
        numbered('<b>Limestone and chalk (CaCO<sub>3</sub>):</b> water containing dissolved CO<sub>2</sub> converts '
                 'it into soluble Ca(HCO<sub>3</sub>)<sub>2</sub>. This is carbonate (temporary) hardness.',
                 '<b>Dolomite (CaCO<sub>3</sub>·MgCO<sub>3</sub>):</b> contributes calcium and magnesium together; '
                 'dolomitic ground water is the hardest in practice.',
                 '<b>Gypsum (CaSO<sub>4</sub>) and Epsom salt (MgSO<sub>4</sub>):</b> dissolve directly and give '
                 'non-carbonate (permanent) hardness, which boiling cannot remove.',
                 '<b>Calcium and magnesium chlorides:</b> highly soluble salts found in coastal and industrial '
                 'ground water.',
                 '<b>Human activity:</b> sewage and fertiliser runoff, and repeated evaporation of cooling water, '
                 'concentrate the salts and raise the hardness of surface water.'),
        h4('Types of hardness and how they are removed'),
        table(['Type', 'Salts responsible', 'Removed by'], [
            ['Carbonate (temporary)', 'Ca(HCO<sub>3</sub>)<sub>2</sub>, Mg(HCO<sub>3</sub>)<sub>2</sub>',
             'boiling, lime treatment'],
            ['Non-carbonate (permanent)', 'CaSO<sub>4</sub>, MgSO<sub>4</sub>, CaCl<sub>2</sub>',
             'soda, zeolite, ion exchange'],
        ]),
    ),
    gu=join(
        h4('પાણી hard કેમ બને છે'),
        p('વરસાદનું પાણી કુદરતી રીતે soft હોય છે. એ જ પાણી જમીન અને ખડકમાંથી ઝીરવતું જાય ત્યારે ત્યાંના Ca અને '
          'Mgના ક્ષાર ઓગળી જવાથી hard બને છે.'),
        h4('કારણો, એક એક કરીને'),
        numbered('<b>Limestone અને chalk (CaCO<sub>3</sub>):</b> પાણીમાં ઓગળેલો CO<sub>2</sub> એને દ્રાવ્ય '
                 'Ca(HCO<sub>3</sub>)<sub>2</sub>માં ફેરવે — આ carbonate (temporary) hardness.',
                 '<b>Dolomite (CaCO<sub>3</sub>·MgCO<sub>3</sub>):</b> calcium અને magnesium બંને આપે; dolomiteવાળું '
                 'ground water વ્યવહારમાં સૌથી hard હોય.',
                 '<b>Gypsum (CaSO<sub>4</sub>) અને Epsom salt (MgSO<sub>4</sub>):</b> સીધા ઓગળે અને non-carbonate '
                 '(permanent) hardness આપે, જે ઉકાળવાથી દૂર થતી નથી.',
                 '<b>Calcium અને magnesium chloride:</b> ખૂબ દ્રાવ્ય ક્ષાર; દરિયાકિનારાના અને ઔદ્યોગિક ground waterમાં મળે.',
                 '<b>માનવીય કારણો:</b> sewage અને fertiliserનું runoff તથા cooling water વારંવાર બાષ્પ થવાથી ક્ષાર '
                 'ગાઢા થાય અને surface waterની hardness વધે.'),
        h4('Hardnessનાં પ્રકાર અને દૂર કરવાની રીત'),
        table(['પ્રકાર', 'જવાબદાર ક્ષાર', 'કેવી રીતે દૂર થાય'], [
            ['Carbonate (temporary)', 'Ca(HCO<sub>3</sub>)<sub>2</sub>, Mg(HCO<sub>3</sub>)<sub>2</sub>',
             'ઉકાળવાથી, lime treatmentથી'],
            ['Non-carbonate (permanent)', 'CaSO<sub>4</sub>, MgSO<sub>4</sub>, CaCl<sub>2</sub>',
             'soda, zeolite, ion exchange'],
        ]),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (c)', marks=7, q='Explain Zeolite process for water softening.',
    en=join(
        h4('Principle'),
        p('In the <b>zeolite process</b> hard water percolates through a bed of <b>sodium zeolite</b> '
          '(permutit, Na<sub>2</sub>O·Al<sub>2</sub>O<sub>3</sub>·nSiO<sub>2</sub>·xH<sub>2</sub>O). The '
          'Ca<sup>2+</sup> and Mg<sup>2+</sup> ions of the water are exchanged for the Na<sup>+</sup> ions held '
          'by the zeolite, so the outlet water is soft.'),
        h4('Reactions'),
        work('Ca(HCO3)2 + Na2–zeolite → Ca–zeolite + 2NaHCO3',
             'MgSO4 + Na2–zeolite → Mg–zeolite + Na2SO4',
             'Regeneration: Ca–zeolite + 2NaCl → Na2–zeolite + CaCl2'),
        figure(fig.zeolite(), 'Fig. 2.1 · Zeolite softener with brine regeneration.'),
        h4('Construction — part and purpose'),
        table(['Part', 'Purpose'], [
            ['Steel vessel with zeolite bed', 'the exchange medium; bed depth 1–1.5 m on a gravel support'],
            ['Inlet distributor', 'spreads the hard water evenly over the bed'],
            ['Supporting gravel layer', 'stops the zeolite from washing out with the treated water'],
            ['Brine tank and pump', 'NaCl solution for regeneration'],
            ['Soft-water outlet with hardness test point', 'delivers water and lets the outlet be checked'],
            ['Backwash and drain lines', 'clean the bed and carry away the regeneration waste'],
        ]),
        h4('Working — step and reason'),
        steps(('Service', 'Hard water enters at the top and flows down. The exchange is fast, so the flow is kept '
                          'at about 10–15 bed volumes per hour to give enough contact time.'),
              ('Soft water', 'Water leaving the bed has hardness below about 10 ppm as CaCO<sub>3</sub>.'),
              ('Exhaustion', 'After a fixed volume the bed is saturated and hardness appears in the outlet; the run '
                             'is stopped.'),
              ('Backwash', 'Upward flow loosens the bed and removes suspended dirt, so the brine can reach every grain.'),
              ('Regeneration', '10 % NaCl brine is passed slowly; Na<sup>+</sup> replaces the Ca<sup>2+</sup> and '
                               'Mg<sup>2+</sup> on the bed, and the waste carries CaCl<sub>2</sub> and MgCl<sub>2</sub>.'),
              ('Rinse', 'The bed is rinsed with soft water until chloride disappears from the outlet, then service restarts.')),
        h4('Advantages, limitations, use'),
        bullets('Very low hardness, compact unit, no sludge, low running cost, and the cycle can be made automatic.',
                'Turbid water blocks the bed; iron and manganese poison the zeolite; the waste brine must be disposed '
                'of; and it cannot remove anions, so the water is soft but not demineralised.'),
        p('Use: boiler feed, laundry, textile dyeing and cooling-water make-up, wherever hardness below about '
          '10 ppm is required.'),
    ),
    gu=join(
        h4('સિદ્ધાંત'),
        p('<b>Zeolite process</b>માં hard પાણી <b>sodium zeolite</b> (permutit, '
          'Na<sub>2</sub>O·Al<sub>2</sub>O<sub>3</sub>·nSiO<sub>2</sub>·xH<sub>2</sub>O)ની bedમાંથી ઝીરે છે. '
          'પાણીના Ca<sup>2+</sup> અને Mg<sup>2+</sup> સામે zeolite પર રહેલા Na<sup>+</sup> આવે છે, એટલે નીકળતું '
          'પાણી soft થાય છે.'),
        h4('પ્રક્રિયાઓ'),
        work('Ca(HCO3)2 + Na2–zeolite → Ca–zeolite + 2NaHCO3',
             'MgSO4 + Na2–zeolite → Mg–zeolite + Na2SO4',
             'Regeneration: Ca–zeolite + 2NaCl → Na2–zeolite + CaCl2'),
        figure(fig.zeolite(), 'આકૃતિ 2.1 · Zeolite softener અને brine regeneration.'),
        h4('રચના — ભાગ અને કામ'),
        table(['ભાગ', 'કામ'], [
            ['Steel vesselમાં zeolite bed', 'exchange માધ્યમ; gravel પર 1–1.5 m જાડી bed'],
            ['Inlet distributor', 'hard પાણી bed પર સરખું ફેલાવે'],
            ['Supporting gravel', 'zeolite પાણી સાથે વહી ન જાય તે રોકે'],
            ['Brine tank અને pump', 'regeneration માટે NaClનું દ્રાવણ'],
            ['Soft-water outlet અને hardness test point', 'પાણી આપે અને outlet ચેક કરવા દે'],
            ['Backwash અને drain line', 'bed સાફ કરે અને regeneration waste કાઢે'],
        ]),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Service', 'Hard પાણી ઉપરથી નીચે વહે. Exchange ઝડપી હોવાથી પૂરતો contact time મળે એ માટે flow '
                          'લગભગ 10–15 bed volume પ્રતિ કલાક રાખાય.'),
              ('Soft water', 'Bedમાંથી નીકળતા પાણીની hardness CaCO<sub>3</sub> તરીકે લગભગ 10 ppmથી ઓછી રહે.'),
              ('Exhaustion', 'થોડું volume પસાર થયા પછી bed ભરાય અને outletમાં hardness દેખાય, એટલે run બંધ કરાય.'),
              ('Backwash', 'ઉપરની તરફ flowથી bed ઢીલું થાય અને તરતા કણ નીકળે, જેથી brine દરેક કણ સુધી પહોંચે.'),
              ('Regeneration', '10 % NaCl brine ધીમે પસાર થાય; Na<sup>+</sup> bed પરના Ca<sup>2+</sup> અને '
                               'Mg<sup>2+</sup>ની જગ્યાએ બેસે, અને waste સાથે CaCl<sub>2</sub> તથા MgCl<sub>2</sub> જાય.'),
              ('Rinse', 'Outletમાંથી chloride પૂરો નીકળે ત્યાં સુધી soft પાણીથી rinse કરીને service ફરી શરૂ કરાય.')),
        h4('ફાયદા, મર્યાદાઓ, ઉપયોગ'),
        bullets('Hardness ખૂબ ઓછી, unit compact, sludge નહીં, running cost ઓછો અને cycle automatic કરી શકાય.',
                'Turbid પાણી bed બ્લોક કરે; iron અને manganese zeolite બગાડે; waste brineનો નિકાલ કરવો પડે; અને '
                'anions દૂર થતા નથી, એટલે પાણી soft થાય પણ demineralised નહીં.'),
        p('ઉપયોગ: boiler feed, laundry, textile dyeing અને cooling-water make-up — જ્યાં લગભગ 10 ppmથી ઓછી '
          'hardness જોઈએ.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (a)', marks=3, tag='OR', q='List characteristics of drinking water.',
    en=join(
        h4('Characteristics of drinking water'),
        table(['Characteristic', 'Acceptable value'], [
            ['pH', '6.5 – 8.5'],
            ['Turbidity', 'below 5 NTU, ideally about 1 NTU'],
            ['Total hardness', 'below 300 ppm as CaCO<sub>3</sub>'],
            ['Total dissolved solids', 'below 500 ppm'],
            ['Coliform bacteria', 'zero per 100 mL'],
            ['Residual chlorine at the tap', '0.2 – 0.5 ppm'],
            ['Fluoride', 'about 1 ppm (0.6 – 1.2)'],
            ['Nitrate', 'below 45 ppm'],
            ['Taste and odour', 'no objectionable taste or smell'],
        ]),
        p('It must also be free of visible colour, suspended matter, and toxic metals such as lead and arsenic. '
          'These values follow the usual IS 10500 drinking-water limits.'),
    ),
    gu=join(
        h4('પીવાના પાણીની લાક્ષણિકતાઓ'),
        table(['લાક્ષણિકતા', 'સ્વીકાર્ય મૂલ્ય'], [
            ['pH', '6.5 – 8.5'],
            ['Turbidity', '5 NTUથી ઓછી, લગભગ 1 NTU શ્રેષ્ઠ'],
            ['Total hardness', 'CaCO<sub>3</sub> તરીકે 300 ppmથી ઓછી'],
            ['Total dissolved solids', '500 ppmથી ઓછા'],
            ['Coliform bacteria', '100 mLમાં શૂન્ય'],
            ['Tap પર residual chlorine', '0.2 – 0.5 ppm'],
            ['Fluoride', 'લગભગ 1 ppm (0.6 – 1.2)'],
            ['Nitrate', '45 ppmથી ઓછું'],
            ['Taste અને ગંધ', 'અણગમતો સ્વાદ કે ગંધ નહીં'],
        ]),
        p('ઉપરાંત પાણીમાં દેખાતો રંગ, તરતા કણ અને lead–arsenic જેવી જહેરીલી ધાતુ ન હોવી જોઈએ. આ મૂલ્યો '
          'સામાન્ય IS 10500 પીવાના પાણીની મર્યાદા પ્રમાણે છે.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (b)', marks=4, tag='OR', q='List use of various utilities in chemical plant.',
    en=join(
        h4('Utilities and their use'),
        table(['Utility', 'Main use in a chemical plant'], [
            ['Water — process, cooling, boiler feed', 'reaction medium, washing and extraction, cooling-tower make-up, '
                                                     'steam generation'],
            ['Steam — LP / MP / HP', 'jacket and coil heating of reactors, reboilers of distillation columns, '
                                     'evaporators, dryers, line tracing'],
            ['Compressed air — instrument and plant', 'pneumatic control valves and instruments, air motors, cleaning, '
                                                      'oxidation air'],
            ['Blower air', 'combustion air for boilers and furnaces, ventilation, aeration of effluent treatment'],
            ['Nitrogen — inert gas', 'tank blanketing, purging before start-up and maintenance, inert atmosphere for '
                                     'flammable solvents'],
            ['Refrigeration — chilled water or brine', 'condensing low-boiling vapours, chilling, cold storage'],
            ['Electricity and fuel', 'pump and compressor drives, furnaces, lighting'],
            ['Effluent treatment', 'safe disposal of waste water and compliance with the consent limits'],
        ]),
        h4('Why they are called utilities'),
        p('They are services produced in a central utility block and distributed to every process unit. No single '
          'product can be made without them, yet they are not the product itself — that is exactly what the word '
          'utility means in a plant.'),
    ),
    gu=join(
        h4('Utilities અને તેનો ઉપયોગ'),
        table(['Utility', 'કેમિકલ પ્લાન્ટમાં મુખ્ય ઉપયોગ'], [
            ['પાણી — process, cooling, boiler feed', 'reaction medium, washing–extraction, cooling tower make-up, '
                                                     'steam બનાવવા'],
            ['Steam — LP / MP / HP', 'reactorના jacket–coil heating, distillation columnનો reboiler, evaporator, '
                                     'dryer, line tracing'],
            ['Compressed air — instrument અને plant', 'pneumatic control valve–instrument, air motor, સફાઈ, oxidation air'],
            ['Blower air', 'boiler–furnaceનું combustion air, ventilation, effluent treatmentમાં aeration'],
            ['Nitrogen — inert gas', 'tank blanketing, start-up–maintenance પહેલાં purging, flammable solvent માટે '
                                     'inert વાતાવરણ'],
            ['Refrigeration — chilled water કે brine', 'નીચા boiling pointવાળા vapour condense કરવા, chilling, cold storage'],
            ['Electricity અને fuel', 'pump–compressor ચલાવવા, furnace, lighting'],
            ['Effluent treatment', 'waste waterનો સુરક્ષિત નિકાલ અને consent limit પાળવા'],
        ]),
        h4('એમને utilities કેમ કહેવાય'),
        p('આ સેવાઓ કેન્દ્રીય utility blockમાં બને છે અને દરેક process unit સુધી પહોંચે છે. એમના વગર એક પણ '
          'product બની શકે નહીં, છતાં એ product નથી — plantમાં "utility" શબ્દનો અર્થ એ જ છે.'),
    ),
))

Q2['cards'].append(dict(
    number='Q.2 (c)', marks=7, tag='OR', q='Explain Phosphate process for water softening.',
    en=join(
        h4('Principle'),
        p('In the <b>phosphate process</b> sodium phosphate (Na<sub>3</sub>PO<sub>4</sub>) or sodium '
          'hexametaphosphate (calgon) is dosed into the water. Calcium and magnesium phosphates are almost '
          'insoluble, so the hardness ions are precipitated and removed.'),
        p('The residual hardness is only about <b>5 ppm</b> — the lowest of all the chemical softening processes — '
          'which is why it is used where a boiler must stay absolutely scale-free.'),
        h4('Reactions'),
        work('3Ca(HCO3)2 + 2Na3PO4 → Ca3(PO4)2↓ + 6NaHCO3',
             '3CaSO4 + 2Na3PO4 → Ca3(PO4)2↓ + 3Na2SO4',
             '3MgSO4 + 2Na3PO4 → Mg3(PO4)2↓ + 3Na2SO4'),
        figure(fig.phosphate(), 'Fig. 2.2 · Phosphate softening: dosing, reaction tank, settling and filtration.'),
        h4('Construction — part and purpose'),
        table(['Part', 'Purpose'], [
            ['Dosing tank with metering pump', 'adds Na<sub>3</sub>PO<sub>4</sub> in proportion to the measured hardness'],
            ['Reaction cum heating tank (70–100 °C)', 'gives a fast reaction and a dense, settleable precipitate'],
            ['Clarifier / settling tank', 'separates Ca<sub>3</sub>(PO<sub>4</sub>)<sub>2</sub> and '
                                          'Mg<sub>3</sub>(PO<sub>4</sub>)<sub>2</sub> sludge'],
            ['Filter', 'retains the fine phosphate floc'],
            ['Sludge sump', 'collects the sludge for disposal'],
        ]),
        h4('Working — step and reason'),
        steps(('Step 1', 'The hardness of the incoming water is measured and the phosphate dose is set from it; a '
                         'small excess keeps the residual low.'),
              ('Step 2', 'Water and phosphate are mixed in the reaction tank. Heating to 70–100 °C makes the '
                         'precipitate dense and quick to settle.'),
              ('Step 3', 'The mixture is held in the clarifier so that the phosphate sludge settles at the bottom.'),
              ('Step 4', 'Sludge is drawn off; the clear overflow is filtered and used as boiler feed water.')),
        h4('Advantages and limitations'),
        bullets('Lowest residual hardness, so practically no scale forms on the boiler tubes.',
                'In a boiler the phosphate also acts as an internal treatment: any hardness that enters later is '
                'converted into loose sludge that can be blown down instead of forming hard scale.',
                'The dose can be linked to the feed-pump stroke, so operation is simple and automatic.',
                'The chemical is costly, sludge disposal is a problem, and a large excess of phosphate causes '
                'foaming and caustic embrittlement of the boiler metal.'),
        p('Use: mainly internal treatment of boiler feed water and small high-purity water systems.'),
    ),
    gu=join(
        h4('સિદ્ધાંત'),
        p('<b>Phosphate process</b>માં પાણીમાં sodium phosphate (Na<sub>3</sub>PO<sub>4</sub>) કે sodium '
          'hexametaphosphate (calgon) dose કરાય છે. Calcium અને magnesium phosphate લગભગ અદ્રાવ્ય હોવાથી '
          'hardness આપતા ions precipitate થઈને દૂર થાય છે.'),
        p('Residual hardness ફક્ત લગભગ <b>5 ppm</b> રહે — બધી chemical પદ્ધતિઓમાં સૌથી ઓછી — એટલે જ જ્યાં '
          'boilerમાં scale બિલકુલ ન જોઈએ ત્યાં વપરાય છે.'),
        h4('પ્રક્રિયાઓ'),
        work('3Ca(HCO3)2 + 2Na3PO4 → Ca3(PO4)2↓ + 6NaHCO3',
             '3CaSO4 + 2Na3PO4 → Ca3(PO4)2↓ + 3Na2SO4',
             '3MgSO4 + 2Na3PO4 → Mg3(PO4)2↓ + 3Na2SO4'),
        figure(fig.phosphate(), 'આકૃતિ 2.2 · Phosphate softening: dosing, reaction tank, settling અને filtration.'),
        h4('રચના — ભાગ અને કામ'),
        table(['ભાગ', 'કામ'], [
            ['Dosing tank અને metering pump', 'માંપેલી hardness પ્રમાણે Na<sub>3</sub>PO<sub>4</sub> ઉમેરે'],
            ['Reaction cum heating tank (70–100 °C)', 'ઝડપી reaction અને ગાઢ, જલદી બેસતું precipitate આપે'],
            ['Clarifier / settling tank', 'Ca<sub>3</sub>(PO<sub>4</sub>)<sub>2</sub> અને '
                                          'Mg<sub>3</sub>(PO<sub>4</sub>)<sub>2</sub> sludge અલગ કરે'],
            ['Filter', 'બારીક phosphate floc પકડે'],
            ['Sludge sump', 'sludge નિકાલ માટે એકઠો કરે'],
        ]),
        h4('કાર્ય — સ્ટેપ અને કારણ'),
        steps(('Step 1', 'આવતા પાણીની hardness માપીને phosphateનો dose ઠરાવાય; થોડી excess રાખવાથી residual ઓછી રહે.'),
              ('Step 2', 'Reaction tankમાં પાણી અને phosphate ભેળવાય. 70–100 °C સુધી ગરમ કરવાથી precipitate ગાઢ '
                         'બને અને જલદી બેસે.'),
              ('Step 3', 'Mixture clarifierમાં રોકાય, જેથી phosphate sludge નીચે જમા થાય.'),
              ('Step 4', 'Sludge કાઢાય; ઉપરનું સાફ પાણી filter કરીને boiler feed તરીકે વપરાય.')),
        h4('ફાયદા અને મર્યાદાઓ'),
        bullets('સૌથી ઓછી residual hardness, એટલે boiler tube પર scale લગભગ ન બને.',
                'Boilerમાં phosphate internal treatment તરીકે પણ કામ કરે: પછી અંદર આવેલી hardness સહેલાઈથી '
                'blow-down થઈ શકે એવા ઢીલા sludgeમાં ફેરવાય, સખત scale ન બને.',
                'Feed pumpના stroke સાથે dose જોડી શકાય, એટલે operation સાદું અને automatic રહે.',
                'Chemical મોંઘું, sludge નિકાલ મુશ્કેલ, અને ઘણું excess phosphate હોય તો foaming તથા '
                'caustic embrittlement થાય.'),
        p('ઉપયોગ: મુખ્યત્વે boiler feed waterની internal treatment અને નાની ઊંચી શુદ્ધતાવાળી system માટે.'),
    ),
))
