const parkingLayout = document.querySelector('.parking-layout');
const availableSlotsText = document.getElementById('available-slots');
const occupiedSlotsText = document.getElementById('occupied-slots');

// Function to generate parking slots dynamically
function generateParkingSlots(numSlots) {
  parkingLayout.innerHTML = ''; // Clear existing slots
  for (let i = 0; i < numSlots; i++) {
    const slot = document.createElement('div');
    slot.classList.add('parking-slot');
    slot.dataset.slotId = i;
    parkingLayout.appendChild(slot);
  }
}

// Update Slot Status
function updateSlotStatus(slotId, status) {
  const slot = document.querySelector(`[data-slot-id="${slotId}"]`);
  if (slot) {
    slot.classList.remove('available', 'occupied');
    slot.classList.add(status);
  }
}

// Start camera processing and communicate with Flask via SocketIO
function startCamera() {
  socket.emit('start_camera'); // Emit a message to Flask to start camera processing
}

// WebSocket Integration for Real-Time Data from Backend
const socket = io.connect('http://localhost:5000');  // Connect to Flask server

socket.on('update_parking_status', function(data) {
  const availableSlots = data.available;
  const occupiedSlots = data.occupied;

  // Update UI dynamically
  availableSlotsText.textContent = `Available Slots: ${availableSlots}`;
  occupiedSlotsText.textContent = `Occupied Slots: ${occupiedSlots}`;

  const numSlots = 36;  // Same as backend
  for (let i = 0; i < numSlots; i++) {
    const status = i < availableSlots ? 'available' : 'occupied';
    updateSlotStatus(i, status);
  }
});
