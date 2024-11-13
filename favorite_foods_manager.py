favorite_foods = [] # initializing empty list to store favorite foods here

while True:
    print('Welcome to Favorite Foods Manager!!')
    print('0. Exit')
    print('1. Add favorite food')
    print('2. Remove favorite food')
    print('3. View all favorite foods')

    choice = input('Select an option: ') # taking option choice input from user here

    if choice == '0':
        print('Thank you for using Favorite Foods Manager!!\n')
        break

    elif choice == '1':
        food = input('Enter the name of your favorite food: ')

        favorite_foods.append(food)
        print(f'{food} added successfully!!\n')

    elif choice == '2':
        food = input('Enter the name of a food you want to remove: ')

        if food in favorite_foods:
            favorite_foods.remove(food)
            print(f'{food} removed successfully!!\n')
        else:
            print(f'{food} was not found in the list!!\n')

    elif choice == '3':
        if favorite_foods:
            print('Your favorite foods are: ')
            for i, food in enumerate(favorite_foods, 1):
                print(f'{i}. {food}')
            print('')
        else:
            print('No favorite food added yet!!\n')

    else:
        print('Invalid Choice!!\n')
