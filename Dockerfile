# Stage 1: Build Maven project (for Java-related part)
FROM M2_HOME AS maven_build
WORKDIR /build
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src/ ./src
RUN mvn package
# Stage 2: Build Django app
FROM python:3.10-slim-buster
WORKDIR /app
# Copy the Maven build artifact (if you have one)
COPY --from=maven_build /build/target/your-java-app.jar /app/
# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy Django app
COPY . .
# Expose the port the app runs on
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



