# Data Warehouse and OLAP Cube for Car Dealership

A complete data warehouse project built for a car dealership case study.  
The project includes dimensional modelling, implementation of a star schema in SQL Server and construction of an OLAP cube in SQL Server Analysis Services (SSAS).

## Scope of the project

1. Dimensional modelling  
   - Star schema design  
   - Fact table: FactZamowienie  
   - Dimension tables: DimCzas, DimKlienci, DimPracownicy, DimSalon, DimSamochod  

2. SQL implementation  
   - Creation of all dimension and fact tables  
   - Primary and foreign key relationships  
   - Sample data inserted for analytical testing  

3. Data warehouse structure  
   - Separate DWH database created in SQL Server  
   - Logical separation of dimensions and fact  
   - Data prepared for OLAP processing  

4. OLAP Cube (SSAS)  
   - Data Source and Data Source View configuration  
   - Cube creation with measures and attributes  
   - Deployment to SSAS server  
   - Basic browsing and validation of measures and hierarchies  

## Purpose

The project demonstrates the full process of building a small-scale Business Intelligence solution:
- modelling data for analytical use,
- implementing a star schema,
- organising a data warehouse in SQL Server,
- creating and deploying an OLAP cube.

## Files

- `SQL_PROJEKT_1.pdf` – dimensional modelling and schema design  
- `SQL_PROJEKT_2.pdf` – SQL implementation of the data warehouse  
- `SQL_PROJEKT_2_KOSTKA_OLAP.pdf` – OLAP cube configuration and deployment guide

