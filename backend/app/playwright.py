from playwright.async_api import async_playwright

async def scrape_business(business_name):
    results = []
    url = "https://search.sunbiz.org/Inquiry/CorporationSearch/ByName"
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = await browser.new_page()

        # Navigate to the search page
        await page.goto(url)
        print("Page loaded successfully.")

        # Fill the search input and submit the form
        await page.fill("input#SearchTerm", business_name)
        await page.click("input[type='submit'][value='Search Now']")
        print(f"Searched for business name: {business_name}")

        # Wait for the results table to load
        await page.wait_for_selector("table", timeout=10000)

        # Extract rows from the results table
        rows = await page.query_selector_all("table tr")
        print(f"Number of rows found: {len(rows)}")

        # Iterate over rows, skipping the header row
        for row in rows[1:]:
            cols = await row.query_selector_all("td")
            if len(cols) >= 3:
                business_name = (await cols[0].inner_text()).strip()
                doc_number = (await cols[1].inner_text()).strip() if len(cols) > 1 else None
                status = (await cols[2].inner_text()).strip() if len(cols) > 2 else None
                print(f"Scraped row: {business_name}, {doc_number}, {status}")

                # Append the result
                results.append({
                    "business_name": business_name,
                    "doc_number": doc_number,
                    "status": status,
                    "registration_date": None,  # Update if date is available
                    "state_of_formation": "",  # Update if state is available
                })

        # Close the browser
        await browser.close()

    print(f"Final results: {results}")
    return results
