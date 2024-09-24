import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import os
import base64

dash.register_page(__name__,path='/khoka_conclusions')

pdf_filename = './assets/metabolitos.pdf'
encoded_pdf = base64.b64encode(open(pdf_filename, 'rb').read()).decode('utf-8')

# Define the navigation bar with the dropdown menu

portada =  dbc.Row(
        [
            html.Img(src="/assets/h_conclu.webp",style={"width": "100%",'marginTop':'3%','marginBottom':'3   %'},className="center-image"),
        ]
                )

conclusiones = dbc.Container(
    dbc.Row([
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("CONCLUSIONES", className="body-title-green"), 
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Button('DESCARGAR MAPA DE METABOLITOS', id='bt-descarga', n_clicks=0, className="boton-descarga"),
                dcc.Download(id="download-pdf"),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("El estudio de metabolitos en la hoja de coca",className="body-title-2",id="conclu_estudio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["A través de la historia, la humanidad ha reconocido y venerado diversas especies animales y vegetales como sagradas. En el reino vegetal, destaca un grupo de plantas que producen sustancias especializadas para protegerse del entorno: los alcaloides. Estos compuestos orgánicos naturales, que contienen al menos un átomo de nitrógeno en una configuración molecular única, pueden ejercer efectos profundos en el organismo humano, influyendo en la percepción y los estados de conciencia."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),


                html.Div(children=[
                    html.P("Las plantas han desarrollado ingeniosos mecanismos para aprovechar los elementos disponibles en su entorno, sintetizando sustancias exclusivas de cada especie. Este fascinante campo de estudio continúa revelando descubrimientos sorprendentes. Es particularmente admirable cómo las culturas ancestrales identificaron estas plantas y determinaron las condiciones óptimas para maximizar sus beneficios. Un ejemplo notable es el uso tradicional de la hoja de coca: al añadir cenizas de conchas marinas calcinadas y masticar la hoja durante un tiempo prolongado, se potencia la liberación y absorción de sus alcaloides."),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.P("Elementos fundamentales como el nitrógeno, el carbono y el oxígeno constituyen la base de la materia orgánica y son esenciales en las proteínas, que aportan estructura a los músculos y son indispensables en nuestra dieta. Sin embargo, en los alcaloides, el nitrógeno desempeña un papel diferente. Posee un par de electrones libres que no participan en enlaces químicos, confiriéndole propiedades básicas. Esta característica, compartida con otros elementos del grupo del nitrógeno en la tabla periódica, como el fósforo y el arsénico, hace que los alcaloides sean afines a sustancias ácidas, formando sales solubles en agua. Por el contrario, en soluciones alcalinas, los alcaloides son menos solubles."),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.P("Otra propiedad notable de los alcaloides es su afinidad por tejidos con alto contenido lipídico, como el cerebro y el sistema nervioso. Esta afinidad les permite atravesar barreras biológicas y ejercer efectos significativos en diversos sistemas del cuerpo, influyendo en funciones vitales y en los estados de conciencia."),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["Entre los alcaloides más conocidos se encuentran la cafeína, presente en el café y el té y consumida masivamente en todo el mundo; la morfina, utilizada como potente analgésico en medicina; y la nicotina, producida por el tabaco, que además de ser un eficaz insecticida, es responsable de la adicción asociada al consumo de tabaco. Muchos alcaloides tienen la capacidad de generar dependencia cuando se consumen de forma recurrente. La heroína, derivada de la morfina, fue inicialmente empleada con fines terapéuticos, pero su uso médico se descontinuó rápidamente debido a su alto potencial adictivo."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["Dentro de los alcaloides existe un subgrupo llamado alcaloides tropanos, cuyo nombre proviene de la planta "
                          , html.Span("Atropa belladonna", className="italic-text"), 
                          ", de la cual se extraen la escopolamina y la atropina. Estas sustancias son conocidas por inducir estados de confusión, pérdida de voluntad, parálisis y, en dosis elevadas, pueden conducir a la muerte por fallo cardíaco."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["La hoja de coca contiene varios alcaloides tropanos, siendo la cocaína y la ecgonina los más prominentes. La cocaína tiene una historia extensa: fue el primer anestésico local descubierto, capaz de adormecer los nervios de la zona orofaríngea, resultando muy útil en cirugía. Aunque la cocaína suele acaparar la atención, la hoja de coca alberga otros alcaloides tropanos cuyos efectos aún no se comprenden plenamente. Además, contiene flavonoides y compuestos fenólicos que, en sinergia con los alcaloides, contribuyen a efectos como la reducción del hambre, el aumento de la vitalidad, la disminución del cansancio y el incremento de la concentración mental."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["Para profundizar en la riqueza química de la hoja de coca, ", 
                          html.Span("Khoka Project", className="italic-text"), " realizó un estudio comparativo de cuatro variedades: ", 
                          html.Span("Erythroxylum coca", className="italic-text"), " var. ", 
                          html.Span("coca", className="italic-text"), ", ",
                          html.Span("Erythroxylum coca", className="italic-text"), " var. ", 
                          html.Span("ipadu", className="italic-text"), ", ",
                          html.Span("Erythroxylum novogranatense", className="italic-text"), " var. ", 
                          html.Span("novogranatense", className="italic-text"), " y ", 
                          html.Span("Erythroxylum novogranatense", className="italic-text"), " var. ", 
                          html.Span("truxillense", className="italic-text"), ". Cada una de estas variedades exhibe un perfil único de metabolitos secundarios, reflejando la diversidad y complejidad de sus procesos bioquímicos."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["La cocaína está presente en todas las variedades, alcanzando su concentración máxima en E. coca var. coca. La ecgonina predomina en E. coca var. ipadu, originaria de la Amazonía, lo que sugiere que las condiciones de alta humedad favorecen su acumulación, posiblemente debido a la facilidad con que la cocaína se hidroliza en presencia de agua."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["Además de estos alcaloides, se identificaron otros compuestos como el éster metílico de ecgonina y diversos flavonoides y ácidos fenólicos, entre ellos el ácido abiético y el ácido clorogénico. Estos componentes subrayan la especificidad y adaptación ecológica de cada tipo de coca, demostrando la versatilidad de estas plantas para producir sustancias de defensa y adaptación."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["Al explorar las funciones críticas de estas sustancias, encontramos que la ecgonina actúa como precursor en la biosíntesis de la cocaína. Sirve como reserva de carbono y nitrógeno, elementos esenciales para el crecimiento y desarrollo de la planta. Su acumulación puede ser una respuesta a factores de estrés ambiental, permitiendo a la planta adaptarse a diversas condiciones."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["La cocaína, el alcaloide más estudiado de la hoja de coca, desempeña múltiples roles vitales. Funciona como un potente repelente de herbívoros debido a su toxicidad, disuadiendo ataques y protegiendo a la planta. También posee propiedades antimicrobianas, ayudando a resistir infecciones por bacterias, hongos y otros patógenos. En situaciones de estrés, como sequía o alta radiación solar, la producción de cocaína puede aumentar, sugiriendo un papel en la mitigación del daño celular y en la adaptación a condiciones adversas."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["El ácido abiético es un diterpeno presente en la hoja de coca que cumple funciones protectoras y adaptativas. Conocido por sus propiedades antiinflamatorias y cicatrizantes, contribuye a la reparación de tejidos dañados y a la defensa contra patógenos y herbívoros. Además, actúa como antioxidante, protegiendo las células vegetales del daño oxidativo causado por factores ambientales como la radiación UV y los radicales libres. Este compuesto también puede influir en la interacción de la planta con microorganismos beneficiosos del suelo, favoreciendo la simbiosis y mejorando la absorción de nutrientes."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["Es importante destacar que, al masticar la hoja de coca, los alcaloides como la cocaína son liberados y pueden sufrir transformaciones químicas en el organismo humano. El proceso de hidrólisis convierte la cocaína en benzoilecgonina y éster metílico de ecgonina, metabolitos con diferentes efectos y perfiles de actividad. Sin embargo, la cocaína ingerida de esta manera se metaboliza principalmente en el hígado y, en menor medida, en la boca."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["La hoja de coca es un compendio de complejos compuestos químicos que reflejan la sofisticación de los mecanismos de defensa y adaptación de las plantas. El estudio de sus metabolitos secundarios nos ofrece una ventana a las estrategias evolutivas de supervivencia vegetal y revela potenciales aplicaciones farmacológicas y terapéuticas que han sido aprovechadas por diversas culturas a lo largo de la historia."]),
                ],id="conclu1", className="text-none"),

                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Button(id='toggle-button1', children=html.Img(src='/assets/icon-mas.webp',style={'width': '48px', 'height': '48px'}), n_clicks=0, className="boton-imagen"),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),

                html.Div("Resultado del análisis químico de las cuatro variedades ",className="body-title-2",id="conclu_resultados"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["En un exhaustivo análisis de las cuatro variedades de coca, emergieron notables diferencias en la expresión de sus metabolitos secundarios. Realizamos una comparación detallada de la presencia o ausencia de diversos alcaloides en cada variedad. Destaca que la variedad Truxillense carece de trigonelina, mientras que la Novogranatense no manifiesta ni trigonelina ni metil éster de ecgonina. Por otro lado, la Mimosina fue detectada exclusivamente en la variedad Ipadu, aunque en proporciones muy bajas."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),


                html.Div(children=[
                        html.Div(["Las proporciones de los metabolitos revelaron una marcada predominancia de cocaína y ecgonina, con otros alcaloides presentes en menor medida. De particular relevancia fueron el metil éster de ecgonina y el etil éster de ecgonina, identificados únicamente en la variedad Ipadu. La variedad Coca presentó la mayor proporción de cocaína respecto a ecgonina, mientras que la Novogranatense mostró una proporción equilibrada entre ambos. En contraste, las variedades Ipadu y Truxillense exhibieron una mayor proporción de ecgonina en comparación con cocaína, siendo Ipadu la que mostró la diferencia más pronunciada, casi opuesta a la variedad Coca. Es importante aclarar que este estudio proporciona datos cualitativos, y los porcentajes reportados se calcularon en función de la intensidad de la señal del compuesto más abundante en cada cromatograma. Los análisis cuantitativos de cada metabolito se llevarán a cabo en estudios futuros."]),
                        dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                        html.Div(["Al comparar los metabolitos secundarios de naturaleza ácida o fenólica, la variedad Truxillense destacó por su mayor diversidad, presentando diez fenoles. Le siguió la variedad Coca con siete fenoles, y las variedades Ipadu y Novogranatense con seis fenoles cada una. Entre los ácidos fenólicos, el ácido abietico fue el más prevalente en todas las variedades, seguido por el ácido cinámico y el ácido shikímico."]),
                        dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                        html.Div(["En términos generales, las proporciones aparentes de los ácidos fenólicos fueron inferiores a las de los alcaloides. La variedad Ipadu mostró la mayor presencia de ácidos fenólicos, mientras que la Novogranatense presentó la menor diversidad en su expresión."]),
                ],id="conclu2", className="text-none"),

                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Button(id='toggle-button2', children=html.Img(src='/assets/icon-mas.webp',style={'width': '48px', 'height': '48px'}), n_clicks=0, className="boton-imagen"),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),


                html.Div("Conclusiones del estudio de metabolitos en las variedades de coca",className="body-title-2",id="conclu_variedades"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["El análisis comparativo de las cuatro variedades reveló diferencias sustanciales en la presencia y proporción de diversos metabolitos secundarios, destacándose principalmente los alcaloides y los ácidos fenólicos."]),
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Div("Alcaloides:",className="body-title-3",id="conclu_var-1"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["En cuanto a las proporciones de cocaína y ecgonina, se observaron tendencias distintivas: la variedad Coca exhibió una predominancia de cocaína sobre la ecgonina, mientras que las variedades Ipadu y Truxillense mostraron una mayor proporción de ecgonina en relación con la cocaína. Por otro lado, la variedad Novogranatense mantuvo una proporción equilibrada entre estos dos metabolitos."]),
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Div("Ácidos Fenólicos:",className="body-title-3",id="conclu_var-2"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Entre las cuatro variedades analizadas, la Truxillense destacó por su mayor diversidad fenólica, presentando diez diferentes fenoles. Le siguieron la variedad Coca con siete fenoles, y tanto Ipadu como Novogranatense con seis cada una."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),


                html.Div(children=[
                        html.Div(["En cuanto a los ácidos específicos, el ácido abiético predominó en todas las variedades, evidenciando la mayor proporción entre los fenoles identificados. Asimismo, tanto el ácido cinámico como el ácido shikímico estuvieron presentes de manera uniforme en todas las variedades estudiadas. Sin embargo, ciertas variantes mostraron ausencias notables: el ácido clorogénico y el ácido 3-O-cumaroilquínico no se detectaron en la variedad Novogranatense, mientras que el ácido 5-O-cumaroilquínico y el ácido cafeico estuvieron ausentes en Truxillense y Novogranatense, respectivamente."]),
                        dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                        html.Div(["Las proporciones de ácidos fenólicos fueron inferiores en comparación con los alcaloides, destacándose la variedad Ipadu por su mayor concentración de estos compuestos, en contraste con la Novogranatense, que presentó la menor diversidad de expresión fenólica. Esta notable presencia de ácidos orgánicos en Ipadu puede atribuirse al mayor estrés ambiental al que está sometida, dado su origen amazónico. En esta región, los suelos ricos en materia orgánica y la alta biodiversidad de plantas y microorganismos favorecen la producción de una amplia gama de metabolitos diversos."]),
                        dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                        html.Div(["Este estudio no solo resalta la variabilidad bioquímica entre las distintas variedades de coca, sino que también sugiere que las condiciones ambientales específicas desempeñan un papel crucial en la síntesis y acumulación de metabolitos secundarios. Tales hallazgos podrían tener implicaciones significativas tanto para el uso tradicional de estas variedades como para futuras investigaciones científicas orientadas a aprovechar sus compuestos bioactivos."]),
                ],id="conclu3", className="text-none"),

                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Button(id='toggle-button3', children=html.Img(src='/assets/icon-mas.webp',style={'width': '48px', 'height': '48px'}), n_clicks=0, className="boton-imagen"),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),


                html.Div(["Comparación de compuestos presentes en la literatura vs. los presentes en el jardín de ", html.Span("Khoka Project", className="italic-text"), "."],className="body-title-2",id="conclu_compara"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["El análisis de las cuatro variedades de coca presentes en el bioarchivo de ", html.Span("Khoka Project", className="italic-text"), " reveló la identificación de dieciocho metabolitos secundarios, destacándose los alcaloides como el grupo predominante, seguidos por los ácidos hidroxicinámicos. Un hallazgo notable fue la presencia exclusiva de trans-cinnamoylcocaína, corroborando los informes de Plowman que indican una mayor incidencia de este isómero en comparación con la cis-cinnamoylcocaína, cuya ausencia también fue confirmada en todas las variedades estudiadas."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),

                html.Div(children=[
                        html.Div(["En cuanto a otras clases de compuestos, se observó una escasa presencia de terpenos y sesquiterpenos en las cuatro variedades. Además, los flavonoides estuvieron completamente ausentes, incluso en la variedad Truxillensis, lo que subraya una particular carencia en este grupo de metabolitos. Sin embargo, la detección de compuestos como la mimosina y la trigonelina aportó un perfil de alcaloides distintivo, diferenciando cada variedad de manera significativa."]),
                        dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                        html.Div(["Es importante resaltar que únicamente los alcaloides coinciden tanto con los reportes existentes en la literatura como con los hallazgos obtenidos en el herbario. Los alcaloides identificados incluyen cocaína, trans-cinnamoylcocaína, ecgonina, éster etílico de ecgonina, benzoil ecgonina, éster metílico de ecgonina y tropina. Esta coincidencia refuerza la fiabilidad de los datos obtenidos y subraya la relevancia de los alcaloides en el perfil bioquímico de las variedades de coca estudiadas."]),
                        dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                        html.Div(["En síntesis, este estudio no solo confirma la predominancia de los alcaloides en las variedades de coca, sino que también destaca la variabilidad en la presencia de otros metabolitos secundarios, influenciada posiblemente por factores genéticos y ambientales. Estos hallazgos ofrecen una base sólida para futuras investigaciones enfocadas en la explotación biotecnológica y farmacológica de estos compuestos."]),
                ],id="conclu4", className="text-none"),
                
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Button(id='toggle-button4', children=html.Img(src='/assets/icon-mas.webp',style={'width': '48px', 'height': '48px'}), n_clicks=0, className="boton-imagen"),
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),


                html.Div("Referencias Bibliográficas",className="body-title-2",id="conclu_referen"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Adams, R., Cristol, S. J., Anderson, A. A., & Albert, A. A. (1945). The structure of leucenol.", 
                          html.Span("I. Journal of the American Chemical Society",className="italic-text"),", 67, 89–92. https://doi.org/10.1021/ja01217a032"],className="body-biblio"),
                html.Div(["Albert Niemann. (1860). Ueber eine neue organische Base in den Cocablättern.", 
                          html.Span("Archiv der Pharmazie",className="italic-text"),"153(2-3), 129–155, 291–308."],className="body-biblio"),
                html.Div(["Budavari, S. (Ed.). (1996). The Merck Index: An encyclopedia of chemicals, drugs, and biologicals (12a ed.). Merck. ISBN 0911910123.", 
                          ],className="body-biblio"),
                html.Div(["Casale, J. F., Pinero, E. L., & Corbeil, E. M. (2006). Isolation of cis-cinnamoylcocaine from crude illicit cocaine via alumina column chromatography.", 
                          html.Span("Journal of Microbiology",className="italic-text"),"4(1-4), 37-41."],className="body-biblio"),
                html.Div(["Chow, W. L., Gonzalez, M. A., Avanes, A. A., & Olson, D. E. (2023). Rapid synthesis of psychoplastogenic tropane alkaloids. JACS Au, 3(10), 2703-2708.", 
                          ],className="body-biblio"),
                html.Div(["Cognard, E., et al. (2006). [Título del artículo].", 
                          html.Span("Journal of Pharmaceutical and Biomedical Analysis",className="italic-text"),", 41, 925."],className="body-biblio"),
                html.Div(["Collins, A., & Matthews, J. C. (1983, febrero). Interactions of cocaine and cocaine congeners with sodium channels.", 
                          html.Span("Biochemical Pharmacology",className="italic-text"),", 32(3), 455–460. https://doi.org/10.1016/0006-2952(83)90523-3"],className="body-biblio"),
                html.Div(["Curry, S. H., & Marler, M. (2020, mayo). Effects of ecgonine methyl ester on cognition in scopolamine-impaired and aged rats.", 
                          html.Span("[Nombre de la revista]",className="italic-text"),", Volumen, [Páginas]."],className="body-biblio"),
                html.Div(["Dewick, P. M. (2002). Medicinal natural products: A biosynthetic approach (3ª ed.). John Wiley & Sons.", 
                          ],className="body-biblio"),
                html.Div(["Evans, W. C. (1981). The comparative phytochemistry of the genus Erythroxylon.", 
                          html.Span("Journal of Ethnopharmacology",className="italic-text"),", 3."],className="body-biblio"),
                html.Div(["Facchini, P. J., & St-Pierre, B. (2005). Synthesis and accumulation of alkaloids in pharmaceutical plants.", 
                          html.Span("Current Opinion in Plant Biology",className="italic-text"),", 8(3), 317-324."],className="body-biblio"),
                html.Div(["Findlay, S. P. (1954). The three-dimensional structure of the cocaines. Part I. Cocaine and pseudococaine.", 
                          html.Span("Journal of the American Chemical Society",className="italic-text"),", 76(11), 2855-2862."],className="body-biblio"),
                html.Div(["Gaedcke, F. (1855). Ueber das Erythroxylin, dargestellt aus den Blättern des in Südamerika.", 
                          ],className="body-biblio"),
                html.Div(["Gootenberg, P. (2009). Andean cocaine: The making of a global drug.", 
                          html.Span("University of North Carolina Press.",className="italic-text"),""],className="body-biblio"),
                html.Div(["Harris, G. C., & Sanderson, T. F. (1963). Abietic acid.", 
                          html.Span("Organic Syntheses",className="italic-text"),", 32, 1; Coll. Vol. 4:1."],className="body-biblio"),
                html.Div(["Hemel, P. B., & Chiltoskey, M. U. (1975). Cherokee plants and their uses – A 400 year history. Sylva, NC: Herald Publishing Co.; citado en Moerman,", 
                          html.Span("D. A. A database of foods, drugs, dyes and fibers of Native American peoples, derived from plants.",className="italic-text"),""],className="body-biblio"),
                html.Div(["Hoffman, R. S., Kaplan, J. L., Hung, O. L., & Goldfrank, L. R. (2004). Ecgonine methyl ester protects against cocaine lethality in mice.", 
                          html.Span("Journal of Toxicology: Clinical Toxicology",className="italic-text"),", 42(4), 349–354. https://doi.org/10.1081/clt-120039540"],className="body-biblio"),
                html.Div(["Henry, T. A. (1949). Leucenol. En The Plant Alkaloids (4ª ed., pp. 2–3).", 
                          html.Span("The Blakiston Company.",className="italic-text"),""],className="body-biblio"),
                html.Div(["Jowett, H. A. D., & Pyman, F. L. (1909). CXVI.—Relation between chemical constitution and physiological action in the tropane alkaloids. Part II.", 
                          html.Span("Journal of the Chemical Society",className="italic-text"),", Transactions, 95, 1020-1032."],className="body-biblio"),
                html.Div(["Johnson, E. L., & Emche, S. D. (1994). Variation of alkaloid content in Erythroxylum coca leaves from leaf bud to leaf drop.", 
                          html.Span("Annals of Botany",className="italic-text"),", 73(6), 645-650."],className="body-biblio"),
                html.Div(["Kutchan, T. M. (1995). Alkaloid biosynthesis—The basis for metabolic engineering of medicinal plants.", 
                          html.Span("The Plant Cell",className="italic-text"),", 7(7), 1059-1070."],className="body-biblio"),
                html.Div(["Kuroda, R., Kazumura, K., Ushikata, M., Minami, Y., & Kajiya, K. (2018). Elucidating the improvement in vascular endothelial function from Sakurajima Daikon and its mechanism of action: A comparative study with Raphanus sativus.", 
                          html.Span("Journal of Agricultural and Food Chemistry",className="italic-text"),", 66(33), 8714–8721. https://doi.org/10.1021/acs.jafc.8b04899"],className="body-biblio"),
                html.Div(["Mascré, M. (1937). Le leucaenol, principe défini retiré des graines de Leucaena glauca Benth. (Légumineuses Papilionacées).", 
                          html.Span("Comptes Rendus",className="italic-text"),", 204, 890–891."],className="body-biblio"),
                html.Div(["Matthews, J. C., & Collins, A. (1983, febrero). Interactions of cocaine and cocaine congeners with sodium channels.", 
                          html.Span("Biochemical Pharmacology",className="italic-text"),", 32(3), 455–460. https://doi.org/10.1016/0006-2952(83)90523-3"],className="body-biblio"),
                html.Div(["Meyer, E. M., Potter, L. T., De Vane, C. L., Irwin, I., MacKay, S. L., Miller, R., & Ruttenber, A. J. (1990). Effects of benzoyltropine and tropacocaine on several cholinergic processes in the rat brain.", 
                          html.Span("Journal of Pharmacology and Experimental Therapeutics",className="italic-text"),", 254(2), 584-590."],className="body-biblio"),
                html.Div(["Niemann, A. (1860). Ueber eine neue organische Base in den Cocablättern.", 
                          html.Span("Archiv der Pharmazie",className="italic-text"),"153(2-3), 129–155, 291–308."],className="body-biblio"),
                html.Div(["Nov, M., Ka, Saleminka, C. A., & Khanb, I. (n.d.). Review paper: Biological activity of the alkaloids of Erythroxylum coca and Erythroxylum novogranatense.", 
                          html.Span("",className="italic-text"),""],className="body-biblio"),
                html.Div(["Oliveira, S. L. D. (2012). Fitoquímica de espécies de Erythroxylum do semiárido: isolamento e determinação estrutural de alcaloides tropânicos, flavonoides e diterpenos.", 
                          html.Span("",className="italic-text"),""],className="body-biblio"),
                html.Div(["O’Hagan, D. (2000). Pyrrole, pyrrolidine, pyridine, piperidine and tropane alkaloids.", 
                          html.Span("Natural Product Reports",className="italic-text"),", 17(5), 435-446. https://doi.org/10.1039/A998546A"],className="body-biblio"),
                html.Div(["Plowman, T., & Rivier, L. (1983). Cocaine and cinnamoylcocaine content of Erythroxylum species.", 
                          html.Span("Annals of Botany",className="italic-text"),", 51(5), 641-659."],className="body-biblio"),
                html.Div(["Schaffer, M., Hill, V., & Cairns, T. (2005). Hair analysis for cocaine: The requirement for effective wash procedures and effects of drug concentration and hair porosity in contamination and decontamination.", 
                          html.Span("Journal of Analytical Toxicology",className="italic-text"),", 29(5), 319–326. https://doi.org/10.1093/jat/29.5.319"],className="body-biblio"),
                html.Div(["Wink, M. (2008). Plant secondary metabolites: Occurrence, structure, and role in the human diet.", 
                          html.Span("Blackwell Publishing.",className="italic-text"),""],className="body-biblio"),
                html.Div(["Wolff, K., et al. (1999). [Título del artículo].", 
                          html.Span("Addiction",className="italic-text"),", 94, 1279."],className="body-biblio"),
                html.Div(["Xujiang, Y. U. A. N., Lijiao, M. E. N., Yadi, L. I. U., Yu, Q. I. U., Cuimin, H. E., & Huang, W. (2020). Truxillic and truxinic acid derivatives: Configuration, source, and bioactivities of natural cyclobutane dimers.", 
                          html.Span("Journal of Holistic Integrative Pharmacy",className="italic-text"),", 1(1), 48-69. https://doi.org/10.1016/j.jhip.2020.05.002"],className="body-biblio"),


            ],
            className="container-text"
        ))





# Definir los tooltips
tooltips = []
# solvente
for i in range(1,6):
       tooltips.append(
              dbc.Tooltip("También llamado solvente, un disolvente es una sustancia, generalmente líquida, que puede disolver otras sustancias sin alterarlas químicamente para formar una solución.", 
                    target="solvente_{0}".format(str(i)), className="custom-tooltip"))




# Define the layout
layout =    [ dbc.Col(
                portada,
                xs={"size": 12, "order": 2},  # Change order to 2 on extra small devices
                sm={"size": 12, "order": 2},  # Change order to 2 on small devices
                md={"size": 12, "order": 3},
                lg={"size": 12, "order": 3},
                xl={"size": 12, "order": 3},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
                
            ),
            dbc.Col(
                conclusiones,
                xs={"size": 12, "order": 4},  # Change order to 2 on extra small devices
                sm={"size": 12, "order": 4},  # Change order to 2 on small devices
                md={"size": 12, "order": 4},
                lg={"size": 12, "order": 4},
                xl={"size": 12, "order": 4},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
            ),
            *tooltips
        ]

@callback(
    Output("download-pdf", "data"),
    Input("bt-descarga", "n_clicks"),
    prevent_initial_call=True
)
def download_pdf(n_clicks):
    return dcc.send_bytes(base64.b64decode(encoded_pdf), filename=pdf_filename)

@callback(
    Output('conclu1', 'style'),
    Output('toggle-button1', 'children'),    
    [Input('toggle-button1', 'n_clicks')]
)
def toggle_paragraph(n_clicks):
    if n_clicks % 2 == 0:
        return {'display': 'none'}, html.Img(src='/assets/icon-mas.webp',style={'width': '48px', 'height': '48px'})
    else:
        return {'display': 'block'}, html.Img(src='/assets/icon-menos.webp',style={'width': '48px', 'height': '48px'})

@callback(
    Output('conclu2', 'style'),
    Output('toggle-button2', 'children'),    
    [Input('toggle-button2', 'n_clicks')]
)
def toggle_paragraph(n_clicks):
    if n_clicks % 2 == 0:
        return {'display': 'none'}, html.Img(src='/assets/icon-mas.webp',style={'width': '48px', 'height': '48px'})
    else:
        return {'display': 'block'}, html.Img(src='/assets/icon-menos.webp',style={'width': '48px', 'height': '48px'})

@callback(
    Output('conclu3', 'style'),
    Output('toggle-button3', 'children'),    
    [Input('toggle-button3', 'n_clicks')]
)
def toggle_paragraph(n_clicks):
    if n_clicks % 2 == 0:
        return {'display': 'none'}, html.Img(src='/assets/icon-mas.webp',style={'width': '48px', 'height': '48px'})
    else:
        return {'display': 'block'}, html.Img(src='/assets/icon-menos.webp',style={'width': '48px', 'height': '48px'})

@callback(
    Output('conclu4', 'style'),
    Output('toggle-button4', 'children'),    
    [Input('toggle-button4', 'n_clicks')]
)
def toggle_paragraph(n_clicks):
    if n_clicks % 2 == 0:
        return {'display': 'none'}, html.Img(src='/assets/icon-mas.webp',style={'width': '48px', 'height': '48px'})
    else:
        return {'display': 'block'}, html.Img(src='/assets/icon-menos.webp',style={'width': '48px', 'height': '48px'})

