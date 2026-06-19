As an AI Platform Engineer, you are responsible for managing the massive weight files (checkpoints) generated when training Large Language Models (LLMs).

The Requirements:
Store: Register a new model checkpoint. It requires a checkpoint_id (e.g., "llama-v1"), a parameter_size_billion (int, e.g., 70), and a default status of "stored".


Deploy: Change a checkpoint's status to "deployed" (so the inference API knows it's active).


Archive: Change a checkpoint's status to "archived" (moves it to cold storage like AWS S3 Glacier).

Delete: Completely remove the checkpoint from the registry ONLY IF it is currently "archived". You cannot delete a "stored" or "deployed" model.


View: Allow the user to view all checkpoints currently in the "stored" state.

Your Mission:
Write the full Python script. Maintain absolute Separation of Concerns, and make sure your frontend Driver doesn't get into a paradox with your backend Manager's strict state rules.