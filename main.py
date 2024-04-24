from selenium import webdriver
from selenium.webdriver.common.by import By
import time

start_url = "https://www.jnec.edu.bt/en/"

# driver.add_cookie({'name': 'JNEC', 'value': 'No Access to unauthorized users!'})

driver = webdriver.Edge()
driver.get(start_url)
time.sleep(5)


def Breadth_first_Search():
    driver.get(start_url)
    links = driver.find_elements(By.TAG_NAME, 'a')

    internal_links = []
    external_links = []

    for link in links:
        href = link.get_attribute('href')

        if href:
            if start_url in href:
                internal_links.append(link.get_attribute('href'))

            else:
                external_links.append(link.get_attribute('href'))

    print("Internal_links:")
    for internal_link in internal_links:
        print(internal_link)
    internals = len(internal_links)
    print(f"Total internal_links:{internals}")

    print("\nExternal_links:")
    for external_link in external_links:
        print(external_link)
    externals = len(external_links)
    print(f"Total external_links:{externals}")
    print("\n")


def extract_svg(jnec):
    driver.get(jnec)
    svg_content = driver.execute_script('return document.getElementsByTagName("a")[0]')
    print(svg_content)
    print("Here is Issue on Extracting Images.")


def image_urls():
    driver.get(start_url)
    img_links = driver.find_elements(By.TAG_NAME, 'img')
    for img_link in img_links:
        print(img_link.get_attribute('src'))
        print(img_link.get_attribute('alt'))
    print("\n Here is the Visited links")

def visit_all_links_in_depth(url, max_depth=3, visited=None, depth=0):
    if visited is None:
        visited = set()
    if depth > max_depth:
        return

    driver = webdriver.Chrome()

    driver.get(url)
    print("Visited:", url)
    visited.add(url)

    anchor_tags = driver.find_elements(By.TAG_NAME, 'a')

    for anchor_tag in anchor_tags:
        href = anchor_tag.get_attribute('href')
        if href and href not in visited:
            visit_all_links_in_depth(href, max_depth, visited, depth + 1)

max_depth = 3

if __name__ == '__main__':
    print(driver.current_url)
    Breadth_first_Search()
    image_urls()
    extract_svg(start_url)
    visit_all_links_in_depth(start_url, max_depth)