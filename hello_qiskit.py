from qiskit import *
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector, plot_histogram, visualize_transition, plot_bloch_vector

circ = QuantumCircuit(1)
circ.h(0)

simulator = Aer.get_backend('statevector_simulator')
result = simulator.run(circ).result()
sv = result.get_statevector(circ)
ct=result.get_counts()
print(ct)

print(sv)

# ---------
from qiskit_ibm_runtime import QiskitRuntimeService

# Save an IBM Quantum account and set it as your default account.
QiskitRuntimeService.save_account(
   channel="ibm_quantum",
   token="00a8ce17fa47bd8ec116db6ace3a621b71ee3b60f7497fafbfe28fb0df16d9c7c023b470dc9eb5ac95014513d5ae5270668f0d85410cf11afc0006a572e25955",
   set_as_default=True,
   # Use `overwrite=True` if you're updating your token.
   overwrite=True,
)

# Load saved credentials
service = QiskitRuntimeService()
#----

from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import EstimatorV2 as Estimator

# Create a new circuit with two qubits
qc = QuantumCircuit(2)

# Add a Hadamard gate to qubit 0
qc.h(0)

# Perform a controlled-X gate on qubit 1, controlled by qubit 0
qc.cx(0, 1)
from qiskit_ibm_runtime import QiskitRuntimeService
# If you did not previously save your credentials, use the following line instead:
# service = QiskitRuntimeService(channel="ibm_quantum", token="")
service = QiskitRuntimeService()
backend = service.least_busy(simulator=False, operational=True)

# Convert to an ISA circuit and layout-mapped observables.
pm = generate_preset_pass_manager(backend=backend, optimization_level=0)
isa_circuit = pm.run(qc)

isa_circuit.draw('mpl', idle_wires=False)

#----------------
plot_bloch_vector([0,1,0], title="New Bloch Sphere")

import numpy as np
from qiskit.visualization import plot_bloch_vector
 
# You can use spherical coordinates instead of cartesian.
 
plot_bloch_vector([1, np.pi/2, np.pi/3], coord_type='spherical')

#----------------
from qiskit import *
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector, plot_histogram, visualize_transition

circ = QuantumCircuit(1)
circ.x(0)

simulator = Aer.get_backend('statevector_simulator')
result = simulator.run(circ).result()
sv = result.get_statevector(circ)
ct=result.get_counts()
#comment the lines and view each out put one by one
print(sv)
plot_bloch_multivector(sv)
visualize_transition(circ)
plot_histogram(ct)

#----------------
from qiskit import *
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector, plot_histogram, visualize_transition

circ = QuantumCircuit(1)
circ.h(0)

simulator = Aer.get_backend('statevector_simulator')
result = simulator.run(circ).result()
sv = result.get_statevector(circ)
ct=result.get_counts()
#comment the lines and view each out put one by one
print(sv)
plot_bloch_multivector(sv)
visualize_transition(circ)
plot_histogram(ct)