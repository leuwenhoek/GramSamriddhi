import os
import json
import matplotlib.pyplot as plt


class JSONDataModule:
    def __init__(self):
        # Define directory and file paths
        self.base_dir = 'data'
        self.static_dir = 'static'
        
        # Electricity
        self.electricity_dir = os.path.join(self.base_dir, 'electricity')
        self.electricity_json = os.path.join(self.electricity_dir, 'electricity_data.json')
        self.electricity_graph_dir = os.path.join(self.static_dir, 'electricity')
        self.electricity_graph = os.path.join(self.electricity_graph_dir, 'electricity_graph.png')

        # Water
        self.water_dir = os.path.join(self.base_dir, 'water')
        self.water_json = os.path.join(self.water_dir, 'water_data.json')
        self.water_graph_dir = os.path.join(self.static_dir, 'water')
        self.water_graph = os.path.join(self.water_graph_dir, 'water_graph.png')

        # Projects
        self.projects_dir = os.path.join(self.base_dir, 'projects')
        self.projects_json = os.path.join(self.projects_dir, 'projects_data.json')
        self.projects_graph_dir = os.path.join(self.static_dir, 'projects')
        self.projects_graph = os.path.join(self.projects_graph_dir, 'projects_graph.png')

    def ensure_directories(self):
        os.makedirs(self.electricity_dir, exist_ok=True)
        os.makedirs(self.water_dir, exist_ok=True)
        os.makedirs(self.electricity_graph_dir, exist_ok=True)
        os.makedirs(self.water_graph_dir, exist_ok=True)
        os.makedirs(self.projects_dir, exist_ok=True)
        os.makedirs(self.projects_graph_dir, exist_ok=True)

    # ==================== ELECTRICITY DATA ====================
    def get_electricity_data(self):
        return {
            "jitwarr_purr_village": {
                "electricity_data": [
                    {"month": "January", "consumption_kwh": 1250, "bill_rupees": 9500, "power_cuts": 8},
                    {"month": "February", "consumption_kwh": 1180, "bill_rupees": 8900, "power_cuts": 6},
                    {"month": "March", "consumption_kwh": 1350, "bill_rupees": 10200, "power_cuts": 10},
                    {"month": "April", "consumption_kwh": 1420, "bill_rupees": 10700, "power_cuts": 12},
                    {"month": "May", "consumption_kwh": 1580, "bill_rupees": 11900, "power_cuts": 15},
                    {"month": "June", "consumption_kwh": 1620, "bill_rupees": 12200, "power_cuts": 18},
                    {"month": "July", "consumption_kwh": 1550, "bill_rupees": 11700, "power_cuts": 14},
                    {"month": "August", "consumption_kwh": 1480, "bill_rupees": 11200, "power_cuts": 11},
                    {"month": "September", "consumption_kwh": 1320, "bill_rupees": 10000, "power_cuts": 9},
                    {"month": "October", "consumption_kwh": 1280, "bill_rupees": 9700, "power_cuts": 7},
                    {"month": "November", "consumption_kwh": 1220, "bill_rupees": 9200, "power_cuts": 5},
                    {"month": "December", "consumption_kwh": 1300, "bill_rupees": 9800, "power_cuts": 4}
                ],
                "summary": {
                    "total_consumption_kwh": 15950,
                    "total_bill_rupees": 120200,
                    "average_power_cuts_per_month": 9.5
                }
            }
        }

    # ==================== WATER DATA ====================
    def get_water_data(self):
        return {
            "jitwarr_purr_village": {
                "water_supply_data": [
                    {"month": "January", "consumption_kl": 420, "bill_rupees": 2800, "supply_days": 28, "shortage_days": 3},
                    {"month": "February", "consumption_kl": 395, "bill_rupees": 2600, "supply_days": 26, "shortage_days": 2},
                    {"month": "March", "consumption_kl": 450, "bill_rupees": 3000, "supply_days": 29, "shortage_days": 2},
                    {"month": "April", "consumption_kl": 480, "bill_rupees": 3200, "supply_days": 27, "shortage_days": 3},
                    {"month": "May", "consumption_kl": 520, "bill_rupees": 3500, "supply_days": 25, "shortage_days": 6},
                    {"month": "June", "consumption_kl": 540, "bill_rupees": 3600, "supply_days": 23, "shortage_days": 7},
                    {"month": "July", "consumption_kl": 510, "bill_rupees": 3400, "supply_days": 26, "shortage_days": 5},
                    {"month": "August", "consumption_kl": 490, "bill_rupees": 3300, "supply_days": 27, "shortage_days": 4},
                    {"month": "September", "consumption_kl": 440, "bill_rupees": 2900, "supply_days": 28, "shortage_days": 2},
                    {"month": "October", "consumption_kl": 425, "bill_rupees": 2800, "supply_days": 29, "shortage_days": 2},
                    {"month": "November", "consumption_kl": 410, "bill_rupees": 2700, "supply_days": 28, "shortage_days": 2},
                    {"month": "December", "consumption_kl": 430, "bill_rupees": 2850, "supply_days": 29, "shortage_days": 2}
                ],
                "summary": {
                    "total_consumption_kl": 5510,
                    "total_bill_rupees": 36610,
                    "average_supply_days_per_month": 27.08,
                    "total_shortage_days": 40
                }
            }
        }

    # ==================== PROJECTS DATA ====================
    def get_projects_data(self):
        return {
  "jitwarr_purr_village": {
    "projects": {
      "total_projects": 40,
      "active_projects": 23,
      "completed_projects": 17,
      "projects_data": [
        {
          "project_id": "P001",
          "name": "Solar Street Lighting Installation",
          "category": "Infrastructure",
          "description": "Installation of 150 solar-powered LED street lights across main village roads to improve night-time safety and reduce energy costs.",
          "start_date": "2023-01-15",
          "end_date": "2023-06-30",
          "budget_allocated": 850000,
          "budget_spent": 820000,
          "funding_sources": ["Village Panchayat Fund", "MNRE Grant"],
          "status": "Active",
          "progress_percentage": 95,
          "lead_agency": "Jitwarpur Panchayat",
          "target_beneficiaries": 1200,
          "actual_beneficiaries": 1180,
          "key_achievements": ["125 lights installed", "20% energy savings achieved"],
          "challenges": ["Initial delays due to monsoon"],
          "priority_level": "High"
        },
        {
          "project_id": "P002",
          "name": "Community Health Center Upgrade",
          "category": "Health",
          "description": "Renovation and equipping of the primary health center with modern facilities including digital X-ray and telemedicine setup.",
          "start_date": "2023-03-10",
          "end_date": "2024-12-31",
          "budget_allocated": 1250000,
          "budget_spent": 950000,
          "funding_sources": ["NHM Funds", "CSR - Local Hospital"],
          "status": "Active",
          "progress_percentage": 75,
          "lead_agency": "District Health Department",
          "target_beneficiaries": 2500,
          "actual_beneficiaries": 1800,
          "key_achievements": ["New OPD building completed", "Telemedicine operational"],
          "challenges": ["Staff recruitment delays"],
          "priority_level": "Critical"
        },
        {
          "project_id": "P003",
          "name": "Women Skill Development Center",
          "category": "Education & Skills",
          "description": "Establishment of a training center offering vocational courses in tailoring, computer literacy, and beauty culture for 200 women.",
          "start_date": "2023-02-20",
          "end_date": "2023-11-30",
          "budget_allocated": 450000,
          "budget_spent": 420000,
          "funding_sources": ["NRLM", "Village Savings Group"],
          "status": "Active",
          "progress_percentage": 88,
          "lead_agency": "Mahila Samiti",
          "target_beneficiaries": 200,
          "actual_beneficiaries": 175,
          "key_achievements": ["150 women trained", "50 self-help groups formed"],
          "challenges": ["Low attendance during harvest season"],
          "priority_level": "Medium"
        },
        {
          "project_id": "P004",
          "name": "Village Library & Digital Resource Center",
          "category": "Education",
          "description": "Construction of a modern library with 5000 books and computer lab with internet access for students and youth.",
          "start_date": "2023-04-01",
          "end_date": "2024-03-31",
          "budget_allocated": 320000,
          "budget_spent": 280000,
          "funding_sources": ["Sarva Shiksha Abhiyan", "Local Donations"],
          "status": "Active",
          "progress_percentage": 85,
          "lead_agency": "Village Education Committee",
          "target_beneficiaries": 800,
          "actual_beneficiaries": 650,
          "key_achievements": ["Building completed", "3000 books procured"],
          "challenges": ["Internet connectivity issues"],
          "priority_level": "Medium"
        },
        {
          "project_id": "P005",
          "name": "Wastewater Treatment Plant",
          "category": "Sanitation",
          "description": "Construction of a decentralized wastewater treatment facility to serve 500 households and prevent water contamination.",
          "start_date": "2023-05-15",
          "end_date": "2024-09-30",
          "budget_allocated": 1800000,
          "budget_spent": 1450000,
          "funding_sources": ["Swachh Bharat Mission", "State Jal Board"],
          "status": "Active",
          "progress_percentage": 80,
          "lead_agency": "Public Health Engineering Dept.",
          "target_beneficiaries": 2500,
          "actual_beneficiaries": 2000,
          "key_achievements": ["Treatment plant 80% complete", "Pipeline network laid"],
          "challenges": ["Land acquisition delays"],
          "priority_level": "High"
        },
        {
          "project_id": "P006",
          "name": "Agricultural Training & Demo Farm",
          "category": "Agriculture",
          "description": "Development of a 5-acre demonstration farm showcasing modern farming techniques, drip irrigation, and organic farming methods.",
          "start_date": "2023-01-10",
          "end_date": "2023-12-31",
          "budget_allocated": 650000,
          "budget_spent": 620000,
          "funding_sources": ["ATMA", "Krishi Vigyan Kendra"],
          "status": "Active",
          "progress_percentage": 92,
          "lead_agency": "Block Agriculture Office",
          "target_beneficiaries": 450,
          "actual_beneficiaries": 420,
          "key_achievements": ["Demo farm operational", "200 farmers trained"],
          "challenges": ["Water scarcity in summer"],
          "priority_level": "High"
        },
        {
          "project_id": "P007",
          "name": "Youth Sports Complex",
          "category": "Youth Development",
          "description": "Construction of a multi-sport facility including cricket ground, volleyball court, and indoor badminton hall for village youth.",
          "start_date": "2023-06-01",
          "end_date": "2024-06-30",
          "budget_allocated": 950000,
          "budget_spent": 720000,
          "funding_sources": ["Sports Authority", "Village Youth Association"],
          "status": "Active",
          "progress_percentage": 75,
          "lead_agency": "Panchayat Youth Committee",
          "target_beneficiaries": 350,
          "actual_beneficiaries": 280,
          "key_achievements": ["Cricket ground ready", "Equipment procured"],
          "challenges": ["Funding delays"],
          "priority_level": "Medium"
        },
        {
          "project_id": "P008",
          "name": "Rainwater Harvesting System",
          "category": "Water Conservation",
          "description": "Installation of 50 rooftop rainwater harvesting systems in schools and community buildings to recharge groundwater.",
          "start_date": "2023-03-01",
          "end_date": "2023-10-31",
          "budget_allocated": 280000,
          "budget_spent": 265000,
          "funding_sources": ["Jal Shakti Abhiyan", "NGO Partnership"],
          "status": "Active",
          "progress_percentage": 94,
          "lead_agency": "Watershed Management Committee",
          "target_beneficiaries": 1500,
          "actual_beneficiaries": 1420,
          "key_achievements": ["45 systems installed", "20% groundwater recharge"],
          "challenges": ["Technical training needed"],
          "priority_level": "High"
        },
        {
          "project_id": "P009",
          "name": "Digital Literacy Program",
          "category": "Education",
          "description": "Training program to provide basic digital literacy to 300 senior citizens and women in using smartphones and internet services.",
          "start_date": "2023-07-15",
          "end_date": "2024-04-30",
          "budget_allocated": 180000,
          "budget_spent": 145000,
          "funding_sources": ["Digital India", "Local IT Volunteers"],
          "status": "Active",
          "progress_percentage": 80,
          "lead_agency": "Village IT Committee",
          "target_beneficiaries": 300,
          "actual_beneficiaries": 240,
          "key_achievements": ["200 participants trained", "WhatsApp groups created"],
          "challenges": ["Language barriers"],
          "priority_level": "Medium"
        },
        {
          "project_id": "P010",
          "name": "Handpump Repair & Maintenance",
          "category": "Water Supply",
          "description": "Comprehensive repair and maintenance of 35 existing handpumps and installation of 5 new ones in remote areas.",
          "start_date": "2023-02-01",
          "end_date": "2023-08-31",
          "budget_allocated": 220000,
          "budget_spent": 210000,
          "funding_sources": ["Jal Jeevan Mission", "Panchayat Funds"],
          "status": "Active",
          "progress_percentage": 95,
          "lead_agency": "Handpump Maintenance Committee",
          "target_beneficiaries": 1800,
          "actual_beneficiaries": 1750,
          "key_achievements": ["32 handpumps repaired", "Water quality improved"],
          "challenges": ["Spare parts availability"],
          "priority_level": "High"
        },
        {
          "project_id": "P011",
          "name": "School Infrastructure Improvement",
          "category": "Education",
          "description": "Construction of additional classrooms, toilets, and boundary walls for the village middle school.",
          "start_date": "2023-01-20",
          "end_date": "2023-09-30",
          "budget_allocated": 750000,
          "budget_spent": 720000,
          "funding_sources": ["Samarth Scheme", "RUSA"],
          "status": "Active",
          "progress_percentage": 96,
          "lead_agency": "School Management Committee",
          "target_beneficiaries": 450,
          "actual_beneficiaries": 440,
          "key_achievements": ["3 new classrooms ready", "Toilet block completed"],
          "challenges": ["Monsoon-related delays"],
          "priority_level": "High"
        },
        {
          "project_id": "P012",
          "name": "Organic Farming Promotion",
          "category": "Agriculture",
          "description": "Promotion of organic farming practices through training, certification, and market linkages for 100 farmers.",
          "start_date": "2023-04-15",
          "end_date": "2024-03-31",
          "budget_allocated": 380000,
          "budget_spent": 320000,
          "funding_sources": ["Paramparagat Krishi Vikas Yojana", "NGO Support"],
          "status": "Active",
          "progress_percentage": 84,
          "lead_agency": "Organic Farming Group",
          "target_beneficiaries": 100,
          "actual_beneficiaries": 85,
          "key_achievements": ["60 farmers certified", "Organic market linkages established"],
          "challenges": ["Certification process delays"],
          "priority_level": "Medium"
        },
        {
          "project_id": "P013",
          "name": "Elderly Care Home",
          "category": "Social Welfare",
          "description": "Construction of a day care center for 50 elderly citizens with medical checkup facilities and recreational activities.",
          "start_date": "2023-05-01",
          "end_date": "2024-01-31",
          "budget_allocated": 420000,
          "budget_spent": 380000,
          "funding_sources": ["NSAP", "Local Donations"],
          "status": "Active",
          "progress_percentage": 90,
          "lead_agency": "Senior Citizens Association",
          "target_beneficiaries": 50,
          "actual_beneficiaries": 45,
          "key_achievements": ["Building 90% complete", "Medical tie-up established"],
          "challenges": ["Staff training required"],
          "priority_level": "Medium"
        },
        {
          "project_id": "P014",
          "name": "Livelihood Support for Landless Families",
          "category": "Livelihood",
          "description": "Provision of goats, poultry units, and sewing machines to 75 landless families to create sustainable income sources.",
          "start_date": "2023-06-10",
          "end_date": "2024-06-10",
          "budget_allocated": 560000,
          "budget_spent": 520000,
          "funding_sources": ["MGNREGA", "SGSY"],
          "status": "Active",
          "progress_percentage": 92,
          "lead_agency": "SHG Federation",
          "target_beneficiaries": 75,
          "actual_beneficiaries": 70,
          "key_achievements": ["65 families provided assets", "Training completed"],
          "challenges": ["Follow-up monitoring needed"],
          "priority_level": "High"
        },
        {
          "project_id": "P015",
          "name": "Cultural Heritage Preservation",
          "category": "Culture",
          "description": "Restoration of the 150-year-old village temple and documentation of local folk arts and traditions.",
          "start_date": "2023-03-25",
          "end_date": "2023-12-15",
          "budget_allocated": 280000,
          "budget_spent": 260000,
          "funding_sources": ["Ministry of Culture", "Local Contributions"],
          "status": "Active",
          "progress_percentage": 93,
          "lead_agency": "Cultural Heritage Committee",
          "target_beneficiaries": 800,
          "actual_beneficiaries": 750,
          "key_achievements": ["Temple restoration 90% complete", "Folk art documentation ongoing"],
          "challenges": ["Skilled artisans shortage"],
          "priority_level": "Low"
        },
        {
          "project_id": "P016",
          "name": "Nutrition Garden Program",
          "category": "Health & Nutrition",
          "description": "Establishment of kitchen gardens in 200 households to promote nutritional security and reduce malnutrition.",
          "start_date": "2023-07-01",
          "end_date": "2024-06-30",
          "budget_allocated": 240000,
          "budget_spent": 210000,
          "funding_sources": ["POSHAN Abhiyaan", "Anganwadi Centers"],
          "status": "Active",
          "progress_percentage": 87,
          "lead_agency": "ICDS Department",
          "target_beneficiaries": 200,
          "actual_beneficiaries": 175,
          "key_achievements": ["150 gardens established", "Training sessions conducted"],
          "challenges": ["Water availability issues"],
          "priority_level": "High"
        },
        {
          "project_id": "P017",
          "name": "Road Connectivity Improvement",
          "category": "Infrastructure",
          "description": "Grading and metalling of 8 km internal village roads to improve connectivity and reduce travel time.",
          "start_date": "2023-02-15",
          "end_date": "2023-11-30",
          "budget_allocated": 1200000,
          "budget_spent": 1150000,
          "funding_sources": ["PMGSY", "Panchayat Funds"],
          "status": "Active",
          "progress_percentage": 96,
          "lead_agency": "Rural Development Department",
          "target_beneficiaries": 3000,
          "actual_beneficiaries": 2850,
          "key_achievements": ["7 km roads completed", "Drainage system installed"],
          "challenges": ["Rain delays"],
          "priority_level": "High"
        },
        {
          "project_id": "P018",
          "name": "Solar Water Pumping Stations",
          "category": "Agriculture",
          "description": "Installation of 12 solar-powered water pumping stations for irrigation in farmer fields.",
          "start_date": "2023-04-20",
          "end_date": "2024-01-31",
          "budget_allocated": 720000,
          "budget_spent": 680000,
          "funding_sources": ["MNRE", "State Agriculture Dept."],
          "status": "Active",
          "progress_percentage": 94,
          "lead_agency": "Solar Energy Committee",
          "target_beneficiaries": 150,
          "actual_beneficiaries": 140,
          "key_achievements": ["10 pumps installed", "30% irrigation coverage increase"],
          "challenges": ["Maintenance training needed"],
          "priority_level": "High"
        },
        {
          "project_id": "P019",
          "name": "Child Rights & Protection Center",
          "category": "Child Welfare",
          "description": "Establishment of a child protection unit with counseling services and legal aid for vulnerable children.",
          "start_date": "2023-08-01",
          "end_date": "2024-07-31",
          "budget_allocated": 350000,
          "budget_spent": 280000,
          "funding_sources": ["Childline India", "District Social Welfare"],
          "status": "Active",
          "progress_percentage": 80,
          "lead_agency": "Child Welfare Committee",
          "target_beneficiaries": 120,
          "actual_beneficiaries": 95,
          "key_achievements": ["Counseling services started", "Awareness camps conducted"],
          "challenges": ["Stigma around seeking help"],
          "priority_level": "Critical"
        },
        {
          "project_id": "P020",
          "name": "Eco-Tourism Development",
          "category": "Economic Development",
          "description": "Development of village trails, homestay facilities, and cultural experiences to promote responsible tourism.",
          "start_date": "2023-09-15",
          "end_date": "2024-09-15",
          "budget_allocated": 480000,
          "budget_spent": 320000,
          "funding_sources": ["Tourism Dept.", "Local Entrepreneurs"],
          "status": "Active",
          "progress_percentage": 65,
          "lead_agency": "Tourism Promotion Committee",
          "target_beneficiaries": 50,
          "actual_beneficiaries": 35,
          "key_achievements": ["3 homestays ready", "3 trail mapping completed"],
          "challenges": ["Marketing needed"],
          "priority_level": "Medium"
        },
        {
          "project_id": "P021",
          "name": "Disaster Management Training Center",
          "category": "Safety",
          "description": "Training facility for disaster preparedness including flood response, first aid, and evacuation drills.",
          "start_date": "2023-10-01",
          "end_date": "2024-09-30",
          "budget_allocated": 420000,
          "budget_spent": 280000,
          "funding_sources": ["NDMA", "State Disaster Management"],
          "status": "Active",
          "progress_percentage": 65,
          "lead_agency": "Disaster Management Committee",
          "target_beneficiaries": 500,
          "actual_beneficiaries": 320,
          "key_achievements": ["Training modules developed", "50 volunteers trained"],
          "challenges": ["Equipment procurement delays"],
          "priority_level": "High"
        },
        {
          "project_id": "P022",
          "name": "Artisan Skill Enhancement",
          "category": "Handicrafts",
          "description": "Skill development program for traditional potters and weavers to improve product quality and market access.",
          "start_date": "2023-11-01",
          "end_date": "2024-10-31",
          "budget_allocated": 260000,
          "budget_spent": 200000,
          "funding_sources": ["KVIC", "Coir Board"],
          "status": "Active",
          "progress_percentage": 75,
          "lead_agency": "Artisan Cooperative",
          "target_beneficiaries": 80,
          "actual_beneficiaries": 65,
          "key_achievements": ["Design workshop completed", "Online marketplace created"],
          "challenges": ["Market competition"],
          "priority_level": "Medium"
        },
        {
          "project_id": "P023",
          "name": "Green Energy Community Microgrid",
          "category": "Renewable Energy",
          "description": "Development of a 50kW solar microgrid to provide reliable power to 100 remote households.",
          "start_date": "2023-12-01",
          "end_date": "2024-11-30",
          "budget_allocated": 2800000,
          "budget_spent": 1800000,
          "funding_sources": ["SEC", "Green Climate Fund"],
          "status": "Active",
          "progress_percentage": 60,
          "lead_agency": "Renewable Energy Cooperative",
          "target_beneficiaries": 100,
          "actual_beneficiaries": 0,
          "key_achievements": ["Site survey completed", "Solar panels procured"],
          "challenges": ["Grid integration complexities"],
          "priority_level": "High"
        },
        {
          "project_id": "P024",
          "name": "Financial Literacy & Banking Inclusion",
          "category": "Financial Inclusion",
          "description": "Financial literacy camps and bank account opening drives for 400 unbanked households.",
          "start_date": "2024-01-15",
          "end_date": "2024-12-31",
          "budget_allocated": 150000,
          "budget_spent": 110000,
          "funding_sources": ["PMJDY", "Local Banks"],
          "status": "Active",
          "progress_percentage": 70,
          "lead_agency": "Banking Correspondent",
          "target_beneficiaries": 400,
          "actual_beneficiaries": 280,
          "key_achievements": ["250 accounts opened", "Financial literacy sessions conducted"],
          "challenges": ["Documentation issues"],
          "priority_level": "Medium"
        },
        {
          "project_id": "P025",
          "name": "Herbal Medicine Garden & Training",
          "category": "Health",
          "description": "Establishment of medicinal plant garden and training in traditional herbal medicine practices.",
          "start_date": "2024-02-01",
          "end_date": "2024-12-01",
          "budget_allocated": 220000,
          "budget_spent": 160000,
          "funding_sources": ["AYUSH Ministry", "Local Healers"],
          "status": "Active",
          "progress_percentage": 70,
          "lead_agency": "Traditional Medicine Group",
          "target_beneficiaries": 200,
          "actual_beneficiaries": 140,
          "key_achievements": ["Garden established", "50 healers trained"],
          "challenges": ["Plant sourcing difficulties"],
          "priority_level": "Low"
        },
        {
          "project_id": "P026",
          "name": "Waste Management & Recycling Unit",
          "category": "Sanitation",
          "description": "Setting up a community waste segregation and recycling unit with composting facilities.",
          "start_date": "2024-03-01",
          "end_date": "2024-12-31",
          "budget_allocated": 380000,
          "budget_spent": 280000,
          "funding_sources": ["Swachh Bharat", "Private Partnership"],
          "status": "Active",
          "progress_percentage": 70,
          "lead_agency": "Waste Management Committee",
          "target_beneficiaries": 2000,
          "actual_beneficiaries": 1500,
          "key_achievements": ["Segregation bins distributed", "Compost unit operational"],
          "challenges": ["Community behavior change"],
          "priority_level": "Medium"
        },
        {
          "project_id": "P027",
          "name": "Entrepreneurship Incubation Center",
          "category": "Economic Development",
          "description": "Support center providing mentorship, funding, and workspace for 20 young entrepreneurs.",
          "start_date": "2024-04-01",
          "end_date": "2025-03-31",
          "budget_allocated": 450000,
          "budget_spent": 300000,
          "funding_sources": ["Startup India", "MSME"],
          "status": "Active",
          "progress_percentage": 60,
          "lead_agency": "Entrepreneurship Cell",
          "target_beneficiaries": 20,
          "actual_beneficiaries": 15,
          "key_achievements": ["Space prepared", "Mentor network established"],
          "challenges": ["Funding pipeline development"],
          "priority_level": "Medium"
        },
        {
          "project_id": "P028",
          "name": "Climate Resilient Crop Varieties",
          "category": "Agriculture",
          "description": "Introduction of drought-resistant and flood-tolerant crop varieties to 200 farmers.",
          "start_date": "2024-05-01",
          "end_date": "2025-04-30",
          "budget_allocated": 320000,
          "budget_spent": 220000,
          "funding_sources": ["ICAR", "State Agriculture University"],
          "status": "Active",
          "progress_percentage": 65,
          "lead_agency": "Climate Smart Agriculture Group",
          "target_beneficiaries": 200,
          "actual_beneficiaries": 130,
          "key_achievements": ["Seed distribution started", "Demo plots established"],
          "challenges": ["Farmer acceptance"],
          "priority_level": "High"
        },
        {
          "project_id": "P029",
          "name": "Mental Health Awareness Program",
          "category": "Health",
          "description": "Community awareness and counseling services for mental health issues affecting 500 individuals.",
          "start_date": "2024-06-01",
          "end_date": "2025-05-31",
          "budget_allocated": 280000,
          "budget_spent": 180000,
          "funding_sources": ["NIMHANS", "Local Health Workers"],
          "status": "Active",
          "progress_percentage": 60,
          "lead_agency": "Mental Health Support Group",
          "target_beneficiaries": 500,
          "actual_beneficiaries": 300,
          "key_achievements": ["Awareness campaigns launched", "Counselor training completed"],
          "challenges": ["Stigma reduction"],
          "priority_level": "Medium"
        },
        {
          "project_id": "P030",
          "name": "Biodiversity Conservation Park",
          "category": "Environment",
          "description": "Creation of a 10-acre biodiversity park with native plant species and wildlife conservation education.",
          "start_date": "2024-07-01",
          "end_date": "2025-06-30",
          "budget_allocated": 650000,
          "budget_spent": 420000,
          "funding_sources": ["MoEFCC", "Wildlife Trust"],
          "status": "Active",
          "progress_percentage": 60,
          "lead_agency": "Environment Committee",
          "target_beneficiaries": 1000,
          "actual_beneficiaries": 600,
          "key_achievements": ["Land preparation completed", "Species survey done"],
          "challenges": ["Funding for maintenance"],
          "priority_level": "Low"
        },
        {
          "project_id": "P031",
          "name": "Village Archive & Documentation Center",
          "category": "Heritage",
          "description": "Digital archiving of village history, oral traditions, and important documents for future generations.",
          "start_date": "2022-06-01",
          "end_date": "2023-05-31",
          "budget_allocated": 180000,
          "budget_spent": 175000,
          "funding_sources": ["IGNCA", "Local Historians"],
          "status": "Completed",
          "progress_percentage": 100,
          "lead_agency": "Heritage Documentation Team",
          "target_beneficiaries": 1500,
          "actual_beneficiaries": 1400,
          "key_achievements": ["500 documents digitized", "Oral history recorded"],
          "challenges": ["None - successfully completed"],
          "priority_level": "Low"
        },
        {
          "project_id": "P032",
          "name": "Pucca Housing for BPL Families",
          "category": "Housing",
          "description": "Construction of 25 pucca houses for Below Poverty Line families under PMAY scheme.",
          "start_date": "2021-08-15",
          "end_date": "2023-03-31",
          "budget_allocated": 3750000,
          "budget_spent": 3700000,
          "funding_sources": ["PMAY-G", "State Housing Board"],
          "status": "Completed",
          "progress_percentage": 100,
          "lead_agency": "Housing Construction Committee",
          "target_beneficiaries": 25,
          "actual_beneficiaries": 25,
          "key_achievements": ["All 25 houses handed over", "Sanitary latrines included"],
          "challenges": ["Material cost escalation"],
          "priority_level": "Critical"
        },
        {
          "project_id": "P033",
          "name": "Anganwadi Center Upgradation",
          "category": "Child Development",
          "description": "Upgradation of 5 anganwadi centers with better infrastructure and nutritional facilities.",
          "start_date": "2022-01-10",
          "end_date": "2022-12-31",
          "budget_allocated": 250000,
          "budget_spent": 245000,
          "funding_sources": ["ICDS", "Village Development Fund"],
          "status": "Completed",
          "progress_percentage": 100,
          "lead_agency": "Women & Child Development",
          "target_beneficiaries": 300,
          "actual_beneficiaries": 290,
          "key_achievements": ["All 5 centers upgraded", "Nutritional kits distributed"],
          "challenges": ["Staff training coordination"],
          "priority_level": "High"
        },
        {
          "project_id": "P034",
          "name": "Cattle Vaccination & Health Camp",
          "category": "Animal Husbandry",
          "description": "Mass vaccination and health checkup camps for 2000 cattle heads in the village.",
          "start_date": "2022-03-01",
          "end_date": "2022-09-30",
          "budget_allocated": 180000,
          "budget_spent": 172000,
          "funding_sources": ["Animal Husbandry Dept.", "Local Vet Association"],
          "status": "Completed",
          "progress_percentage": 100,
          "lead_agency": "Livestock Development Committee",
          "target_beneficiaries": 2000,
          "actual_beneficiaries": 1950,
          "key_achievements": ["1850 cattle vaccinated", "Health camps successful"],
          "challenges": ["Farmer participation"],
          "priority_level": "Medium"
        },
        {
          "project_id": "P035",
          "name": "Tree Plantation Drive",
          "category": "Environment",
          "description": "Plantation of 5000 trees across the village under Green India Mission.",
          "start_date": "2021-06-05",
          "end_date": "2022-05-31",
          "budget_allocated": 150000,
          "budget_spent": 145000,
          "funding_sources": ["Green India Mission", "Local Schools"],
          "status": "Completed",
          "progress_percentage": 100,
          "lead_agency": "Green Brigade",
          "target_beneficiaries": 3000,
          "actual_beneficiaries": 2800,
          "key_achievements": ["4500 trees planted", "70% survival rate"],
          "challenges": ["Watering arrangements"],
          "priority_level": "Medium"
        },
        {
          "project_id": "P036",
          "name": "Adult Literacy Campaign",
          "category": "Education",
          "description": "Literacy classes for 150 illiterate adults focusing on basic reading, writing, and numeracy skills.",
          "start_date": "2021-09-01",
          "end_date": "2022-08-31",
          "budget_allocated": 120000,
          "budget_spent": 115000,
          "funding_sources": ["Saakshar Bharat", "Volunteer Teachers"],
          "status": "Completed",
          "progress_percentage": 100,
          "lead_agency": "Adult Education Center",
          "target_beneficiaries": 150,
          "actual_beneficiaries": 140,
          "key_achievements": ["130 adults certified literate", "Follow-up classes conducted"],
          "challenges": ["Attendance consistency"],
          "priority_level": "Medium"
        },
        {
          "project_id": "P037",
          "name": "Community Radio Station",
          "category": "Information & Communication",
          "description": "Setting up a low-power community radio station to broadcast local news, agricultural information, and cultural programs.",
          "start_date": "2022-02-14",
          "end_date": "2022-11-30",
          "budget_allocated": 320000,
          "budget_spent": 310000,
          "funding_sources": ["Prasar Bharati", "Local Content Creators"],
          "status": "Completed",
          "progress_percentage": 100,
          "lead_agency": "Community Media Group",
          "target_beneficiaries": 2500,
          "actual_beneficiaries": 2300,
          "key_achievements": ["Station operational", "Regular programming schedule"],
          "challenges": ["Content generation"],
          "priority_level": "Low"
        },
        {
          "project_id": "P038",
          "name": "Sanitary Latrine Construction",
          "category": "Sanitation",
          "description": "Construction of 200 individual household latrines under Total Sanitation Campaign.",
          "start_date": "2020-10-01",
          "end_date": "2022-03-31",
          "budget_allocated": 800000,
          "budget_spent": 780000,
          "funding_sources": ["TSC", "Village Contributions"],
          "status": "Completed",
          "progress_percentage": 100,
          "lead_agency": "Sanitation Task Force",
          "target_beneficiaries": 200,
          "actual_beneficiaries": 200,
          "key_achievements": ["Open defecation free status achieved", "Usage monitoring established"],
          "challenges": ["Behavioral change"],
          "priority_level": "High"
        },
        {
          "project_id": "P039",
          "name": "Seed Bank & Grain Storage",
          "category": "Agriculture",
          "description": "Establishment of community seed bank and improved grain storage facilities for farmers.",
          "start_date": "2021-11-15",
          "end_date": "2022-10-31",
          "budget_allocated": 280000,
          "budget_spent": 270000,
          "funding_sources": ["National Seed Corporation", "FCI"],
          "status": "Completed",
          "progress_percentage": 100,
          "lead_agency": "Farmers' Cooperative",
          "target_beneficiaries": 300,
          "actual_beneficiaries": 290,
          "key_achievements": ["Seed bank operational", "Storage losses reduced by 40%"],
          "challenges": ["Quality control"],
          "priority_level": "Medium"
        },
        {
          "project_id": "P040",
          "name": "Legal Aid Clinic",
          "category": "Social Justice",
          "description": "Monthly legal aid camps providing free legal advice and document preparation services to marginalized communities.",
          "start_date": "2022-04-01",
          "end_date": "2023-03-31",
          "budget_allocated": 150000,
          "budget_spent": 145000,
          "funding_sources": ["NALSA", "District Legal Services"],
          "status": "Completed",
          "progress_percentage": 100,
          "lead_agency": "Legal Aid Committee",
          "target_beneficiaries": 400,
          "actual_beneficiaries": 380,
          "key_achievements": ["350 cases resolved", "Awareness increased"],
          "challenges": ["Follow-up on cases"],
          "priority_level": "Medium"
        }
      ]
    }
  }
}

    # ==================== SAVE DATA ====================
    def save_electricity_data(self):
        self.ensure_directories()
        data = self.get_electricity_data()
        with open(self.electricity_json, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Saved electricity data to {self.electricity_json}")

    def save_water_data(self):
        self.ensure_directories()
        data = self.get_water_data()
        with open(self.water_json, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Saved water data to {self.water_json}")

    def save_projects_data(self):
        self.ensure_directories()
        data = self.get_projects_data()
        with open(self.projects_json, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Saved projects data to {self.projects_json}")

    def save_all_data(self):
        self.save_electricity_data()
        self.save_water_data()
        self.save_projects_data()

    # ==================== LOAD DATA ====================
    def load_electricity_data(self):
        with open(self.electricity_json, 'r') as f:
            return json.load(f)

    def load_water_data(self):
        with open(self.water_json, 'r') as f:
            return json.load(f)

    def load_projects_data(self):
        with open(self.projects_json, 'r') as f:
            return json.load(f)

    # ==================== PLOT ELECTRICITY ====================
    def plot_electricity(self):
        data = self.load_electricity_data()
        entries = data["jitwarr_purr_village"]["electricity_data"]

        months = [e["month"] for e in entries]
        consumption = [e["consumption_kwh"] for e in entries]
        power_cuts = [e["power_cuts"] for e in entries]

        plt.figure(figsize=(12, 6))
        plt.bar(months, consumption, color='skyblue', alpha=0.7, label="Consumption (kWh)")
        plt.plot(months, power_cuts, color='red', marker='o', linewidth=2, label="Power Cuts")
        plt.xlabel("Month")
        plt.ylabel("Value")
        plt.title("Electricity Consumption and Power Cuts per Month")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(self.electricity_graph)
        plt.close()
        print(f"Electricity graph saved to {self.electricity_graph}")

    # ==================== PLOT WATER ====================
    def plot_water(self):
        data = self.load_water_data()
        entries = data["jitwarr_purr_village"]["water_supply_data"]

        months = [e["month"] for e in entries]
        consumption = [e["consumption_kl"] for e in entries]
        shortage_days = [e["shortage_days"] for e in entries]

        plt.figure(figsize=(12, 6))
        plt.bar(months, consumption, color='#1e90ff', alpha=0.7, label="Consumption (kL)")
        plt.plot(months, shortage_days, color='orange', marker='o', linewidth=2, label="Shortage Days")
        plt.xlabel("Month")
        plt.ylabel("Value")
        plt.title("Water Consumption and Shortage Days per Month")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(self.water_graph)
        plt.close()
        print(f"Water graph saved to {self.water_graph}")

    # ==================== PLOT PROJECTS ====================
    def plot_projects(self):
        data = self.load_projects_data()
        projects = data["jitwarr_purr_village"]["projects"]["projects_data"]

        # Count projects per category
        from collections import Counter
        categories = [p["category"] for p in projects]
        category_counts = Counter(categories)

        plt.figure(figsize=(12, 6))
        plt.bar(category_counts.keys(), category_counts.values(), color='green', alpha=0.7)
        plt.xlabel("Category")
        plt.ylabel("Number of Projects")
        plt.title("Number of Projects per Category")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(self.projects_graph)
        plt.close()
        print(f"Projects graph saved to {self.projects_graph}")

    # ==================== PLOT ALL ====================
    def plot_all(self):
        self.plot_electricity()
        self.plot_water()
        self.plot_projects()