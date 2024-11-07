import pandas as pd

# Define file paths
input_excel = 'Sequencing_StoolV3V4.xlsx'  # Input Excel file
output_fasta = 'Sequencing_StoolV3V4.fasta'  # Output FASTA file

# Read the Excel file
data = pd.read_excel(input_excel)

# Open the output FASTA file for writing
with open(output_fasta, mode='w') as fasta_file:
    for index, row in data.iterrows():
        # Extract the ID and sequence from each row
        sequence_id = row['ID']
        sequence = row['Sequence']
        
        # Write to the FASTA file
        fasta_file.write(f'>{sequence_id}\n')
        fasta_file.write(f'{sequence}\n')

print(f'FASTA file has been created at {output_fasta}')
