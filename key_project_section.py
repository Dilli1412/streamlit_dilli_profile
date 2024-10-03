st.subheader("Key Projects")
    projects = [
        {
            "name": "ERPNext Implementation for Manufacturing Firm",
            "description": "Led the end-to-end implementation of ERPNext for a mid-sized manufacturing company, resulting in a 40% improvement in inventory management and a 25% reduction in production lead times.",
        },
        {
            "name": "Custom ERP Module Development",
            "description": "Spearheaded the development of custom ERP modules for specific client needs, including a specialized quality control system that increased product consistency by 30%.",
        },
        {
            "name": "Searates ERP Global Implementation",
            "description": "Managed the implementation of Searates ERP for multiple international clients in the logistics sector, resulting in a 30% increase in operational efficiency and improved global shipment tracking capabilities.",
        },
    ]
    
    for project in projects:
        with st.expander(project["name"]):
            st.write(project["description"])