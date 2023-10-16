from langchain.prompts import PromptTemplate


prompt0_en_baseline = PromptTemplate(
    input_variables=["p1", "p2"],
    template=
     """Could you please tell me if the following two products are the same one?
Product 1: {p1}
Product 2: {p2}

Please answer my question only with True or False."""
)

prompt1_en_short_mustafa = PromptTemplate(
    input_variables=["p1", "p2"],
    template=
     """Are the following two products the same?
Product 1: {p1}
Product 2: {p2}

Answer with 'True' or 'False'."""
)

prompt2_en_short_mustafa = PromptTemplate(
    input_variables=["p1", "p2"],
    template=
     """Are the following two products the same?
Product 1: {p1}
Product 2: {p2}

Answer with 'True' or 'False.'"""
)


prompt_1_zero_shot_CoT = PromptTemplate(
    input_variables=["p1", "p2"],
    template="""Could you please tell me if the following two products are the same one?
Product 1: {p1}
Product 2: {p2}

Please answer my question with Yes or No. Lets think step by step."""
)

# product1 = "Title: " + cut_length(str(df["title_left"][1] or "none")) + "\nDescription: " + cut_length(str(df["description_left"][1] or "none"))


prompt_2_zeroshot_rules_ralph = PromptTemplate(
    input_variables=["p1", "p2"],
    template="""Your task is to decide if two product descriptions refer to the same product.

The following rules regarding product features need to be observed:

1. The brand of matching products must be the same if available
2. Model names of matching products must be the same if available
3. Model numbers of matching products must be the same if available
4. Additional features of matching products must be the same if available

Do the following two product descriptions refer to the same real-world product? Answer with 'Yes' if they do and 'No' if they do not.
Product 1: {p2}
Product 2: {p1}
"""
)



# product1 = "Title: " + cut_length(str(df["title_left"][1] or "none")) + "\nDescription: " + cut_length(str(df["description_left"][1] or "none")) + "\nBrand:" + str(df["brand_left"][1] or "none") 





# evalPrompts

evalPrompt_1 = PromptTemplate(
    input_variables=["chain_of_thought_reasoning"],
    template="""The following text is the answer and reasoning if two product descriptions refer to the same product. 
    Please evaluate if the the overall conclusion is that the two products match or not.
    Your answer should be either "match" or "no match".
    Answer: {chain_of_thought_reasoning}
"""
)