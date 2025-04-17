import React, { useState, useEffect, useCallback } from "react";
import { TextField, Button, Table, TableBody, TableCell, TableHead, TableRow, Typography, Card } from "@mui/material";
import api_configuration from "./config"; // Imports reusable value about the REST API for application here.

const WorkItemsPage = () => {
    const [userId, setUserId] = useState("");
    const [workItems, setWorkItems] = useState([]);

    const fetchWorkItems = useCallback(async () => {
        try {
            const response = await fetch(`${api_configuration.API_URL_BASE}/workitems/user/${userId}`);
            if (response.ok) {
                const data = await response.json();
                setWorkItems(data.user_workitems);
            } else {
                console.error("Failed to fetch work items.");
            }
        } catch (error) {
            console.error("Error: ", error);
        }
    }, [userId]); // Re-create fetchWorkItems ONLY when userId changes.

    useEffect(() => {
        if (userId) {
            fetchWorkItems();
        }
    }, [userId, fetchWorkItems ]);

    return (
        <Card style={{ padding: "20px", margin: "auto", marginTop: "20px", maxWidth: "800px" }}>
            <Typography variant="h5" style={{ marginBottom: "20px" }}>
                WorkItems List
            </Typography>
            <TextField
                label="User ID"
                variant="outlined"
                fullWidth
                margin="normal"
                value={userId}
                onChange={(e) => setUserId(e.target.value)}
            />
            <Button variant="contained" color="primary" onClick={fetchWorkItems}>
                Fetch WorkItems
            </Button>
            <Table style={{ marginTop: "20px" }}>
                <TableHead>
                    <TableRow>
                        <TableCell>ID</TableCell>
                        <TableCell>Title</TableCell>
                        <TableCell>Description</TableCell>
                        <TableCell>Status</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {workItems.map((item) => (
                        <TableRow key={item.id}>
                            <TableCell>{item.id}</TableCell>
                            <TableCell>{item.title}</TableCell>
                            <TableCell>{item.description}</TableCell>
                            <TableCell>{item.status}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </Card>
    );
};

export default WorkItemsPage;
