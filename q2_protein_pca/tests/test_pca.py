import skbio
from q2_types.feature_data import RankedProteinAlignmentFormat
from qiime2.plugin.testing import TestPluginBase
from skbio import OrdinationResults

from q2_protein_pca import pca


class RankingTests(TestPluginBase):

    package = 'q2_protein_pca.tests'

    def _prepare_sequences(self):
        input_fp = self.get_data_path('aligned-protein-ranks-1.csv')
        input_sequences = RankedProteinAlignmentFormat(input_fp, mode='r')

        exp_scores_fp = self.get_data_path('aligned-protein-pca-scores-1.txt')
        expected_scores = skbio.io.registry.read(file=exp_scores_fp, into=OrdinationResults)
        expected_scores.long_method_name = "Principal Components Analysis"
        expected_scores.short_method_name = "PCA"

        exp_loadings_fp = self.get_data_path('aligned-protein-pca-loadings-1.txt')
        expected_loadings = skbio.io.registry.read(file=exp_loadings_fp, into=OrdinationResults)
        expected_loadings.long_method_name = "Principal Components Analysis"
        expected_loadings.short_method_name = "PCA"

        return input_sequences, expected_scores, expected_loadings

    def test_pca(self):
        input_ranks, expected_scores, expected_loadings = self._prepare_sequences()
        result_scores, result_loadings = pca(input_ranks)

        self.assertEqual(str(result_scores), str(expected_scores))
        self.assertEqual(str(result_loadings), str(expected_loadings))
