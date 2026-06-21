
print("=" * 50)
print("        COLLEGE COUNSELOR AI AGENT")
print("=" * 50)

# ==========================
# FUNCTIONS
# ==========================

def calculate_percentage(obtained, total):
    return (obtained / total) * 100


def validate_rank(rank):
    return rank > 0


def recommend_colleges(exam, interest, rank, percentage):

    colleges = []

    # ==========================
    # EAMCET
    # ==========================
    if exam == "EAMCET":

        if interest == "CSE":
            if rank < 2000:
                colleges = [
                    (
                        "JNTU Kakinada",
                        "Kakinada",
                        "CSE Available",
                        "₹45,000/year",
                        "0884-2300900"
                    ),
                    (
                        "Andhra University",
                        "Visakhapatnam",
                        "CSE Available",
                        "₹50,000/year",
                        "0891-2844000"
                    )
                ]

            elif rank < 6000:
                colleges = [
                    (
                        "Gayatri Vidya Parishad",
                        "Visakhapatnam",
                        "CSE Available",
                        "₹55,000/year",
                        "0891-2739144"
                    ),
                    (
                        "VIT-AP",
                        "Amaravati",
                        "CSE Available",
                        "₹1,50,000/year",
                        "0863-2370444"
                    )
                ]

            else:
                colleges = [
                    (
                        "GMRIT",
                        "Srikakulam",
                        "CSE Available",
                        "₹70,000/year",
                        "08942-246167"
                    ),
                    (
                        "RVR and JC College",
                        "Guntur",
                        "CSE Available",
                        "₹65,000/year",
                        "0863-2283399"
                    )
                ]

        elif interest == "AI-ML":
            if rank < 5000:
                colleges = [
                    (
                        "Andhra University",
                        "Visakhapatnam",
                        "AI-ML Available",
                        "₹50,000/year",
                        "0891-2844000"
                        ),
                    (
                        "GVPCE",
                        "Visakhapatnam",
                        "AI-ML Available",
                        "₹60,000/year",
                        "0891-2739144"
                        )
                ]
            else:
                colleges = [
                    (
                        "GMRIT",
                        "Srikakulam",
                        "AI-ML Available",
                        "₹70,000/year",
                        "08942-246167"
                        ),
                    (
                        "VIT-AP",
                        "Amaravati",
                        "AI-ML Available",
                        "₹1,50,000/year",
                        "0863-2370444")
                ]

        elif interest == "ECE":
            if rank < 3500:
                colleges = [
                    (
                        "JNTU Kakinada",
                        "Kakinada",
                        "ECE Available",
                        "₹45,000/year",
                        "0884-2300900"
                        ),
                    (
                        "Andhra University",
                        "Visakhapatnam",
                        "ECE Available",
                        "₹50,000/year",
                        "0891-2844000"
                        )
                ]
            else:
                colleges = [
                    (   
                        "GVPCE",
                        "Visakhapatnam",
                        "ECE Available",
                        "₹60,000/year",
                        "0891-2739144"
                        ),
                    (
                        "SRKR Engineering College",
                        "Bhimavaram",
                        "ECE Available",
                        "₹55,000/year",
                        "08816-223332"
                        )
                ]

    # ==========================
    # WBJEE
    # ==========================
    elif exam == "WBJEE":

        if interest == "CSE":
            if rank < 1000:
                colleges = [
                    (
                          "Jadavpur University",
                        "Kolkata",
                        "CSE Available",
                        "₹40,000/year",
                        "033-24572222"
                        )
                ]

            elif rank < 5000:
                colleges = [
                    (
                        "Heritage Institute of Technology",
                        "Kolkata",
                        "CSE Available",
                        "₹80,000/year",
                        "033-66270600"
                        ),
                    (
                        "Techno Main Salt Lake",
                        "Kolkata",
                        "CSE Available",
                        "₹75,000/year",
                        "033-23572950"
                        )
                ]

            else:
                colleges = [
                    (
                        "Haldia Institute of Technology",
                        "Haldia",
                        "CSE Available",
                        "₹70,000/year",
                        "03224-252900"
                        )
                ]

        elif interest == "AI-ML":
            colleges = [
                (
                    "Heritage Institute of Technology",
                    "Kolkata",
                    "AI-ML Available",
                    "₹80,000/year",
                    "033-66270600"
                    ),
                (
                    "IEM Kolkata",
                    "Kolkata",
                    "AI-ML Available",
                    "₹75,000/year",
                    "033-23572995"
                    )
            ]

        elif interest == "ECE":
            colleges = [
                (  
                    "Jadavpur University",
                    "Kolkata",
                    "ECE Available",
                    "₹40,000/year",
                    "033-24572222"
                    ),
                (
                    "IEM Kolkata",
                    "Kolkata",
                    "ECE Available",
                    "₹75,000/year",
                    "033-23572995"
                    )
            ]

    # ==========================
    # JEE MAIN
    # ==========================
    elif exam == "JEE MAIN":

        if percentage < 75:
            print("\nWARNING: You may not satisfy IIT/NIT eligibility criteria.")
            print("Please verify the latest JoSAA rules.")

            colleges = []
        else:
            if rank < 5000:
                colleges = [
                    (
                        "NIT Trichy",
                        "Tiruchirappalli",
                        "CSE Available",
                        "₹85,000/year",
                        "0431-2503000"
                        ),
                    (
                        "NIT Surathkal",
                        "Mangalore",
                        "CSE Available",
                        "₹80,000/year",
                        "0824-2474000"
                        )
                ]

            elif rank < 15000:
                colleges = [
                    (
                        "VNIT Nagpur",
                        "Nagpur",
                        "CSE Available",
                        "₹82,000/year",
                        "0712-2801566"
                        ),
                    (
                        "NIT Durgapur",
                        "Durgapur",
                        "CSE Available",
                        "₹78,000/year",
                        "0343-2752000"
                        )
                ]

            else:
                colleges = [
                    (   
                        "IIIT Bhubaneswar",
                        "Bhubaneswar",
                        "CSE Available",
                        "₹80,000/year",
                        "0674-6636555"
                        ),
                    (
                        "Newer NITs",
                        "Various Locations",
                        "CSE Available",
                        "₹75,000/year",
                        "Check Official Website"
                        )
                ]

    # ==========================
    # JEE ADVANCED
    # ==========================
    elif exam == "JEE ADVANCED":

        if percentage < 75:
                print("\nWARNING: You may not satisfy IIT eligibility criteria.")
                print("Please verify the latest IIT admission rules.")
                colleges = []
        else:
            if rank < 2000:
                colleges = [
                    (
                        "   IIT Bombay",
                        "Mumbai",
                        "CSE Available",
                        "₹90,000/year",
                        "022-25722545"
                        ),
                    (
                        "IIT Delhi",
                        "New Delhi",
                        "CSE Available",
                        "₹88,000/year",
                        "011-26591727"
                        ),
                    (
                        "IIT Madras",
                        "Chennai",
                        "CSE Available",
                        "₹85,000/year",
                        "044-22578000"
                        )
                ]

            elif rank < 6000:
                colleges = [
                    (
                        "IIT Kharagpur",
                        "Kharagpur",
                        "CSE Available",
                        "₹85,000/year",
                        "03222-255221"
                        ),
                    (
                        "IIT Roorkee",
                        "Roorkee",
                        "CSE Available",
                        "₹82,000/year",
                        "01332-285311"
                        )
                ]

            else:
                colleges = [
                    (
                         "IIT ISM Dhanbad",
                        "Dhanbad",
                        "CSE Available",
                        "₹80,000/year",
                        "0326-2235001"
                        ),
                    (
                        "IIT Jammu",
                        "Jammu",
                        "CSE Available",
                        "₹78,000/year",
                        "0191-2570631"
                        )
                ]

    return colleges


# ==========================
# USER INPUT
# ==========================

print("\nEnter Intermediate Details")

board = input("Board (CBSE/ICSE/STATE BOARD): ").upper()
stream = input("Stream (MPC/BIPC/COMMERCE/ARTS): ").upper()

total_marks = float(input("Total Marks: "))
obtained_marks = float(input("Marks Obtained: "))

percentage = calculate_percentage(
    obtained_marks,
    total_marks
)

if percentage < 35:
    print("\nWARNING:")
    print("Percentage is below 35%. Please verify your marks.")



print("\nEnter Entrance Exam Details")

exam = input(
    "Exam (EAMCET/WBJEE/JEE MAIN/JEE ADVANCED): "
).upper()

rank = int(input("Rank: "))

if not validate_rank(rank):
    print("Invalid Rank!")
    exit()

interest = input(
    "Branch (CSE/AI-ML/ECE): "
).upper()

# ==========================
# RESULTS
# ==========================

colleges = recommend_colleges(
    exam,
    interest,
    rank,
    percentage
)

print("\n" + "=" * 50)
print("PROFILE SUMMARY")
print("=" * 50)

print(f"Board      : {board}")
print(f"Stream     : {stream}")
print(f"Percentage : {percentage:.2f}%")
print(f"Exam       : {exam}")
print(f"Rank       : {rank}")
print(f"Interest   : {interest}")

print("\nRecommended Colleges:\n")

if len(colleges) == 0:
    print("No college recommendations available.")
else:
    for college, location, branch, fee, contact in colleges:
        print(f"• {college}")
        print(f"  Location : {location}")
        print(f"  Branch   : {branch}")
        print(f"  Fee      : {fee}")
        print(f"  Contact  : {contact}")
        print()

print("Thank you for using College Counselor AI Agent!")

