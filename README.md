# **Objective**

The project aimed to evaluate real estate listings on the most popular online marketplace in Albania, [Merrjep](http://www.merrjep.al).  

# Context

The real estate market has always been one of the main methods of investments for Albania. Prices for real estate have seen a steady rise in recent years, much to the chagrin of the residents in Tirana, where the majority of the market exists.

# Approach

## Data Collection

Using Python and the BeautifulSoup library to build a web scraper which collected listings from last 100 pages of Merrjep’s [real estate section](https://www.merrjep.al/njoftime/imobiliare-vendbanime/ne-shitje-kerkoj-te-blej-me-qera-kerkohet-me-qera). 

## Data Cleaning

Data cleaning was necessary firstly for undefined characters.  The date and surface values were changed to a more functional formatting. Information was normalized so each listing had the same attributes.

## **Exploratory Analysis**

With a standardized dataset of 5000 listings scraped from 2023 to July 2024, the data still needed to be queried efficiently to remove outliers. There were a lot of cases of missing basic information (price or surface), and quite a number of duplicate listings. For this reason the data was queried based on:

- Price between 4_000 and 2_000_000 EUR
- Surface between 45 and 1_000 square meters
- Only listings in EUR
- Only listings for sale (no units for rent)
    
    ### Price Trends
    
    From early 2023 to Jul 2024, there is an increase of around 12% to the average price per square meter in Tirana. This is in line with [observed market trends](https://www.monitor.al/cmimet-e-apartamenteve-ne-kryeqytet-shtrenjtohen-deri-ne-30-brenda-nje-viti-kryeson-periferia/).
    
    ![image](https://github.com/user-attachments/assets/8b5623ee-65f6-4464-bef9-6e57bf3072b7)
    
    ### Price Distributions
    
    From around 850 listings, less than half of those have a maximum listing price of 120_000 EUR. Approx. 20% of listings fall into the most expensive price category. 
    
    With an average salary for residents of Tirana of around [700 EUR](https://www.instat.gov.al/media/12918/vjetari-statistikor-rajonal-2023__.pdf) and a minimal monthly loan of around [570 EUR](https://www.tiranabank.al/c/23/perllogaritje-e-kredise) (even higher if 100% financing required), the cost of ownership for a new family would be around 40% of their earnings. This is higher than the usually recommended 30% and it includes only the loan repayment to the bank (other expenses like life insurance not included)
    

    ![image](https://github.com/user-attachments/assets/bb5f7c03-91de-41da-9207-23a612742b9e)

# Conclusion

The unaffordability of current real estate prices for an average family does suggest a price bubble. But the underlying reasons for this bubble are definitely multi-faceted and merit further analysis such as current fiscal and social policies.

- Around [33% of current residencies are uninhabited](https://www.instat.gov.al/media/13626/cens-2023-census-botim.pdf).
- Around [26% of residencies are bought from non-residents](https://www.bankofalbania.org/rc/doc/Vrojtim_mbi_Ecurine_e_Tregut_te_Pasurive_te_Paluajtshme_ne_Shqiperi_6MII_2023_27288.pdf), where a third of them are non-EU.
