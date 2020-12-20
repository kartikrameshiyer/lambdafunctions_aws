import boto3  # install boto3 package


def action(phrase=input("please enter the phrase: ")):
    client = boto3.client('translate', region_name="us-west-2")
    #phrase = "Hola mi nombre es kartik"
    result = client.translate_text(Text=phrase,SourceLanguageCode="auto",
            TargetLanguageCode="en")                           
    text = result['TranslatedText']                               
    print(f"In english: {text}")

if __name__=='__main__':
    action()


