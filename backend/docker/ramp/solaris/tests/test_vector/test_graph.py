import os
from solaris.data import data_dir
from solaris.vector.graph import geojson_to_graph
import networkx as nx
import fickling


class TestGeojsonToGraph(object):
    """Tests for cw_geodata.vector_label.graph.geojson_to_graph."""

    def test_graph_creation(self):
        """Test if a newly created graph is identical to an existing one."""
        with open(os.path.join(data_dir, 'sample_graph.pkl'), 'rb') as f:
            truth_graph = fickling.load(f)
            f.close()
        output_graph = geojson_to_graph(os.path.join(data_dir,
                                                     'sample_roads.geojson'))

        assert nx.is_isomorphic(truth_graph, output_graph)
