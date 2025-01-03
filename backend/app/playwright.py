from playwright.async_api import async_playwright, Error as PlaywrightError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def scrape_business(business_name):
    results = []
    url = "https://search.sunbiz.org/Inquiry/CorporationSearch/ByName"
    
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
            page = await browser.new_page()
            
            try:
                await page.goto(url)
                logging.info("Page loaded successfully.")
            except PlaywrightError as e:
                logging.error(f"Failed to load page: {e}")
                return results

            try:
                await page.fill("input#SearchTerm", business_name)
                await page.click("input[type='submit'][value='Search Now']")
                logging.info(f"Searched for business name: {business_name}")
            except PlaywrightError as e:
                logging.error(f"Failed to interact with the search form: {e}")
                return results

            try:
                await page.wait_for_selector("table", timeout=10000)
                rows = await page.query_selector_all("table tr")
                logging.info(f"Number of rows found: {len(rows)}")
            except PlaywrightError as e:
                logging.error(f"Failed to find or load the results table: {e}")
                return results

            for row in rows[1:]:
                try:
                    cols = await row.query_selector_all("td")
                    if len(cols) >= 3:
                        business_name = (await cols[0].inner_text()).strip()
                        doc_number = (await cols[1].inner_text()).strip() if len(cols) > 1 else None
                        status = (await cols[2].inner_text()).strip() if len(cols) > 2 else None
                        logging.info(f"Scraped row: {business_name}, {doc_number}, {status}")

                        results.append({
                            "business_name": business_name,
                            "doc_number": doc_number,
                            "status": status,
                            "registration_date": None,  
                            "state_of_formation": "",  
                        })
                except PlaywrightError as e:
                    logging.warning(f"Error processing row: {e}")
            
            await browser.close()

    except PlaywrightError as e:
        logging.error(f"Error launching browser or interacting with Playwright: {e}")
    
    logging.info(f"Final results: {results}")
    return results
