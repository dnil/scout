import pkg_resources

###### Files ######

# Gene sources:
hgnc_file = 'demo/resources/hgnc_reduced_set.txt.gz'
exac_file = 'demo/resources/forweb_cleaned_exac_r03_march16_z_data_pLI_reduced.txt.gz'
transcripts37_file = 'demo/resources/ensembl_transcripts_reduced.txt.gz'

# OMIM resources:
mim2gene_file = 'demo/resources/mim2gene_reduced.txt.gz'
genemap2_file = 'demo/resources/genemap2_reduced.txt.gz'

# Hpo resources
hpogenes_file = 'demo/resources/ALL_SOURCES_ALL_FREQUENCIES_genes_to_phenotype_reduced.txt.gz'
hpoterms_file = 'demo/resources/ALL_SOURCES_ALL_FREQUENCIES_phenotype_to_genes_reduced.txt.gz'
hpo_phenotype_to_terms = 'demo/resources/ALL_SOURCES_ALL_FREQUENCIES_diseases_to_genes_to_phenotypes_reduced.txt.gz'

# Additional resources
madeline_file = 'demo/madeline.xml'

###### Paths ######

# Gene paths
hgnc_reduced_path = pkg_resources.resource_filename('scout', hgnc_file)
exac_reduced_path = pkg_resources.resource_filename('scout', exac_file)
transcripts37_reduced_path = pkg_resources.resource_filename('scout', transcripts37_file)
transcripts38_reduced_path = pkg_resources.resource_filename('scout', transcripts37_file)

# OMIM paths
mim2gene_reduced_path = pkg_resources.resource_filename('scout', mim2gene_file)
genemap2_reduced_path = pkg_resources.resource_filename('scout', genemap2_file)

# Hpo paths
hpogenes_reduced_path = pkg_resources.resource_filename('scout', hpogenes_file)
hpoterms_reduced_path = pkg_resources.resource_filename('scout', hpoterms_file)
hpo_phenotype_to_terms_reduced_path = pkg_resources.resource_filename('scout', hpo_phenotype_to_terms)

# Additional paths
madeline_path = pkg_resources.resource_filename('scout', madeline_file)
