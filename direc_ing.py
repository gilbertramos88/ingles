print("hi world")


import difflib

nameCodingJobs = {1:"Photo Software", 2:"Apps Developer", 3:"Social Network Development", 4:"Databases", 5:"Operating Systems", 6:"Game Development"}



listPhotoSoftware = ["Resolution", "Exposure", "Histogram", "Saturation", "Sharpening", "White balance", "Noise reduction", "Contrast", "Filter", "Crop",
                    "Clone stamp", "Layer", "Masking", "Aspect ratio", "Metadata"]

listAppsDeveloper = ["Frontend", "Backend", "Framework", "API", "Database", "User Interface", "User Experience", "DevOps", "Continuous Integration", 
                     "Debugging", "Version Control", "Repository", "Middleware", "Deployment", "Scalability"]

listSocialNetworkDevelopment = ["Interface", "Experience", "Users", "Platform", "Moderation", "Security", "Privacy", "Scalability", "Application", 
                                "Authentication", "Design", "Communities", "Interaction", "Content", "Analytics"]

listDatabases = ["Table", "Query", "Index", "Primary key", "Foreign key", "View", "Join", "Normalization", "Denormalization", "Unique Index"]

listOperatingSystems = ["Thread", "System call", "Memory management", "Device driver", "File system", "Synchronization", "Multitask", "I/O management", 
                        "Shell", "API", "Boot loader", "Filesystem hierarchy", "Firmware", "Paging", "Throughput"]

listGameDevelopment = ["Designer", "Programmers", "Artists", "Animators", "Sound engineers", "Writers", "Testers", "Producers", "Level designers", "UI/UX", 
                       "Narrative designers", "QA specialists", "Developers", "Concept artists", "Composers"]



dictPhotoSoftware = {"Resolution":"ˌrɛzəˈluːʃᵊn", "Exposure":"ɪkˈspəʊʒə", "Histogram":"ˈhɪsˈtəgræm", "Saturation":"ˌsæʧəˈreɪʃᵊn", 
                     "Sharpening":"ˈʃɑːpᵊnɪŋ", "White balance":"waɪt ˈbælᵊns", "Noise reduction":"nɔɪz rɪˈdʌkʃᵊn", "Contrast":"ˈkɒntrɑːst", 
                     "Filter":"ˈfɪltə", "Crop":"krɒp", "Clone stamp":"kləʊn stæmp", "Layer":"ˈleɪə", "Masking":"ˈmɑːskɪŋ", 
                     "Aspect ratio":"ˈæspɛkt ˈreɪʃiəʊ", "Metadata":"ˈmɛtəˌdeɪtə"}

dictAppsDeveloper = {"Frontend":"frʌntɛnd", "Backend":"ˌbækˈɛnd", "Framework":"ˈfreɪmwɜːk", "API":"eɪ-piː-aɪ", "Database":"ˈdeɪtəbeɪs", 
                    "User Interface":"ˈjuːzər ˈɪntəfeɪs", "User Experience":"ˈjuːzər ɪkˈspɪəriəns", "DevOps":"dɛv ɒps", 
                    "Continuous Integration":"kənˈtɪnjuəs ˌɪntɪˈɡreɪʃᵊn", "Debugging":"diːˈbʌɡɪŋ", "Version Control":"ˈvɜːʒᵊn kənˈtrəʊl", 
                    "Repository":"rɪˈpɒzɪtᵊri", "Middleware":"ˈmɪdᵊl weə", "Deployment":"dɪˈplɔɪmənt", "Scalability":"skeɪləˈbɪləti"}

dictSocialNetworkDevelopment = {"Interface":"ˈɪntəfeɪs", "Experience":"ɪkˈspɪəriəns", "Users":"ˈjuːzəz", "Platform":"ˈplætfɔːm", 
                                "Moderation":"ˌmɒdəˈreɪʃᵊn", "Security":"sɪˈkjʊərəti", "Privacy":"ˈprɪvəsi", "Scalability":"skeɪləˈbɪləti", 
                                "Application":"ˌæplɪˈkeɪʃᵊn", "Authentication":"ɔːˌθɛntɪˈkeɪʃᵊn", "Design":"dɪˈzaɪn", "Communities":"kəˈmjuːnətiz", 
                                "Interaction":"ˌɪntəˈrækʃᵊn", "Content":"ˈkɒntɛnt", "Analytics":"ˌænəˈlɪtɪks"}

dictDatabases = {"Table":"ˈteɪbᵊl", "Query":"ˈkwɪəri", "Index":"ˈɪndɛks", "Primary key":"ˈpraɪmᵊri kiː", "Foreign key":"ˈfɒrən kiː", 
                        "View":"vjuː", "Join":"ʤɔɪn", "Normalization":"ˌnɔːməlaɪˈzeɪʃᵊn", "Denormalization":"diːˌnɔːməlaɪˈzeɪʃᵊn", 
                        "Unique Index":"juːˈniːk ˈɪndɛks"}

dictOperatingSystems = {"Thread":"θrɛd", "System call":"ˈsɪstəm kɔːl", "Memory management":"ˈmɛmᵊri ˈmænɪʤmənt", "Device driver":"dɪˈvaɪs ˈdraɪvə", 
                        "File system":"faɪl ˈsɪstəm", "Synchronization":"ˌsɪŋkrənaɪˈzeɪʃᵊn", "Multitask":"ˌmʌltɪˈtɑːsk", 
                        "I/O management":"aɪ/əʊ ˈmænɪʤmənt", "Shell":"ʃɛl", "API":"eɪ-piː-aɪ", "Boot loader":"buːt ˈləʊdə", 
                        "Filesystem hierarchy":"faɪlˈsɪstəm ˈhaɪərɑːki", "Firmware":"ˈfɜːmweə", "Paging":"ˈpeɪʤɪŋ", "Throughput":"ˈθruːpʊt"}

dictGameDevelopment = {"Designer":"dɪˈzaɪnə", "Programmers":"ˈprəʊɡræməz", "Artists":"ˈɑːtɪsts", "Animators":"ˈænɪmeɪtəz", 
                       "Sound engineers":"saʊnd ˌɛnʤɪˈnɪəz", "Writers":"ˈraɪtəz", "Testers":"ˈtɛstəz", "Producers":"prəˈdjuːsəz", 
                       "Level designers":"ˈlɛvᵊl dɪˈzaɪnəz", "UI/UX":"juː-aɪ/juː-ɛks", "Narrative designers":"ˈnærətɪv dɪˈzaɪnəz", 
                       "QA specialists":"kjuː-eɪ ˈspɛʃᵊlɪsts", "Developers":"dɪˈvɛləpəz", "Concept artists":"ˈkɒnsɛpt ˈɑːtɪsts", 
                       "Composers":"kəmˈpəʊzəz"}



categories = {
    1: (listPhotoSoftware, dictPhotoSoftware),
    2: (listAppsDeveloper, dictAppsDeveloper),
    3: (listSocialNetworkDevelopment, dictSocialNetworkDevelopment),
    4: (listDatabases, dictDatabases),
    5: (listOperatingSystems, dictOperatingSystems),
    6: (listGameDevelopment, dictGameDevelopment)
}

def correct_spelling(word, word_list):
    matches = difflib.get_close_matches(word, word_list)
    return matches[0] if matches else None

def main():
    while True:
        print("Choose a Coding Job Category (Only numbers):")
        for key, value in nameCodingJobs.items():
            print(f"{key}: {value}")
       
        choice = input("Enter the category number or name: ").strip()
       
        try:
            if choice.isdigit():
                choice = int(choice)
                if choice in nameCodingJobs:
                    category_name = nameCodingJobs[choice]
                else:
                    raise ValueError
            else:
                category_name = next((name for number, name in nameCodingJobs.items() if name.lower() == choice.lower()), None)
                if category_name is None:
                    raise ValueError
           
            category_list, category_dict = categories[choice]
            print(f"Words in the category '{category_name}':")
            print(", ".join(category_list))
           
            while True:
                word = input("Type a word from the list: ").strip()
               
                if word in category_dict:
                    print(f"The pronunciation of '{word}' is: {category_dict[word]}")
                    break
                else:
                    correct_word = correct_spelling(word, category_list)
                    if correct_word:
                        print(f"Word not found. Did he mean '{correct_word}'?")
                    else:
                        print("Word not found and no suggestion found nearby. Please try again.")
        except ValueError:
            print("Ticket not valid. Try again.")
       
        another = input("You want to choose another category? (Y/N): ").strip().lower()
        if another not in ('sí', 'si', 's', 'yes', 'yeah', 'y'):
            print("Thank you for using the program!")
            break

if __name__ == "__main__":
    main()