from pathlib import Path


# =============================================================================
# Paths
# =============================================================================

DATA_DIR = Path(".")

MALI_FILE = DATA_DIR / "mali_top_1000_full_data.csv"
UGANDA_FILE = DATA_DIR / "uganda_top_1000_full_data.csv"

OUTPUT_DIR = Path("plots")
COLUMN_SIMILARITY_FILE = Path("column_similarity.xlsx")


# =============================================================================
# Country labels
# =============================================================================

MALI = "Mali"
UGANDA = "Uganda"


# =============================================================================
# Column mappings
# =============================================================================

COLUMN_MAPPING_MALI = {
    'database_id': 'database_id',
    'Repeat Instance': 'repeat_instance',
    'Medical record number (MRN) (SCDO:1000850) Numéro du dossier médical': 'mrn',
    'date_of_birth': 'date_of_birth',
    'respondent_sex': 'gender',
    'Current marital status (SCDO:1000548) État civil actuel': 'marital_status',
    'Ethnic group (SCDO:1000868) Ethnicité': 'ethnic_group',
    'Religion (SCDO:1000869) Religion': 'religion',
    'Region (SCDO:1000870)\xa0  \xa0      Région': 'region',
    'Street (SCDO:1000872) Rue': 'street',
    'Nearest landmark (SCDO:1000873) Point de repère le plus proche': 'nearest_landmark',
    'Telephone 1 (SCDO:1000876) Téléphone 1': 'telephone_1',
    'Telephone 2 (SCDO:1000877) Téléphone 2': 'telephone_2',
    'Next of kin name (SCDO:1000878) Nom du parent le plus proche (Héritier)': 'next_of_kin_name',
    'Next of kin telephone number (SCDO:1000879) Numéro de téléphone du parent le plus proche (héritier)': 'next_of_kin_phone',
    'Relationship to participant (SCDO:1000880) Relation avec le participant': 'relationship_to_participant',
    'Has the patient consented/assented? (SCDO:1000512) Le patient a-t-il donné son consentement éclairé /assentiment ?': 'consent_assent',
    'Type(s) of informed consent obtained (SCDO:1000520) Type(s) de consentement éclairé obtenu(s) (choice=Study Enrollment Consent /                    Consentement à linscription à létude)': 'consent_study_enrollment',
    'Type(s) of informed consent obtained (SCDO:1000520) Type(s) de consentement éclairé obtenu(s) (choice=Specimen Storage Consent /                  Consentement au stockage des spécimens)': 'consent_specimen_storage',
    'Type(s) of informed consent obtained (SCDO:1000520) Type(s) de consentement éclairé obtenu(s) (choice=Genetic Material Storage Consent  /     Consentement au stockage de matériel génétique)': 'consent_genetic_storage',
    'Type(s) of informed consent obtained (SCDO:1000520) Type(s) de consentement éclairé obtenu(s) (choice=Broad Consent / consentement élargi ou ouverte)': 'consent_broad',
    'Date subject signed consent (dd/mm/yyyy) (SCDO:1000532) Date de signature du consentement par le participant (JJ/mm/aaaa)(SCDO:1000532)': 'consent_date',
    'Consented by: (SCDO:1000533) Qui a obtenu le consentement éclairé': 'consented_by',
    'hospital_name': 'hospital_name',
    'age_visit_years': 'age_visit_years',
    'Is date of SCD diagnosis known? (SCDO:1000552) La date du diagnostic de drépanocytose est-elle connue?': 'is_diagnosis_date_known',
    'Date of SCD diagnosis (dd/mm/yyyy) (SCDO:1000558) La date du diagnostic de la drépanocytose&nbsp': 'date_of_scd_diagnosis',
    ' (JJ/mm/aaaa)(SCDO:1000558)&nbsp': 'scd_diagnosis_date_2',
    'Unnamed: 28': 'unnamed_28',
    'scd_test_result': 'scd_test_result',
    'ABO blood group (SCDO:1000579) Groupe sanguin ABO': 'abo_blood_group',
    'Type of test? (SCDO:1000575) Type de test?': 'test_type',
    'Visit date (dd/mm/yyyy) (SCDO:1000539) Date de visite (jj/mm/aaaa) &nbsp': 'visit_date',
    'Unnamed: 33': 'unnamed_33',
    'Type of visit (SCDO:1000847) Type de visite': 'visit_type',
    'Calculated age (in months) on day of visit (SCDO:1000734) Âge calculé (en mois) le jour de la visite': 'age_visit_months',
    'Self-reported age (in years) (SCDO:1000547) Âge autodéclaré (en années)': 'age_self_reported',
    'Height/Length (SCDO:1000863) Taille&nbsp': 'height_length',
    'Unnamed: 38': 'unnamed_38',
    'Weight (SCDO:1000866) Poids': 'weight',
    "Patient's body temperature (SCDO:1000711) Température corporelle du patient": 'body_temperature',
    'Type of body temperature taken (SCDO:1000759) Type de température corporelle enregistrée': 'temperature_type',
    "Patient's respiratory rate (SCDO:1000714) Fréquence respiratoire du patient": 'respiratory_rate',
    'Difficulty in breathing (SCDO:1000889) Difficulté à respirer Le patient a-t-il des difficultés à respirer ?': 'diff_in_breathing',
    'Systolic blood pressure (SCDO:1000890) Tension artérielle systolique': 'systolic_blood_pressure',
    'Diastolic blood pressure (SCDO:1000891) Tension artérielle diastolique': 'diastolic_blood_pressure',
    "Using hydroxyurea (SCDO:1000591) Utilisation de l'hydroxyurée": 'using_hydroxyurea',
    "Date of initiation of hydroxyurea therapy (dd/mm/yyyy) (SCDO:1000593) Date de début du traitement à l'hydroxyurée (jj/mm/aaaa)": 'date_of_initiation_of_hydr',
    'Using penicillin V (prophylaxis) (SCDO:1000595) Utilisation de la pénicilline V (prophylaxie)': 'using_penicillin_prophylaxis',
    'Using malaria chemoprophylaxis (SCDO:1000600) Utilisation de la chimioprophylaxie contre le paludisme': 'malaria_prophylaxis',
    "Using folic acid (SCDO:1000597) Utilisation de l'acide folique": 'folic_acid',
    'Pneumococcal vaccination up to date (SCDO:1000601) Vaccination anti-pneumococcique à jour': 'pneumococcal_vacc_uptodate',
    'Blood transfusion (SCDO:1000886) Transfusion sanguine&nbsp': 'blood_transfusion',
    'X': 'x',
    'Date of blood transfusion (SCDO:1000549) Date de la transfusion sanguine': 'blood_transfusion_date',
    'Units transfused (SCDO:1000887) Unités transfusées': 'transfusion_units',
    'Priapism (SCDO:1000894) Priapisme': 'priapism',
    'Chest pain (SCDO:1000895) Douleur thoracique': 'chest_pain',
    'Anaemia (SCDO:1000896) Anémie': 'anaemia',
    'Jaundice (SCDO:1000897) Jaunisse': 'jaundice',
    "Sample collection date  Date de prélèvement de l'échantillon": 'sample_collection_date',
    'Red blood cell count (RBC) (SCDO:1000607) Numération des globules rouges': 'rbc',
    'White blood cell count (WBC) (SCDO:1000611) Numération des globules blancs': 'wbc',
    'Platelet count (SCDO:1000615) Numération des plaquettes': 'platelets',
    'Hemoglobin (SCDO:1000619) Hémoglobine': 'hemoglobin',
    'Mean cell volume (MCV) (SCDO:1000621) Volume cellulaire (ou corpusculaire) moyen (VCM)': 'mean_cell_volume',
    'Mean cell hemoglobin (MCH) (SCDO:1000627) Teneur cellulaire (ou corpusculaire) moyenne en hémoglobine (TCMH)': 'mch',
    'Mean cell hemoglobin concentration (MCHC) (SCDO:1000630) Concentration cellulaire (corpusculaire) moyenne en hémoglobine (CCMH)': 'mchc',
    'Red cell distribution width (RDW) (SCDO:1000637) Indice de distribution des globules rouges': 'rdw',
    'Serum creatinine concentration (SCDO:1000645) créatinine sanguine (créatininémie)': 'serum_creatinine',
    'Urea (SCDO:1000898) Urée': 'urea',
    "Urinary albumin concentration (SCDO:1000510) Concentration d'albumine urinaire (microalbuminurie)": 'urinary_albumin',
    'Urinary creatinine concentration (SCDO:1000650) Créatinine urinaire (créatinurie)': 'urinary_creatinine',
    "Alanine aminotransferase level (SCDO:1000657) Taux d'Alanine Aminotransférase": 'alt',
    "Aspartate aminotransferase level (SCDO:1000660) Taux d'Aspartate Aminotransférase (ASAT)": 'ast',
    'Alkaline phosphatase level (SCDO:1000662) Taux de Phosphatase Alcaline (PAL)': 'alkaline_phosphatase',
    'Total bilirubin concentration (SCDO:1000680) Bilirubine Totale': 'total_bilirubin',
    'Lactate dehydrogenase level (SCDO:1000682) Taux de lactate déshydrogénase (LDH)': 'ldh',
    'Number of reticulocytes (SCDO:1000685) Numération des réticulocytes': 'reticulocytes',
    'For which hemoglobins were assay results recorded? (SCDO:1000687) Pour quelles hémoglobines les résultats des dosages ont-ils été enregistrés ? (choice=Hb A)': 'hb_a_measured',
    'For which hemoglobins were assay results recorded? (SCDO:1000687) Pour quelles hémoglobines les résultats des dosages ont-ils été enregistrés ? (choice=Hb  F)': 'hb_f_measured',
    'For which hemoglobins were assay results recorded? (SCDO:1000687) Pour quelles hémoglobines les résultats des dosages ont-ils été enregistrés ? (choice=Hb  S)': 'hb_s_measured',
    'For which hemoglobins were assay results recorded? (SCDO:1000687) Pour quelles hémoglobines les résultats des dosages ont-ils été enregistrés ? (choice=Hb  C)': 'hb_c_measured',
    'For which hemoglobins were assay results recorded? (SCDO:1000687) Pour quelles hémoglobines les résultats des dosages ont-ils été enregistrés ? (choice=Hb  E)': 'hb_e_measured',
    'For which hemoglobins were assay results recorded? (SCDO:1000687) Pour quelles hémoglobines les résultats des dosages ont-ils been recorded ? (choice=Hb A2)': 'hb_a2_measured',
    'For which hemoglobins were assay results recorded? (SCDO:1000687) Pour quelles hémoglobines les résultats des dosages ont-ils été enregistrés ? (choice=Hb  D-Punjab)': 'hb_d_punjab_measured',
    'For which hemoglobins were assay results recorded? (SCDO:1000687) Pour quelles hémoglobines les résultats des dosages ont-ils été enregistrés ? (choice=Hb  G-Philadelphia)': 'hb_g_philadelphia_measured',
    'For which hemoglobins were assay results recorded? (SCDO:1000687) Pour quelles hémoglobines les résultats des dosages ont-ils été enregistrés ? (choice=Hb  O-Arab)': 'hb_o_arab_measured',
    "Record the levels of Hb A if measured. (SCDO:1000691) Enregistrez les niveaux d'Hb A s'ils sont mesurés": 'hb_a_level',
    "Record the levels of Hb F if measured. (SCDO:1000706) Enregistrez les niveaux d'Hb F s'ils sont mesurés": 'hb_f_level',
    "Record the levels of Hb S if measured. (SCDO:1000693) Enregistrez les niveaux d'Hb S s'ils sont mesurés": 'hb_s_level',
    "Record the levels of Hb C if measured. (SCDO:1000694) Enregistrez les niveaux d'Hb C s'ils sont mesurés": 'hb_c_level',
    "Record the levels of Hb E if measured. (SCDO:1000696) Enregistrez les niveaux d'Hb E s'ils sont mesurés": 'hb_e_level',
    "Record the levels of Hb A2 if measured. (SCDO:1000699) Enregistrez les niveaux d'Hb A2 s'ils sont mesurés": 'hb_a2_level',
    "Record the levels of Hb D-Punjab if measured. (SCDO:1000700) Enregistrez les niveaux d'Hb D-Punjab s'ils sont mesurés": 'hb_d_punjab_level',
    'Total hemoglobin (Hbtotal) (SCDO:1000751) Hémoglobine totale': 'hb_total',
    "Oxyhemoglobin saturation (HbO2) (SCDO:1000724)\xa0 Saturation de l'oxyhémoglobine (HbO2)(SCDO:1000724)": 'hbo2_saturation'
}



# =============================================================================
# Variable groups
# =============================================================================

CATEGORICAL_VARS = [
    'gender',
    'marital_status',
    'ethnic_group',
    'region',
    'hospital_name',
    'abo_blood_group'
]

TREATMENT_VARS = [
    'using_hydroxyurea',
    'using_penicillin_prophylaxis',
    'malaria_prophylaxis',
    'folic_acid',
    'pneumococcal_vacc_uptodate',
    'blood_transfusion'
]


# =============================================================================
# Cleaning mappings
# =============================================================================

GENDER_MAPPING = {
    "Female: Femme": "Female",
    "Male:Homme": "Male",
    "Male   Homme": "Male",
}


MALI_MARITAL_STATUS_MAPPING = {
    "Never been married/Annulled    Jamais marié(e)/Annulé(e)":
        "Never been married/Annulled",
    "Married          Mariés":
        "Married",
    "Divorced       Divorcé":
        "Divorced",
    "Widowed        Veuf(ve)":
        None,
    "Separated     Séparé(e)":
        "Separated",
}


MALI_HYDROXYUREA_MAPPING = {
    "Oui": "Yes",
    "Non": "No",
}

MALI_OUINON_MAPPING = {
    "Oui": "Yes",
    "Non": "No",
}


UGANDA_HOSPITAL_MAPPING = {
    "Jrrh": "JRRH",
    "Jinja": "Jinja Hospital",
    "Jinja hospital": "Jinja Hospital",
    "JRRH": "JRRH",
    "Mbale RRH": "MRRH",
    "Mbale  RRH": "MRRH",
    "MRRH": "MRRH",
    "Mulago": "Mulago",
}


# =============================================================================
# Numeric variables
# =============================================================================

MALI_NUMERIC_VARS = [
    "mean_cell_volume",
    "hemoglobin",
    "age_visit_years",
]

UGANDA_NUMERIC_VARS = [
    "mean_cell_volume",
    "hemoglobin",
    "calculated_age",
]
