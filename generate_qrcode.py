import qrcode

def generate_upi_qr():
    """Function to generate UPI QR code"""
    link = input("Enter Your UPI ID: ").strip()
    name = input("Enter Your Name: ").strip()
    
    if not link or not name:
        print("Error: UPI ID and Name cannot be empty!")
        return
    
    # format upi id 
    upi_id_code_format = f"upi://pay?pa={link}&pn={name}&mc=1234"
    
    # generate qr code
    upi_code = qrcode.make(upi_id_code_format)
    
    #save qrcode
    upi_code.save('UPI_QR.png')
    print("UPI QR Code saved as 'UPI_QR.png'")
    
    #show code
    upi_code.show()

def generate_link_qr():
    """Function to generate Link QR code"""
    link = input("Enter Link: ").strip()
    
    if not link:
        print("Error: Link cannot be empty!")
        return
    
    # format link
    if ("https" in link):formatedlink = link
    else:formatedlink = "https://"+link
    
    # generate qr code
    link_code = qrcode.make(formatedlink)
    
    # save qr
    link_code.save('Link_QR.png')
    
    print("Link QR Code saved as 'Link_QR.png'")
    
    # show qr
    link_code.show()

def main():
    """Main function to handle user input"""
    while True:
        print("\nChoose an option:")
        print("1 - Generate UPI QR Code")
        print("2 - Generate Link QR Code")
        print("3 - Exit")
        
        try:
            choice = int(input("Enter Your Choice: ").strip())
            
            if choice == 1:
                generate_upi_qr()
            elif choice == 2:
                generate_link_qr()
            elif choice == 3:
                print("Exiting program...")
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
        
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
