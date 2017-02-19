import gedcom
import US04
FILE_PATH = './Gedcom1.ged'
if __name__ == '__main__':
    gedcom.parse(FILE_PATH)
    
    print('\nIndividuals')
    gedcom.print_individuals()
    print('\nFamilies')
    gedcom.print_families()
    
    US04.US4MbD()
