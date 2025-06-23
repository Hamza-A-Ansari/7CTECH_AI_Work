instructions = f""" 
**intructions** : The input contains product reviews for fashion clothing. Your task is to summarize the reviews in two parts:

1. **summary:** Provide a maximum of 2 to 3 sentence summary focusing only on the fit of the products. Avoid mentioning occasions, events, or reasons for purchasing. Include any positive feedback about product fit and quality.

2. **keywords:** Extract maximum 4 to 5 top used keywords from reviews related to product fit only. Avoid mentioning its festures like color, category etc

**Note**: 
1 : Use only 'summary' and 'keywords' as dictionary keys, and the response should be in dictionary format only.
2 : You want to generate a summary like 'customers mentioned' and it should be in singular form, referring to the product as a single item so instead of saying "The/These product are" you should say "This product is".
3 : If there is having any problem in reviews given to you 'summary' key and 'keywords' key should be empty and exclude any other information or note.
4 : Remember not to include any information about occasions, events, or reasons for purchasing strictly and full focus should be on product fit

**Output Format <dictionary format> :** 
{{
    summary: "<summary of fit>",
    "keywords": ["<keyword1>", "<keyword2>", ...]
}}
"""