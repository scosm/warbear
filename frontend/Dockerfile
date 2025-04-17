# Frontend Dockerfile (frontend/Dockerfile)
FROM node:18

# Set the working directory
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy frontend code
COPY . .

# Build the React app
RUN npm run build

# Expose the app port
EXPOSE 3000

# Serve the app with a simple server
CMD ["npx", "serve", "-s", "build", "-l", "3000"]
