# Setup Instructions

## Pre-requisites
1. Ensure you have access to a Snowflake account.
2. Install necessary Python dependencies (see `requirements.txt`).
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
1. Configure Snowflake:
   - Set up a Snowflake instance.
   - Add credentials and configurations in `src/config/snowflake_config.py`.
2. Configure Cortex:
   - Ensure Cortex Search and Agents are active.

## Running the Setup
1. Verify document ingestion with:
   ```bash
   python src/ingestion/setup_ingestion.py
   ```
2. Test Cortex Agent query:
   ```
   "What documents are available?"
   ```
3. Execute the end-to-end workflow:
   ```bash
   python src/workflow/process_documents.py
   ```
   - Place your PDF/DOCX files in the `data/` directory prior to execution.

## Notes
- Detailed instructions on Openflow and Cortex configurations will follow.
